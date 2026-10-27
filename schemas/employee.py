
from pydantic import BaseModel, Field, ConfigDict, EmailStr
from datetime import date


# Schema for creating an employee
class EmployeeCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    department: str = Field(min_length=2, max_length=50)
    salary: float = Field(gt=0, le=10000000)
    joining_date: date | None = None


# Schema for updating an employee
class EmployeeUpdate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    department: str = Field(min_length=2, max_length=50)
    salary: float = Field(gt=0, le=10000000)


# Schema for the standard employee response
class EmployeeResponse(BaseModel):
    employee_id: int
    name: str
    department: str
    salary: float

    model_config = ConfigDict(from_attributes=True)


# Schema for returning all database employee fields
class EmployeeDatabaseResponse(BaseModel):
    employee_id: int
    name: str
    email: EmailStr | None = None
    phone: str | None = None
    age: int | None = None
    city: str | None = None
    job_title: str | None = None
    department: str
    salary: float
    joining_date: date | None = None

    model_config = ConfigDict(from_attributes=True)


class EmployeeDataResponse(BaseModel):
    message: str
    data: EmployeeResponse


class EmployeeListResponse(BaseModel):
    message: str
    data: list[EmployeeResponse]


class EmployeeDeleteResponse(BaseModel):
    message: str
    data: dict[str, int]
