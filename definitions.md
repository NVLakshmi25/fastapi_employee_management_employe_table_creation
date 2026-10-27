1. What is AsyncSession?

AsyncSession is provided by SQLAlchemy. It allows your FastAPI endpoint to perform asynchronous database operations, such as retrieving, inserting, updating, and deleting records.


Q: What is dependency injection in FastAPI?

Answer: Dependency injection is a feature in FastAPI that provides required resources to an endpoint. I use Depends() to inject a database session, so I don't have to create and close a session manually in every API function.

Q: Why do we use AsyncSession?

Answer: AsyncSession is SQLAlchemy's asynchronous database session. It allows my FastAPI application to perform database operations using await, which helps avoid blocking the event loop during I/O operations.

Q: Why do we use yield in get_db()?

Answer: I use yield to provide the database session to the endpoint. After the request finishes, the context manager closes the session.

Q: Does Depends() itself connect to MySQL?

Answer: No. Depends() resolves and injects the dependency. The session factory creates the session, and SQLAlchemy's engine and driver manage communication with MySQL.
--------------------------------------
FastAPI Employee Management API — Interview Questions and Answers

I'll explain your code as if you are a fresher attending a Python FastAPI interview. The answers use simple English that you can speak directly in an interview, followed by a beginner-friendly explanation so you understand what you are saying.

Your code uses four main concepts:

FastAPI for creating API endpoints.

SQLAlchemy for communicating with the MySQL database.

Pydantic for validating and formatting API data.

AsyncSession and async/await for asynchronous database operations.

1. Understand your project flow first

Client / Swagger UI

Sends GET /employees/ request

FastAPI — main.py

Receives the request and calls the endpoint

get_db() — dependencies.py

Provides an async database session

SQLAlchemy — select(Employee)

Queries employee records from MySQL

Pydantic — EmployeeDatabaseResponse

Validates and converts records into response data

JSON Response

Returns the message, employee count, and employee data

Interview answer: Explain how your GET employees API works.

Writing

When the client sends a GET request to the employees endpoint, FastAPI calls the get_employees function. The get_db dependency provides an asynchronous database session. I use SQLAlchemy to fetch employee records from MySQL. Then I use a Pydantic schema to validate the records and return the response as JSON, along with a success message and the total number of employees.

2. FastAPI interview questions
Q1. What is FastAPI?

Interview answer:

Writing

FastAPI is a Python framework used to build APIs. It supports asynchronous programming, request validation, and automatic API documentation through Swagger UI. In my project, I use FastAPI to create endpoints for employee data.

Understand it: An API lets one application communicate with another. Your endpoint /employees/ lets a client request employee records.

Q2. What is an API endpoint?

Interview answer:

Writing

An API endpoint is a URL where a client can send a request to perform an operation. In my project, GET /employees/ is an endpoint that retrieves all employee records from the database.

Q3. What does @app.get("/employees/") mean?
@app.get("/employees/", response_model=dict)
async def get_employees(db: AsyncSession = Depends(get_db)):

Interview answer:

Writing

The @app.get decorator registers a GET endpoint in FastAPI. The path is /employees/. When a client sends a GET request to this path, FastAPI executes the get_employees function. I use GET because I want to retrieve employee data.

@app.get registers a GET route.

"/employees/" is the URL path.

response_model=dict declares the response as a dictionary, although a dedicated Pydantic response schema would provide better validation.

async def defines an asynchronous function.

Q4. What is the difference between GET and POST?

Interview answer:

Writing

GET is used to retrieve data, while POST is generally used to create new data. In my project, GET /employees/ fetches employee records. A POST employees endpoint can accept employee details and save a new employee to the database.

Method

	

Purpose

	

Employee example




GET

	

Retrieve data

	

Get all employees




POST

	

Create data

	

Add an employee




PUT

	

Update data

	

Update employee details




DELETE

	

Delete data

	

Remove an employee

Q5. What is dependency injection in FastAPI?

Look at your parameter:

db: AsyncSession = Depends(get_db)

Interview answer:

Writing

Dependency injection means FastAPI provides a required resource to a function automatically. In my project, Depends(get_db) tells FastAPI to call get_db and provide a database session to the endpoint. This avoids creating a new session manually inside every endpoint.

Understand it: Instead of writing the database connection setup inside get_employees(), you reuse get_db().

3. Database session and asynchronous programming
Q6. What is AsyncSession?

Interview answer:

Writing

AsyncSession is SQLAlchemy's asynchronous database session. I use it to execute database queries without blocking the event loop while waiting for asynchronous database operations. In my project, it helps me retrieve employee records from MySQL.

Understand it: The session is the object your endpoint uses to communicate with the database. AsyncSession is designed for asynchronous operations.

Q7. What is async and await?

Your code:

async def get_employees(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Employee))

Interview answer:

Writing

The async keyword defines an asynchronous function. The await keyword waits for an asynchronous operation to complete before continuing. In my project, I use await when executing a database query because the database operation is asynchronous.

Understand it:

async def — defines a function that can perform asynchronous work.

await — waits for the result of an awaitable operation.

db.execute(...) — executes the SQLAlchemy query asynchronously.

You cannot simply add await to every function call. The operation must support asynchronous execution.

Q8. What is get_db()?

Your code:

from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from database import AsyncSessionLocal

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as db:
        yield db

Interview answer:

Writing

The get_db function provides a database session to FastAPI endpoints. It creates a session using AsyncSessionLocal and yields it to the endpoint. The async with statement manages the session lifecycle and closes the session when it is no longer needed.

Let's understand each part:

Code

	

Meaning




AsyncGenerator

	

Type hint for an asynchronous generator




AsyncSession

	

Type of database session




AsyncSessionLocal()

	

Creates a new session




async with

	

Manages the session's lifecycle




yield db

	

Provides the session to the endpoint

Important correction: Your import should be:

from collections.abc import AsyncGenerator

Not from _collections_abc import AsyncGenerator.

Q9. What is AsyncSessionLocal?

Interview answer:

Writing

AsyncSessionLocal is an asynchronous session factory created using async_sessionmaker. I use it to create database sessions whenever an API endpoint needs to communicate with the database.

For example, your database.py may contain:

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

bind=engine connects the session factory to the database engine.

class_=AsyncSession specifies the asynchronous session class.

expire_on_commit=False prevents ORM objects from having their loaded attributes expired automatically after a commit.

Q10. What is the difference between engine and session?

Interview answer:

Writing

The engine manages database connectivity and the connection pool. A session is used to execute queries and work with database records. In my project, I create an asynchronous engine and use AsyncSessionLocal to create sessions for API requests.

Think of it this way:

Engine: Manages how the application connects to MySQL.

Session: Lets your application work with database records.

4. SQLAlchemy and ORM interview questions
Q11. What is SQLAlchemy?

Interview answer:

Writing

SQLAlchemy is a Python SQL toolkit and ORM. ORM stands for Object Relational Mapper. It lets me work with database tables using Python classes and objects instead of writing every query as raw SQL. In my project, I use SQLAlchemy to retrieve employee records from MySQL.

Q12. What is an ORM model?

Your model starts like this:

class Employee(Base):
    __tablename__ = "employees"

Interview answer:

Writing

An ORM model is a Python class that represents a database table. In my project, the Employee class represents the employees table. Its attributes represent columns such as employee_id, name, department, and salary.

Q13. What is Base?

Interview answer:

Writing

Base is the common declarative base class for my SQLAlchemy models. My Employee model inherits from Base so SQLAlchemy can register the model and its table metadata.

For example:

class Base(DeclarativeBase):
    pass

The pass statement means the class does not define any additional behavior of its own.

Q14. What are Mapped and mapped_column?

Your code:

employee_id: Mapped[int] = mapped_column(
    Integer,
    primary_key=True,
    index=True,
    autoincrement=True
)

Interview answer:

Writing

Mapped is a SQLAlchemy type annotation that describes the Python type of a mapped attribute. mapped_column defines the database column and its properties. In my project, I use them to define the employee ID, name, email, department, and other employee fields.

For the employee ID:

Mapped[int] — the Python value is an integer.

Integer — the database column uses an integer type.

primary_key=True — identifies each employee uniquely.

autoincrement=True — lets the database generate the next ID automatically in the usual MySQL configuration.

index=True — creates an index to help with lookups.

Q15. Explain select(Employee).
result = await db.execute(select(Employee))

Interview answer:

Writing

The select(Employee) statement creates a SQLAlchemy query to retrieve Employee model records. I execute it using await db.execute because my database session is asynchronous. The result contains the records returned by the query.

The equivalent SQL idea is:

SELECT * FROM employees;

This is a conceptual equivalent; SQLAlchemy generates the actual SQL statement.

Q16. What do scalars().all() do?
employee_records = result.scalars().all()

Interview answer:

Writing

The scalars method extracts the Employee objects from the query result. The all method collects all the returned records into a list. I store that list in employee_records so I can count the employees and prepare the API response.

Break it down:

result — contains the query result.

scalars() — extracts the selected ORM objects.

all() — returns all those objects as a list.

Q17. Why do you use len(employee_records)?

Interview answer:

Writing

I use len(employee_records) to count the number of employee records returned by the query. I include that number in the total_employees field of my API response.

If the query returns five employees, len(employee_records) returns 5. If it returns no employees, it returns 0.

5. Pydantic schema interview questions
Q18. What is Pydantic?

Interview answer:

Writing

Pydantic is a Python library used for data validation and serialization. In my FastAPI project, I use Pydantic schemas to define the structure of employee data and validate the data returned by my API.

Q19. What is EmployeeDatabaseResponse?

Your schema:

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

Interview answer:

Writing

EmployeeDatabaseResponse is a Pydantic response schema. It defines which employee fields should be included in the API response and what types they should have. I use it to validate employee objects retrieved from the database before returning them to the client.

Q20. What is BaseModel?

Interview answer:

Writing

BaseModel is the base class provided by Pydantic. I inherit from BaseModel to create schemas such as EmployeeCreate and EmployeeDatabaseResponse. These schemas help validate and structure the data used by my API.

Q21. What is ConfigDict(from_attributes=True)?

Interview answer:

Writing

ConfigDict is used to configure a Pydantic model. The from_attributes=True setting allows Pydantic to read values from an object's attributes. I need it because SQLAlchemy returns Employee objects, and I want to convert those objects into Pydantic response data.

Without this setting, model_validate(employee) may not be able to validate the SQLAlchemy object directly.

Q22. What does model_validate() do?

Your endpoint uses:

EmployeeDatabaseResponse.model_validate(employee)

Interview answer:

Writing

model_validate is a Pydantic v2 method that validates data against a schema. In my project, I use it to validate each SQLAlchemy Employee object against EmployeeDatabaseResponse before including it in the response.

Q23. What is EmailStr?

Interview answer:

Writing

EmailStr is a Pydantic type used to validate email address formats. I use it for the employee email field so the response schema expects a valid email format or None when the field is optional.

For example, ravi@example.com is a valid email format, while ravi@ is not.

You may need to install the email validation dependency:

python -m pip install "pydantic[email]"
Q24. What does str | None = None mean?

Interview answer:

Writing

It means the field can contain a string or None. Setting the default to None means the field is not required when creating the Pydantic model. In my project, I use this for optional fields such as phone, city, and email.

For example:

phone: str | None = None

This allows a phone value such as "9876543210" or None.

Remember: Allowing None and making a field optional are related but different concepts. The default value None makes the field not required in this Pydantic schema.

6. Employee model interview questions
Q25. Why do you define __tablename__?
class Employee(Base):
    __tablename__ = "employees"

Interview answer:

Writing

The tablename attribute specifies the database table represented by the Employee model. In my project, SQLAlchemy maps the Employee class to the employees table in MySQL.

Q26. Why is employee_id the primary key?

Interview answer:

Writing

The primary key uniquely identifies each employee record. I use employee_id as the primary key so each employee has a unique identifier, even if two employees have the same name.

Q27. What is the difference between nullable=True and nullable=False?

Interview answer:

Writing

nullable=True means the database column can store NULL. nullable=False means the column must have a non-NULL value. In my project, fields such as department and salary are required, while email and phone can be NULL.

Q28. Why do you use String(255) or Integer?

Interview answer:

Writing

I use SQLAlchemy column types to define the kind of data stored in each database column. String is used for text, Integer is used for whole numbers, Float is used for decimal numbers, and Date is used for dates.

Examples from your model:

Field

	

Database type

	

Purpose




employee_id

	

Integer

	

Employee identifier




name

	

String(255)

	

Employee name




age

	

Integer

	

Age in whole years




salary

	

Float

	

Salary amount




joining_date

	

Date

	

Joining date

Q29. Why do you use unique=True for email?

Interview answer:

Writing

I use unique=True to prevent duplicate non-NULL email values in the database. This helps ensure that two employee records do not use the same email address.

The database constraint is important because checking for duplicates only in Python is not enough when multiple requests can arrive at the same time.

7. Questions about your API response
Q30. Why do you return a dictionary?
return {
    "message": "Employees retrieved successfully",
    "total_employees": len(employee_records),
    "data": [
        EmployeeDatabaseResponse.model_validate(employee)
        for employee in employee_records
    ],
}

Interview answer:

Writing

I return a dictionary containing a message, the total number of employees, and the employee data. FastAPI converts the returned data into JSON so the client can understand the API response.

Q31. What is response_model=dict?

Interview answer:

Writing

The response_model parameter tells FastAPI what response type the endpoint declares. In my current code, I use dict because the response contains a dictionary. For better validation and documentation, I can create a dedicated Pydantic response schema with message, total_employees, and data fields.

A more structured approach would be:

from pydantic import BaseModel

class EmployeeListResponse(BaseModel):
    message: str
    total_employees: int
    data: list[EmployeeDatabaseResponse]

Then change the endpoint decorator to:

@app.get("/employees/", response_model=EmployeeListResponse)

Your existing return dictionary can remain the same. FastAPI will validate it against EmployeeListResponse.

Q32. What happens if there are no employee records?

Interview answer:

Writing

If there are no employee records, the query returns an empty list. The total_employees value becomes zero, and the data field contains an empty list. The API can still return a successful response with status code 200.

Example:

{
  "message": "Employees retrieved successfully",
  "total_employees": 0,
  "data": []
}
8. Important code issues to correct

Your code is a good learning example, but these details are worth fixing before an interview.

1. Fix the import and code placement

Your pasted code contains:

from models.empTable import Employee ,

If that trailing comma is actually in your Python file, remove it. Imports, route decorators, functions, schemas, and model definitions should be placed in their respective files, not joined together on one line.

2. Correct the phone type annotation

Your model declares:

phone: Mapped[int | None] = mapped_column(
    String(20),
    nullable=True
)

The Python type is int, but the database type is String(20). Because phone numbers are identifiers rather than values used for arithmetic, prefer:

phone: Mapped[str | None] = mapped_column(
    String(20),
    nullable=True
)

Ensure your Pydantic schema also uses str | None.

3. Make job_title consistent

Currently:

job_title: Mapped[str] = mapped_column(
    String(100),
    nullable=True
)

Since the column permits NULL, the Python annotation should reflect that:

job_title: Mapped[str | None] = mapped_column(
    String(100),
    nullable=True
)

4. Your Pydantic ORM conversion is correct

This combination is appropriate for Pydantic v2:

model_config = ConfigDict(from_attributes=True)

and:

EmployeeDatabaseResponse.model_validate(employee)

It works as long as the SQLAlchemy object's attributes match the schema and their values satisfy the schema's validation rules.

One more detail: EmailStr may reject an existing database email that is not in a valid email format. Also, Base.metadata.create_all() creates missing tables but does not automatically change existing columns when you modify your model. For schema changes, use an appropriate database migration or carefully update the table.
-------------------------------------------------
Q: What is response_model in FastAPI?

It defines the expected response structure. FastAPI uses it to validate, serialize, document, and filter the endpoint's output.

Q: Why do we use from_attributes=True?

It allows Pydantic v2 to read values from object attributes, which is useful when returning SQLAlchemy ORM model instances.

Q: How do you retrieve one employee using SQLAlchemy?

I use select(Employee).where(Employee.employee_id == employee_id), execute it asynchronously with the database session, and use scalar_one_or_none() to get the matching record or None.

Q: How do you handle an employee ID that doesn't exist?

I check whether the query returned None. If it did, I raise HTTPException with status code 404 and an appropriate message.
-----------------------------------

Pydantic Response Schemas and GET Employee by ID from MySQL :::

The FastAPI response_model uses that schema to validate and serialize the endpoint's response. It also documents the response structure in Swagger.

2. What is from_attributes=True?

SQLAlchemy returns database records as Python model objects, rather than ordinary dictionaries.

-----------------------------------------------------------------------------------------------

1. Understand the code flow

Swagger UI / Client

Requests /employees/1

FastAPI endpoint

Receives employee_id = 1

SQLAlchemy + MySQL

Finds the employee whose ID is 1

Pydantic EmployeeResponse

Validates and structures the response

JSON response

Returns employee data with HTTP 200, or HTTP 404 if not found

2. Pydantic and response schema questions
Q1. What is Pydantic?

Interview answer:

Writing

Pydantic is a Python library used for data validation and serialization. In my FastAPI project, I use Pydantic schemas to define the structure of employee data and check that the data matches the expected types.

Simple explanation: Pydantic helps ensure that the data returned by your API follows the format you have defined.

Q2. What is a response schema?

Interview answer:

Writing

A response schema defines the structure of the data returned by an API. In my project, EmployeeResponse defines the fields that should be returned for an employee, such as employee_id, name, email, department, and salary.

Your code:

class EmployeeResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    employee_id: int
    name: str
    email: str | None = None
    phone: str | None = None
    age: int | None = None
    city: str | None = None
    job_title: str | None = None
    department: str
    salary: float
    joining_date: date | None = None

The schema defines the fields and their expected types. For example, employee_id should be an integer and salary should be a number.

Q3. What is from_attributes=True?

Interview answer:

Writing

In Pydantic v2, from_attributes=True allows Pydantic to read values from an object's attributes. In my project, SQLAlchemy returns employee records as Python objects, so I use this setting to allow Pydantic to read fields such as employee.name and employee.salary.

Why is it necessary?

SQLAlchemy might give you an object like this:

employee.name
employee.salary

Pydantic can read those attributes when you validate the object:

EmployeeResponse.model_validate(employee)
Q4. What is the difference between EmployeeCreate and EmployeeResponse?

Interview answer:

Writing

EmployeeCreate defines the data required from the client when creating an employee. EmployeeResponse defines the data returned by the API. I keep them separate because some response fields, such as employee_id, are generated by the database and do not need to be provided by the client.

For example:

EmployeeCreate — input from the client.

EmployeeResponse — output sent back to the client.

This makes your API easier to maintain and prevents the client from needing to provide a database-generated ID.

Q5. What is response_model in FastAPI?

Interview answer:

Writing

The response_model parameter defines the expected response structure of an endpoint. FastAPI uses it to validate and serialize the response, document the response in Swagger, and filter the output to the fields defined in the schema.

For retrieving all employees:

@app.get(
    "/employees/",
    response_model=list[EmployeeResponse]
)

This tells FastAPI that the response should be a list of employee records.

For retrieving one employee:

@app.get(
    "/employees/{employee_id}",
    response_model=EmployeeResponse
)

This tells FastAPI that the response should contain one employee object.

3. GET all employees from MySQL
Q6. How do you retrieve all employees from the database?

Interview answer:

Writing

I use the GET /employees/ endpoint to retrieve all employee records. I get an asynchronous database session through Depends(get_db), execute a SQLAlchemy select query, and use scalars().all() to retrieve the employee objects. FastAPI then validates and returns the records using EmployeeResponse.

Your code:

@app.get(
    "/employees/",
    response_model=list[EmployeeResponse]
)
async def get_employees(
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Employee)
    )

    employees = result.scalars().all()

    return employees

Understand the important lines:

Depends(get_db) provides the database session.

select(Employee) builds the query to retrieve employee records.

await db.execute(...) executes the query asynchronously.

result.scalars().all() collects all employee objects into a list.

return employees returns the list to FastAPI.

The equivalent SQL idea is:

SELECT * FROM employees;
Q7. Why do you use list[EmployeeResponse]?

Interview answer:

Writing

I use list[EmployeeResponse] because the GET all employees endpoint returns multiple employee records. Each item in the list should follow the EmployeeResponse schema. If there are no employees, the endpoint returns an empty list.

For example, the response may look like:

[
  {
    "employee_id": 1,
    "name": "Lakshmi",
    "email": "lakshmi@example.com",
    "phone": "9876543210",
    "age": 24,
    "city": "Kakinada",
    "job_title": "Frontend Developer",
    "department": "IT",
    "salary": 45000.0,
    "joining_date": "2026-01-15"
  }
]

These are sample values. Your actual output depends on the records in your MySQL database.

Q8. Why do you return employees directly?

Interview answer:

Writing

I return employees directly because FastAPI can use the response_model to validate and serialize the list. I do not need to convert every employee manually into a dictionary. The response_model also ensures that the output follows the defined schema.

Important: This changes the response format compared with your earlier version. Previously, you returned a dictionary containing message, total_employees, and data. Now you return a plain list. Both designs are possible, but the response schema must match the chosen format.

4. GET employee by ID
Q9. How do you retrieve one employee by ID?

Interview answer:

Writing

I create a GET /employees/{employee_id} endpoint. FastAPI reads the employee ID from the URL. I use a SQLAlchemy select query with a where condition to find the matching employee. If the employee exists, I return the record. If the employee does not exist, I raise an HTTP 404 exception.

Your code:

@app.get(
    "/employees/{employee_id}",
    response_model=EmployeeResponse
)
async def get_employee(
    employee_id: int,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Employee).where(
            Employee.employee_id == employee_id
        )
    )

    employee = result.scalar_one_or_none()

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee
Q10. What is a path parameter?

Interview answer:

Writing

A path parameter is a value included directly in the URL path. In my project, employee_id is a path parameter. For example, in GET /employees/5, the employee ID is 5, and the endpoint searches for that employee in the database.

For example:

GET /employees/5

Here:

employee_id: int

receives the value 5.

Q11. What does .where() do?

Interview answer:

Writing

The where method adds a condition to a SQLAlchemy query. In my project, I use it to find an employee whose employee_id matches the ID provided in the URL.

Your condition:

Employee.employee_id == employee_id

If the requested ID is 5, the equivalent SQL idea is:

SELECT *
FROM employees
WHERE employee_id = 5;
Q12. What is scalar_one_or_none()?

Interview answer:

Writing

scalar_one_or_none() returns the single matching employee object if one exists. If no matching employee exists, it returns None. I use it because employee_id is a primary key, so there should be at most one matching employee.

Remember these two outcomes:

Employee exists → returns the employee object.

Employee does not exist → returns None.

If the query unexpectedly returns multiple rows, this method raises an exception. A primary key prevents duplicate IDs in a correctly defined database table.

Q13. What is HTTPException?

Interview answer:

Writing

HTTPException is used in FastAPI to return an HTTP error response. In my project, I raise HTTPException with status code 404 when the requested employee ID does not exist in the database.

Your code:

raise HTTPException(
    status_code=404,
    detail="Employee not found"
)

This produces a response similar to:

{
  "detail": "Employee not found"
}
Q14. What is HTTP 404?

Interview answer:

Writing

HTTP 404 means the requested resource was not found. In my project, if I search for an employee ID that does not exist in MySQL, I return a 404 response with the message Employee not found.

Q15. What is the difference between HTTP 404 and HTTP 422?

Interview answer:

Writing

HTTP 404 means the requested employee was not found. HTTP 422 means the request data failed validation. For example, requesting an employee with a valid integer ID that does not exist can return 404, while using abc as the employee ID can return 422 because the endpoint expects an integer.

Compare these requests:

Request

	

Expected result




/employees/1, and employee 1 exists

	

200 OK




/employees/9999, and employee 9999 does not exist

	

404 Not Found




/employees/abc

	

422 Unprocessable Entity

The exact result for /employees/1 depends on whether that record exists in your database.

5. Database and routing questions
Q16. What is the difference between an in-memory list and a MySQL query?

Interview answer:

Writing

An in-memory list stores data temporarily in Python while the program is running. A MySQL query retrieves data from the database. In my project, I replaced the temporary employee list with SQLAlchemy queries so the GET endpoints retrieve actual database records.

Simple example:

An in-memory list might look like:

employees = [
    {"employee_id": 1, "name": "Lakshmi"}
]

But your database-backed endpoint uses:

result = await db.execute(select(Employee))

The second approach retrieves records from MySQL rather than relying on a manually created Python list.

Q17. Why do you use AsyncSession and await?

Interview answer:

Writing

I use AsyncSession for asynchronous database operations. The await keyword lets my endpoint wait for the database operation without blocking the event loop in the usual synchronous way. This helps FastAPI handle other requests while asynchronous I/O is waiting.

Q18. Why should static routes come before dynamic routes?

Interview answer:

Writing

I place static routes such as /employees/filter before the dynamic route /employees/{employee_id}. Otherwise, FastAPI may interpret filter as the employee ID and fail integer validation. Correct route ordering helps avoid this problem when the routes use the same HTTP method and overlapping paths.

For example:

@app.get("/employees/filter")
async def filter_employees():
    ...

@app.get("/employees/{employee_id}")
async def get_employee(employee_id: int):
    ...

The static route is defined first.

Q19. How do you test your GET endpoints?

Interview answer:

Writing

I first check that the MySQL database contains employee records. Then I start the FastAPI application and open Swagger UI at /docs. I test GET /employees/ to retrieve all employees, GET /employees/1 to retrieve one employee, and a non-existing ID to check the 404 response.

Your testing process:

Check records in MySQL Workbench:

SELECT * FROM employees;

Start the application:

python -m uvicorn main:app --reload

Open http://127.0.0.1:8000/docs
.

Click Try it out, then Execute for each GET endpoint.

Check the response body and status code.

6. Scenario-based interview questions

These questions check whether you understand how to use the code, not just memorize definitions.

Q20. What happens when the employee ID exists?

Interview answer:

Writing

When the employee ID exists, SQLAlchemy retrieves the matching Employee object. The endpoint returns that object, and FastAPI validates it using EmployeeResponse and sends the employee data as JSON with HTTP 200.

Q21. What happens when the employee ID does not exist?

Interview answer:

Writing

When the ID does not exist, scalar_one_or_none returns None. My code checks that result and raises HTTPException with status code 404 and the message Employee not found.

Q22. Why did you replace the temporary-list lookup?

Interview answer:

Writing

I replaced the temporary-list lookup because I wanted the API to retrieve real employee records from MySQL. The database query makes the endpoint work with the stored records instead of only the data defined in Python memory.

Q23. What improvements did you make in this lesson?

Interview answer:

Writing

In this lesson, I added a Pydantic response schema with from_attributes=True, applied response_model to both GET endpoints, connected the endpoints to MySQL using SQLAlchemy, and added proper 404 handling when an employee is not found.

7. Practice speaking like an interviewee

Try answering each question aloud before revealing the suggested answer.

1. What is response_model?

Reveal answer

2. Why do you use from_attributes=True?

Reveal answer

3. How do you get all employees?

Reveal answer

4. How do you get one employee?

Reveal answer

5. How do you handle a missing employee?

Reveal answer

6. How do you test your API?

Reveal answer
8. Your final interview summary

If the interviewer asks, “Can you explain what you learned in this lesson?”, you can say:

Writing

In this lesson, I learned how to retrieve employee records from MySQL using FastAPI and SQLAlchemy. I created an EmployeeResponse schema using Pydantic and configured from_attributes=True to read values from SQLAlchemy objects. I used response_model to define the API response structure. For retrieving one employee, I used a SQLAlchemy query with a where condition and scalar_one_or_none(). If the employee does not exist, I raise an HTTP 404 exception. Finally, I test the endpoints using Swagger UI.

----------------------------------------------------------------------

Now we'll migrate the PUT endpoint so it updates an existing employee directly in the database.
We'll cover:

Understand PUT and the EmployeeUpdate schema.

Add the schema to schemas/employee.py.

Find an employee using SQLAlchemy.

Update the employee, commit, and refresh.

Handle missing employees with HTTP 404.

Test the endpoint in Swagger and verify the changes in MySQL Workbench.

------------------------------------------------------------------
1. Understand the code flow
Swagger UI / Client
Requests /employees/1

FastAPI endpoint
Receives employee_id = 1

SQLAlchemy + MySQL
Finds the employee whose ID is 1

Pydantic EmployeeResponse
Validates and structures the response

JSON response
Returns employee data with HTTP 200, or HTTP 404 if not found


2. Pydantic and response schema questions
Q1. What is Pydantic?
Interview answer:
Pydantic is a Python library used for data validation and serialization. In my FastAPI project, I use Pydantic schemas to define the structure of employee data and check that the data matches the expected types.




Simple explanation: Pydantic helps ensure that the data returned by your API follows the format you have defined.
Q2. What is a response schema?
Interview answer:
A response schema defines the structure of the data returned by an API. In my project, EmployeeResponse defines the fields that should be returned for an employee, such as employee_id, name, email, department, and salary.




Your code:
class EmployeeResponse(BaseModel):    model_config = ConfigDict(from_attributes=True)    employee_id: int    name: str    email: str | None = None    phone: str | None = None    age: int | None = None    city: str | None = None    job_title: str | None = None    department: str    salary: float    joining_date: date | None = None



The schema defines the fields and their expected types. For example, employee_id should be an integer and salary should be a number.
Q3. What is from_attributes=True?
Interview answer:
In Pydantic v2, from_attributes=True allows Pydantic to read values from an object's attributes. In my project, SQLAlchemy returns employee records as Python objects, so I use this setting to allow Pydantic to read fields such as employee.name and employee.salary.




Why is it necessary?
SQLAlchemy might give you an object like this:
employee.nameemployee.salary



Pydantic can read those attributes when you validate the object:
EmployeeResponse.model_validate(employee)



Q4. What is the difference between EmployeeCreate and EmployeeResponse?
Interview answer:
EmployeeCreate defines the data required from the client when creating an employee. EmployeeResponse defines the data returned by the API. I keep them separate because some response fields, such as employee_id, are generated by the database and do not need to be provided by the client.




For example:
- EmployeeCreate — input from the client.
- EmployeeResponse — output sent back to the client.
This makes your API easier to maintain and prevents the client from needing to provide a database-generated ID.
Q5. What is response_model in FastAPI?
Interview answer:
The response_model parameter defines the expected response structure of an endpoint. FastAPI uses it to validate and serialize the response, document the response in Swagger, and filter the output to the fields defined in the schema.




For retrieving all employees:
@app.get(    "/employees/",    response_model=list[EmployeeResponse])



This tells FastAPI that the response should be a list of employee records.
For retrieving one employee:
@app.get(    "/employees/{employee_id}",    response_model=EmployeeResponse)



This tells FastAPI that the response should contain one employee object.

3. GET all employees from MySQL
Q6. How do you retrieve all employees from the database?
Interview answer:
I use the GET /employees/ endpoint to retrieve all employee records. I get an asynchronous database session through Depends(get_db), execute a SQLAlchemy select query, and use scalars().all() to retrieve the employee objects. FastAPI then validates and returns the records using EmployeeResponse.




Your code:
@app.get(    "/employees/",    response_model=list[EmployeeResponse])async def get_employees(    db: AsyncSession = Depends(get_db)):    result = await db.execute(        select(Employee)    )    employees = result.scalars().all()    return employees



Understand the important lines:
- Depends(get_db) provides the database session.
- select(Employee) builds the query to retrieve employee records.
- await db.execute(...) executes the query asynchronously.
- result.scalars().all() collects all employee objects into a list.
- return employees returns the list to FastAPI.
The equivalent SQL idea is:
SELECT * FROM employees;


Q7. Why do you use list[EmployeeResponse]?
Interview answer:
I use list[EmployeeResponse] because the GET all employees endpoint returns multiple employee records. Each item in the list should follow the EmployeeResponse schema. If there are no employees, the endpoint returns an empty list.




For example, the response may look like:
[
  {
    "employee_id": 1,
    "name": "Lakshmi",
    "email": "lakshmi@example.com",
    "phone": "9876543210",
    "age": 24,
    "city": "Kakinada",
    "job_title": "Frontend Developer",
    "department": "IT",
    "salary": 45000.0,
    "joining_date": "2026-01-15"
  }
]


These are sample values. Your actual output depends on the records in your MySQL database.
Q8. Why do you return employees directly?
Interview answer:
I return employees directly because FastAPI can use the response_model to validate and serialize the list. I do not need to convert every employee manually into a dictionary. The response_model also ensures that the output follows the defined schema.




Important: This changes the response format compared with your earlier version. Previously, you returned a dictionary containing message, total_employees, and data. Now you return a plain list. Both designs are possible, but the response schema must match the chosen format.
4. GET employee by ID
Q9. How do you retrieve one employee by ID?
Interview answer:
I create a GET /employees/{employee_id} endpoint. FastAPI reads the employee ID from the URL. I use a SQLAlchemy select query with a where condition to find the matching employee. If the employee exists, I return the record. If the employee does not exist, I raise an HTTP 404 exception.




Your code:
@app.get(    "/employees/{employee_id}",    response_model=EmployeeResponse)async def get_employee(    employee_id: int,    db: AsyncSession = Depends(get_db)):    result = await db.execute(        select(Employee).where(            Employee.employee_id == employee_id        )    )    employee = result.scalar_one_or_none()    if employee is None:        raise HTTPException(            status_code=404,            detail="Employee not found"        )    return employee



Q10. What is a path parameter?
Interview answer:
A path parameter is a value included directly in the URL path. In my project, employee_id is a path parameter. For example, in GET /employees/5, the employee ID is 5, and the endpoint searches for that employee in the database.




For example:
GET /employees/5
Here:
employee_id: int



receives the value 5.
Q11. What does .where() do?
Interview answer:
The where method adds a condition to a SQLAlchemy query. In my project, I use it to find an employee whose employee_id matches the ID provided in the URL.




Your condition:
Employee.employee_id == employee_id



If the requested ID is 5, the equivalent SQL idea is:
SELECT *
FROM employees
WHERE employee_id = 5;


Q12. What is scalar_one_or_none()?
Interview answer:
scalar_one_or_none() returns the single matching employee object if one exists. If no matching employee exists, it returns None. I use it because employee_id is a primary key, so there should be at most one matching employee.




Remember these two outcomes:
- Employee exists → returns the employee object.
- Employee does not exist → returns None.
If the query unexpectedly returns multiple rows, this method raises an exception. A primary key prevents duplicate IDs in a correctly defined database table.
Q13. What is HTTPException?
Interview answer:
HTTPException is used in FastAPI to return an HTTP error response. In my project, I raise HTTPException with status code 404 when the requested employee ID does not exist in the database.




Your code:
raise HTTPException(    status_code=404,    detail="Employee not found")



This produces a response similar to:
{
  "detail": "Employee not found"
}


Q14. What is HTTP 404?
Interview answer:
HTTP 404 means the requested resource was not found. In my project, if I search for an employee ID that does not exist in MySQL, I return a 404 response with the message Employee not found.




Q15. What is the difference between HTTP 404 and HTTP 422?
Interview answer:
HTTP 404 means the requested employee was not found. HTTP 422 means the request data failed validation. For example, requesting an employee with a valid integer ID that does not exist can return 404, while using abc as the employee ID can return 422 because the endpoint expects an integer.




Compare these requests:
Request	Expected result
/employees/1, and employee 1 exists	200 OK
/employees/9999, and employee 9999 does not exist	404 Not Found
/employees/abc	422 Unprocessable Entity
The exact result for /employees/1 depends on whether that record exists in your database.

5. Database and routing questions
Q16. What is the difference between an in-memory list and a MySQL query?
Interview answer:
An in-memory list stores data temporarily in Python while the program is running. A MySQL query retrieves data from the database. In my project, I replaced the temporary employee list with SQLAlchemy queries so the GET endpoints retrieve actual database records.




Simple example:
An in-memory list might look like:
employees = [    {"employee_id": 1, "name": "Lakshmi"}]



But your database-backed endpoint uses:
result = await db.execute(select(Employee))



The second approach retrieves records from MySQL rather than relying on a manually created Python list.
Q17. Why do you use AsyncSession and await?
Interview answer:
I use AsyncSession for asynchronous database operations. The await keyword lets my endpoint wait for the database operation without blocking the event loop in the usual synchronous way. This helps FastAPI handle other requests while asynchronous I/O is waiting.




Q18. Why should static routes come before dynamic routes?
Interview answer:
I place static routes such as /employees/filter before the dynamic route /employees/{employee_id}. Otherwise, FastAPI may interpret filter as the employee ID and fail integer validation. Correct route ordering helps avoid this problem when the routes use the same HTTP method and overlapping paths.




For example:
@app.get("/employees/filter")async def filter_employees():    ...@app.get("/employees/{employee_id}")async def get_employee(employee_id: int):    ...



The static route is defined first.
Q19. How do you test your GET endpoints?
Interview answer:
I first check that the MySQL database contains employee records. Then I start the FastAPI application and open Swagger UI at /docs. I test GET /employees/ to retrieve all employees, GET /employees/1 to retrieve one employee, and a non-existing ID to check the 404 response.




Your testing process:
1. Check records in MySQL Workbench:
   SELECT * FROM employees;
2. Start the application:
   python -m uvicorn main:app --reload
3. Open http://127.0.0.1:8000/docs.
4. Click Try it out, then Execute for each GET endpoint.
5. Check the response body and status code.
6. Scenario-based interview questions
These questions check whether you understand how to use the code, not just memorize definitions.
Q20. What happens when the employee ID exists?
Interview answer:
When the employee ID exists, SQLAlchemy retrieves the matching Employee object. The endpoint returns that object, and FastAPI validates it using EmployeeResponse and sends the employee data as JSON with HTTP 200.




Q21. What happens when the employee ID does not exist?
Interview answer:
When the ID does not exist, scalar_one_or_none returns None. My code checks that result and raises HTTPException with status code 404 and the message Employee not found.




Q22. Why did you replace the temporary-list lookup?
Interview answer:
I replaced the temporary-list lookup because I wanted the API to retrieve real employee records from MySQL. The database query makes the endpoint work with the stored records instead of only the data defined in Python memory.




Q23. What improvements did you make in this lesson?
Interview answer:
In this lesson, I added a Pydantic response schema with from_attributes=True, applied response_model to both GET endpoints, connected the endpoints to MySQL using SQLAlchemy, and added proper 404 handling when an employee is not found.





7. Practice speaking like an interviewee
Try answering each question aloud before revealing the suggested answer.
1. What is response_model?
Reveal answer

2. Why do you use from_attributes=True?
Reveal answer

3. How do you get all employees?
Reveal answer

4. How do you get one employee?
Reveal answer

5. How do you handle a missing employee?
Reveal answer

6. How do you test your API?
Reveal answer

8. Your final interview summary
If the interviewer asks, “Can you explain what you learned in this lesson?”, you can say:
In this lesson, I learned how to retrieve employee records from MySQL using FastAPI and SQLAlchemy. I created an EmployeeResponse schema using Pydantic and configured from_attributes=True to read values from SQLAlchemy objects. I used response_model to define the API response structure. For retrieving one employee, I used a SQLAlchemy query with a where condition and scalar_one_or_none(). If the employee does not exist, I raise an HTTP 404 exception. Finally, I test the endpoints using Swagger UI.

-------------------------------------------
Q: What is response_model in FastAPI?

It defines the expected response structure. FastAPI uses it to validate, serialize, document, and filter the endpoint's output.

Q: Why do we use from_attributes=True?

It allows Pydantic v2 to read values from object attributes, which is useful when returning SQLAlchemy ORM model instances.

Q: How do you retrieve one employee using SQLAlchemy?

I use select(Employee).where(Employee.employee_id == employee_id), execute it asynchronously with the database session, and use scalar_one_or_none() to get the matching record or None.

Q: How do you handle an employee ID that doesn't exist?

I check whether the query returned None. If it did, I raise HTTPException with status code 404 and an appropriate message.
-----------------------------------------------------
Goal: When a client sends a POST request, FastAPI validates the data, saves the employee in MySQL, and returns the newly created record with its database-generated ID.

----------------------------
Q: How do you insert a record into MySQL using SQLAlchemy?

I create a SQLAlchemy model object using the validated request data, add it to the session with db.add(), commit the transaction using await db.commit(), and refresh it with await db.refresh() to retrieve generated values.

Q: Why do we use commit()?

commit() saves the pending transaction to the database. Without it, the new record may not be persisted.

Q: Why do we use refresh() after committing?

refresh() reloads the object from the database so we can access generated or updated values, such as the auto-increment employee ID.

Q: Why return HTTP 201?

HTTP 201 Created indicates that the request successfully created a new resource.

---------------------------------
Q: How do you insert a record into MySQL using SQLAlchemy?

I create a SQLAlchemy model object using the validated request data, add it to the session with db.add(), commit the transaction using await db.commit(), and refresh it with await db.refresh() to retrieve generated values.

Q: Why do we use commit()?

commit() saves the pending transaction to the database. Without it, the new record may not be persisted.

Q: Why do we use refresh() after committing?

refresh() reloads the object from the database so we can access generated or updated values, such as the auto-increment employee ID.

Q: Why return HTTP 201?

HTTP 201 Created indicates that the request successfully created a new resource.
---------------------------------------------
Goal: Update an employee's details in MySQL using a PUT request, without using the temporary Python list.

1. What is PUT?

PUT is an HTTP method used to update an existing resource. In this lesson, we'll require all three editable fields—name, department, and salary—in the request body.
---------------------------------------------------

1. What is the DELETE method?
The HTTP DELETE method requests removal of a resource.

Q: How do you delete an employee using FastAPI and SQLAlchemy?

I retrieve the employee from the database using its ID. If the employee doesn't exist, I return HTTP 404. Otherwise, I delete the ORM object using db.delete(), commit the transaction, and return a success message.

Q: Why do we retrieve the employee before deleting it?

To verify that the employee exists and return a meaningful 404 response if the requested record cannot be found.

Q: What is the purpose of commit() in a DELETE operation?

It commits the pending deletion to the database. Without a successful commit, the deletion isn't guaranteed to be persisted.

Q: What is the difference between hard delete and soft delete?

A hard delete removes the database row. A soft delete marks the record as inactive or deleted while retaining its data for historical reference.
---------------------------------------------------------------
Added EmployeeUpdate to schemas/employee.py
[x] Added the database-backed PUT endpoint
[x] Retrieved the employee using SQLAlchemy select()
[x] Returned HTTP 404 for a missing employee
[x] Updated the editable fields
[x] Committed the changes and refreshed the object
[x] Returned the updated employee with EmployeeResponse
[x] Tested successful updates and validation errors in Swagger
[x] Verified the updated values in MySQL Workbench
------------------------------------------------------
Added the database-backed DELETE endpoint.
[x] Retrieved the employee using SQLAlchemy.
[x] Returned HTTP 404 when the employee didn't exist.
[x] Deleted the ORM object using await db.delete(employee).
[x] Committed the transaction with await db.commit().
[x] Returned a JSON success message.
[x] Tested successful and unsuccessful deletions in Swagger.
[x] Verified the deleted record was gone in MySQL Workbench.






