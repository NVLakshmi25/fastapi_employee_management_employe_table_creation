
from contextlib import asynccontextmanager
from fastapi import FastAPI ,HTTPException , status , Depends
from schemas.employee import EmployeeCreate,EmployeeResponse,EmployeeUpdate , EmployeeDatabaseResponse, EmployeeResponse,  EmployeeDataResponse,EmployeeListResponse,EmployeeDeleteResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text, select
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from database import   Base, engine
from dependencies import get_db
from models.empTable import Employee


# Application startup and shutdown
@asynccontextmanager
async def lifespan(app:FastAPI):
    # application Startup
    async with engine.begin() as connection:
        await connection.execute(text("SELECT 1"))
         # Create database tables if they do not exist
        await connection.run_sync(
            Base.metadata.create_all
        )
    print("MySQL connection successful")
    print("Database tables checked/created!")
        # FastAPI starts serving requests after this point
    yield
    
    #shutdown
    await engine.dispose()
    print("Database engine disposed.")

# Create FastAPI application
app = FastAPI(
    title="Employee Management API",
    description="A beginner-friendly Employee Management System",
    version="1.0.0",
    lifespan=lifespan
)


@app.get("/")
async def home():
    return {
        "message": "Welcome to Employee Management API",
        "status": "Application is running"
    }


@app.get("/health")
async def health_check():
    return {
        "status": "healthy"
    }
    
@app.get("/test-db")
async def test_database(
    db:AsyncSession=Depends(get_db)
):
    result =await db.execute(
        text("SELECT 1")
    )
    return{
        "message":"Database conneted  successfully",
        "result":result.scalar()
    }


# --------------------------------------
# GET all employees
@app.get(
    "/employees/",
    response_model=EmployeeListResponse
)
async def get_employees(
    db: AsyncSession = Depends(get_db)
):
    try:
        result = await db.execute(select(Employee))
        employees = result.scalars().all()

        return {
            "message": "Employees retrieved successfully",
            "data": employees
        }

    except SQLAlchemyError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not retrieve employees"
        )


# ------------------------------
# 1. Filter employees by department

@app.get("/employees/filter")
async def filter_employees(
    department: str,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Employee).where(
            Employee.department.ilike(department.strip())
        )
    )

    filtered_employees = result.scalars().all()

    return {
        "message": "Employees filtered successfully",
        "department": department,
        "total_employees": len(filtered_employees),
        "data": filtered_employees
    }

# ------------------------------------------
# retrive one employee  based on ID :
# GET one employee by ID
@app.get(
    "/employees/{employee_id}",
    response_model=EmployeeDataResponse
)
async def get_employee(
    employee_id: int,
    db: AsyncSession = Depends(get_db)
):
    try:
        result = await db.execute(
            select(Employee).where(
                Employee.employee_id == employee_id
            )
        )
        employee = result.scalar_one_or_none()

    except SQLAlchemyError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not retrieve employee"
        )

    if employee is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found"
        )

    return {
        "message": "Employee retrieved successfully",
        "data": employee
    }

# -----------------------------------------------
    


# -----------------------------
# POST create employee
@app.post(
    "/employees/",
    response_model=EmployeeDataResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_employee(
    employee_data: EmployeeCreate,
    db: AsyncSession = Depends(get_db)
):
    new_employee = Employee(
        name=employee_data.name,
        department=employee_data.department,
        salary=employee_data.salary
    )

    try:
        db.add(new_employee)
        await db.commit()
        await db.refresh(new_employee)

    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Employee could not be created because of a data conflict"
        )

    except SQLAlchemyError:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not create employee"
        )

    return {
        "message": "Employee created successfully",
        "data": new_employee
    }

# -----------------------------------
# Update an employee in the temporary list
# PUT update employee
@app.put(
    "/employees/{employee_id}",
    response_model=EmployeeDataResponse
)
async def update_employee(
    employee_id: int,
    employee_data: EmployeeUpdate,
    db: AsyncSession = Depends(get_db)
):
    try:
        result = await db.execute(
            select(Employee).where(
                Employee.employee_id == employee_id
            )
        )
        employee = result.scalar_one_or_none()

        if employee is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Employee not found"
            )

        employee.name = employee_data.name
        employee.department = employee_data.department
        employee.salary = employee_data.salary

        await db.commit()
        await db.refresh(employee)

    except HTTPException:
        raise

    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Employee could not be updated because of a data conflict"
        )

    except SQLAlchemyError:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not update employee"
        )

    return {
        "message": "Employee updated successfully",
        "data": employee
    }
#  ----------------------------------------------------------   
# Delete an employee from the temporary list
# DELETE employee
@app.delete(
    "/employees/{employee_id}",
    response_model=EmployeeDeleteResponse
)
async def delete_employee(
    employee_id: int,
    db: AsyncSession = Depends(get_db)
):
    try:
        result = await db.execute(
            select(Employee).where(
                Employee.employee_id == employee_id
            )
        )
        employee = result.scalar_one_or_none()

        if employee is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Employee not found"
            )

        await db.delete(employee)
        await db.commit()

    except HTTPException:
        raise

    except SQLAlchemyError:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not delete employee"
        )

    return {
        "message": "Employee deleted successfully",
        "data": {
            "employee_id": employee_id
        }
    }



