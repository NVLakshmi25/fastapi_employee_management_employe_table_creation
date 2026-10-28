1. How to explain your project in an interview
Question 1: Tell me about your project.
I developed an Employee Management API using Python and FastAPI. I used MySQL to store employee details and SQLAlchemy to communicate with the database.

My project supports basic CRUD operations. We can create a new employee, retrieve all employees, retrieve one employee by ID, update employee details, and delete an employee.

I also implemented filtering employees by department. I used Pydantic schemas to validate request data and define API responses. I used HTTP status codes and exception handling to manage errors.

This project helped me understand how to build REST APIs and connect a Python application to a database.




2. Understand your project flow
Client / Swagger UI

Sends HTTP requests

FastAPI — main.py

Receives requests and runs endpoints

Pydantic + SQLAlchemy

Validates data and builds database queries

MySQL Database

Stores employee records


For example, when you create an employee, Swagger sends a POST request. FastAPI validates the input, SQLAlchemy saves the employee in MySQL, and the API returns the created employee.
3. Basic interview questions
Practice these answers aloud. They are written as answers from a beginner developer, not as textbook definitions.
Q1. What is FastAPI?
Answer: FastAPI is a Python framework used to build APIs. I used it to create endpoints for employee operations, such as creating, retrieving, updating, and deleting employee records.
Q2. What is an API?
Answer: An API allows two applications to communicate with each other. In my project, the client sends a request to FastAPI, and FastAPI processes the request and returns a response.
Q3. What is a REST API?
Answer: A REST API allows clients to work with resources using HTTP methods such as GET, POST, PUT, and DELETE. In my project, the resource is an employee.
Q4. What is CRUD?
Answer: CRUD stands for Create, Read, Update, and Delete. I implemented these operations for employee records using FastAPI and MySQL.
Q5. Why did you use MySQL?
Answer: I used MySQL because employee information needs to be stored permanently in a database. The records remain available even after the application restarts.
Q6. Why did you use SQLAlchemy?
Answer: SQLAlchemy allows me to interact with the database using Python objects and queries. It reduces the need to write raw SQL for every operation. I used its asynchronous API to execute database queries.
Q7. What is Pydantic?
Answer: Pydantic validates incoming data using Python type hints. In my project, I used Pydantic schemas to check employee details, such as the name, department, and salary, before processing the request.
Q8. What is Swagger UI?
Answer: Swagger UI is an interactive page where I can test my API endpoints. I used /docs to send requests and check the responses without needing a separate frontend application.
4. Questions about your API endpoints
Your code contains six main employee operations. Be ready to explain each one.
HTTP method	Endpoint	Purpose
GET	/employees/	Retrieve all employees
GET	/employees/filter?department=IT	Filter employees by department
GET	/employees/{employee_id}	Retrieve one employee by ID
POST	/employees/	Create an employee
PUT	/employees/{employee_id}	Update an employee
DELETE	/employees/{employee_id}	Delete an employee

Q9. How do you retrieve all employees?
Answer: I use the GET method to retrieve all employees from MySQL. I execute a SQLAlchemy select(Employee) query and use scalars().all() to get all the employee records. Then I return them in the API response.

Important code:
result = await db.execute(select(Employee))employees = result.scalars().all()



Q10. What does select(Employee) mean?
Answer: It creates a SQLAlchemy query to select records from the Employee model. SQLAlchemy uses this model to query the corresponding database table.
Q11. What does scalars().all() do?
Answer: scalars() extracts the employee objects from the query result, and all() returns all matching records as a list.
Q12. How do you filter employees by department?
Answer: I accept the department as a query parameter. Then I use SQLAlchemy's where() condition to retrieve employees belonging to that department.

For example:
select(Employee).where(    Employee.department.ilike(department.strip()))



If the client requests /employees/filter?department=IT, the API returns employees whose department matches IT, ignoring case.
Q13. What is a query parameter?
Answer: A query parameter is a value passed in the URL after a question mark. In my filtering endpoint, department=IT is the query parameter.

Example:
/employees/filter?department=IT


Here, department is the parameter name, and IT is its value.
Q14. What is a path parameter?
Answer: A path parameter is a value included directly in the URL path. I use employee_id to identify one employee.

Example:
/employees/3


Here, 3 is the employee ID.
Q15. What is the difference between a path parameter and a query parameter?
Answer: A path parameter identifies a particular resource, while a query parameter is commonly used to filter or customize a request. In my project, I use the employee ID as a path parameter and the department as a query parameter.
Q16. How do you create an employee?
Answer: I use the POST method. FastAPI receives the employee details through the request body, validates them using EmployeeCreate, and then I create an SQLAlchemy Employee object. I add it to the database session, commit the transaction, and refresh the object to get the saved database values.

Important code:
db.add(new_employee)await db.commit()await db.refresh(new_employee)



Q17. Why do you use db.add()?
Answer: db.add() adds the new employee object to the current SQLAlchemy session. It marks the object for insertion into the database when the transaction is committed.
Q18. Why do you use commit()?
Answer: commit() commits the current transaction so the changes are saved to the database.
Q19. Why do you use refresh()?
Answer: refresh() reloads the object from the database. It helps me access the latest database values, such as an automatically generated employee ID.
Q20. How do you update an employee?
Answer: I first search for the employee using the provided ID. If the employee exists, I update the name, department, and salary. Then I commit the changes and refresh the employee object. If the employee doesn't exist, I return a 404 error.
Q21. How do you delete an employee?
Answer: I first retrieve the employee by ID. If the employee exists, I delete the object and commit the transaction. If no employee is found, I return a 404 error.
Q22. What happens if an employee ID does not exist?
Answer: My API checks whether the query returned an employee. If it returns None, I raise an HTTPException with status code 404 and the message Employee not found.

Example:
if employee is None:    raise HTTPException(        status_code=status.HTTP_404_NOT_FOUND,        detail="Employee not found"    )



5. Questions about important FastAPI concepts
Q23. What is Depends(get_db)?
Answer: Depends() is FastAPI's dependency injection mechanism. In my project, I use Depends(get_db) to provide a database session to an endpoint. This avoids creating a new database session manually inside every endpoint.
Q24. What is AsyncSession?
Answer: AsyncSession is SQLAlchemy's session for asynchronous database operations. I use it with await to execute database queries and commit changes without using the synchronous session API.
Q25. Why do you use async and await?
Answer: I use async def to define asynchronous endpoint functions and await when calling asynchronous database operations. This allows the application to handle other requests while waiting for an asynchronous operation to complete.

Examples from your code:
result = await db.execute(select(Employee))await db.commit()



Q26. What is the purpose of HTTPException?
Answer: HTTPException allows me to return an appropriate HTTP error when something goes wrong. For example, I use a 404 error when an employee is not found and a 500 error when a database operation fails unexpectedly.
Q27. What is response_model?
Answer: response_model tells FastAPI the expected structure of the response. FastAPI uses it to validate and serialize the returned data, and to document the response in Swagger.

For example:
@app.get(    "/employees/{employee_id}",    response_model=EmployeeDataResponse)



In your code, EmployeeDataResponse appears to represent a response containing a message and employee data. The exact structure depends on its definition in schemas/employee.py.
Q28. Why do you use BaseModel?
Answer: I use Pydantic's BaseModel as the base class for my schemas. It lets me define the expected fields and types for employee data.
Q29. What is Field() used for?
Answer: Field() lets me add validation rules to individual fields. For example, I use min_length and max_length for names, and gt=0 to ensure the salary is greater than zero.

From your code:
salary: float = Field(gt=0, le=10000000)



This means the salary must be greater than zero and less than or equal to 10,000,000.
Q30. What is ConfigDict(from_attributes=True)?
Answer: It allows Pydantic to read field values from object attributes, including SQLAlchemy model objects. This is useful when I return database objects from my API instead of manually converting every object into a dictionary.
6. Questions about error handling and HTTP status codes
Q31. What is the difference between 404, 409, and 500?
Answer: A 404 error means the requested employee was not found. A 409 error means the request conflicts with the current database state or violates a constraint. A 500 error means an unexpected server-side problem occurred.
Status code	Meaning in your project
200 OK	The request succeeded
201 Created	An employee was created successfully
404 Not Found	The employee does not exist
409 Conflict	A database constraint or data conflict occurred
422 Unprocessable Entity	The request data failed validation
500 Internal Server Error	An unexpected server or database error occurred

Q32. What is try-except used for?
Answer: I use try-except to handle database errors. If a database operation fails, I catch the exception and return an appropriate HTTP error instead of exposing the raw database error to the client.
Q33. What is SQLAlchemyError?
Answer: SQLAlchemyError is a base exception class for many SQLAlchemy-related errors. I use it to handle database operation failures in my endpoints.
Q34. What is IntegrityError?
Answer: IntegrityError is raised when a database operation violates an integrity constraint, such as a unique constraint or a foreign key constraint. In my POST and PUT endpoints, I catch this error and return a 409 response.

One important point: a database constraint must actually be violated for this exception to occur. It does not mean every invalid input causes an IntegrityError.
Q35. Why do you use rollback()?
Answer: I use rollback() when a database transaction fails. It cancels the uncommitted changes from that transaction and allows the session to recover from the failed operation.

Example:
except SQLAlchemyError:    await db.rollback()    raise HTTPException(        status_code=500,        detail="Could not create employee"    )



Q36. What is the purpose of the lifespan function?
Answer: I use the lifespan function to manage application startup and shutdown. During startup, I check the database connection and create tables if they do not exist. During shutdown, I dispose of the database engine.
Q37. What does Base.metadata.create_all() do?
Answer: It creates the database tables registered with SQLAlchemy's metadata if they do not already exist. It does not automatically migrate existing tables when I change a model. For schema changes, I may need database migrations.
Q38. What is the purpose of the /health endpoint?
Answer: The /health endpoint returns a simple response indicating that the application is running. It is a basic health check. In my current code, it does not independently check the database connection.
Q39. What does /test-db do?
Answer: It executes SELECT 1 against MySQL. If the query succeeds, it returns the result, helping me check whether the application can communicate with the database.

7. Questions about the code an interviewer may notice
These questions are especially useful because an interviewer may ask you to explain or improve your implementation.
Q40. Why are there different response schemas?
Answer: I use different schemas because different endpoints need different response structures. For example, I can use a basic employee schema for employee fields and a wrapper schema when I want to return a message together with the employee data.

Your imports include EmployeeResponse, EmployeeDatabaseResponse, EmployeeDataResponse, EmployeeListResponse, and EmployeeDeleteResponse. Their exact purposes depend on how you defined them in schemas/employee.py.
Q41. Why do you check whether the employee is None?
Answer: The database query may not find a matching employee ID. I check for None before updating or deleting the record, so I don't try to modify an employee that does not exist.
Q42. Why do you put the filter route before the employee-ID route?
Answer: The filter route /employees/filter is a fixed path, while /employees/{employee_id} accepts a variable path value. I register the fixed route first so FastAPI does not interpret the word filter as an employee ID.
Q43. What improvements would you make to this project?
Answer: I would improve the project by separating the routes, schemas, models, and database logic into separate modules. I would also add automated tests, improve input validation, and use database migrations to manage schema changes.

A few practical improvements based on your current code:
- Your create_employee() function accepts joining_date in EmployeeCreate, but it currently doesn't pass that value into Employee.
- Your update_employee() updates only the name, department, and salary. That is fine if those are the only fields you intend to update.
- Your filter endpoint currently returns a wrapper object containing message, department, total_employees, and data. Make sure its response schema matches that structure if you add a response_model.
- Remove the duplicate EmployeeResponse import from your import statement.
- If you later move departments into a separate departments table, you will need to update your model, schemas, and filtering query accordingly.

Based on your schemas/employee.py and models/empTable.py code, let's prepare beginner-friendly interview questions with answers you can speak naturally as a fresher.

Your code has two important parts:
- Pydantic schemas: Validate incoming employee data and define the structure of API responses.
- SQLAlchemy model: Defines how employee information is represented in your MySQL database.
1. Questions about Pydantic schemas
Q1. What is a schema in your project?
Interview answer:

"In my project, I use Pydantic schemas to define the structure of employee data. They help validate the data received from the client and define what information the API should return."

For example, EmployeeCreate defines the fields needed to create an employee.
Q2. Why did you use BaseModel?
Interview answer:

"I use BaseModel from Pydantic to create schemas. It checks the incoming data against the field types and validation rules that I define."

Example from your code:
class EmployeeCreate(BaseModel):    name: str    department: str    salary: float



This tells Pydantic that name and department should be strings, and salary should be a number.
Q3. What is the purpose of EmployeeCreate?
Interview answer:

"EmployeeCreate defines the data required when creating a new employee. In my project, I validate the employee's name, department, salary, and optional joining date before processing the request."
Q4. What is the purpose of Field()?
Interview answer:

"I use Field() to add validation rules to individual fields. For example, I set minimum and maximum lengths for the name and department, and I make sure the salary is greater than zero."

Your code:
name: str = Field(min_length=2, max_length=100)salary: float = Field(gt=0, le=10000000)



The rules mean:
- min_length=2: at least two characters.
- max_length=100: at most 100 characters.
- gt=0: greater than zero.
- le=10000000: less than or equal to 10,000,000.
Q5. What is the difference between EmployeeCreate and EmployeeUpdate?
Interview answer:

"EmployeeCreate defines the data needed to create an employee, while EmployeeUpdate defines the fields that can be updated. In my current code, both schemas require the name, department, and salary. The create schema also includes an optional joining date."

One important detail: your current EmployeeUpdate schema requires all three fields. It is suitable for a full update, not a partial update.
Q6. What does date | None = None mean?
Interview answer:

"It means the joining date is optional. The field can contain a date or None. If the client does not provide the field, its default value is None."

Example:
joining_date: date | None = None



Q7. What is EmailStr?
Interview answer:

"EmailStr is a Pydantic type that validates whether a value follows the expected email address format. I use it for the optional employee email field in my database response schema."

For example, lakshmi@example.com has a valid email format, whereas lakshmi123 does not.

Note that EmailStr checks the format; it does not verify that the email address exists.
Q8. Why did you create EmployeeResponse?
Interview answer:

"I created EmployeeResponse to define the employee fields returned by the API. It includes the employee ID, name, department, and salary. This lets me control which employee fields are included in responses that use this schema."
Q9. What is EmployeeDatabaseResponse?
Interview answer:

"EmployeeDatabaseResponse defines a more detailed employee response. It includes fields such as email, phone, age, city, job title, department, salary, and joining date. I can use it when I want to return more employee details from the database."

Your current EmployeeDatabaseResponse is defined with all these fields, but whether the endpoint returns them depends on which response schema the endpoint declares.
Q10. What is ConfigDict(from_attributes=True)?
Interview answer:

"I use ConfigDict(from_attributes=True) so Pydantic can read values directly from an SQLAlchemy model object. This is useful when I retrieve employee objects from MySQL and return them through FastAPI."

For example:
model_config = ConfigDict(from_attributes=True)



Without this configuration, converting ORM objects to Pydantic models may require a different approach.
2. Questions about response schemas
These questions are based on EmployeeDataResponse, EmployeeListResponse, and EmployeeDeleteResponse.
Q11. Why did you create EmployeeDataResponse?
Interview answer:

"I use EmployeeDataResponse when I want to return a message along with one employee's details. It has two fields: message and data. The data field uses EmployeeResponse to define the employee information."

Your code:
class EmployeeDataResponse(BaseModel):    message: str    data: EmployeeResponse



Example response:
{
  "message": "Employee retrieved successfully",
  "data": {
    "employee_id": 1,
    "name": "Lakshmi",
    "department": "IT",
    "salary": 45000
  }
}


Q12. What is the purpose of EmployeeListResponse?
Interview answer:

"I use EmployeeListResponse to define the response structure when returning multiple employees. It contains a message and a list of employee objects."
class EmployeeListResponse(BaseModel):    message: str    data: list[EmployeeResponse]



Here, list[EmployeeResponse] means that data should contain a list of employee records matching EmployeeResponse.
Q13. What is the purpose of EmployeeDeleteResponse?
Interview answer:

"I created EmployeeDeleteResponse to define the response after deleting an employee. It returns a message and the employee ID."
class EmployeeDeleteResponse(BaseModel):    message: str    data: dict[str, int]



For example:
{
  "message": "Employee deleted successfully",
  "data": {
    "employee_id": 1
  }
}


Q14. What is the difference between a schema and a model?
Interview answer:

"In my project, the Pydantic schema defines how data is validated and returned by the API. The SQLAlchemy model defines the employee table structure and maps Python attributes to database columns."

This is an important distinction to remember during interviews.
3. Questions about your SQLAlchemy model
Q15. What is SQLAlchemy?
Interview answer:

"SQLAlchemy is a Python library that helps applications communicate with relational databases. I use its ORM feature to represent employee records as Python objects and perform database operations."

ORM stands for Object-Relational Mapping.
Q16. What is an ORM model?
Interview answer:

"An ORM model is a Python class that represents a database table. In my project, the Employee class represents the employees table. Its attributes correspond to columns in that table."

Your code:
class Employee(Base):    __tablename__ = "employees"



Q17. Why does your model inherit from Base?
Interview answer:

"I inherit from Base so SQLAlchemy can register my Employee model in its metadata. This allows SQLAlchemy to understand the table structure and use it for database operations."
Q18. What does __tablename__ do?
Interview answer:

"__tablename__ specifies the name of the database table associated with the model. In my project, the Employee model maps to the employees table."
Q19. What is mapped_column()?
Interview answer:

"I use mapped_column() to define the database columns for my SQLAlchemy model. I can specify the column type, whether it is nullable, whether it is a primary key, and other constraints."

For example:
salary: Mapped[float] = mapped_column(    Float,    nullable=False)



This defines a salary column that is required and uses a floating-point database type.
Q20. What does Mapped[int] mean?
Interview answer:

"Mapped is a SQLAlchemy type annotation used to identify attributes that are mapped to database columns. In Mapped[int], the Python attribute is expected to hold an integer."

For example:
employee_id: Mapped[int] = mapped_column(    Integer,    primary_key=True)



Q21. What is a primary key?
Interview answer:

"A primary key uniquely identifies each record in a database table. In my project, employee_id is the primary key, so each employee record has its own identifier."
Q22. What does autoincrement=True mean?
Interview answer:

"It tells the database to generate the next employee ID automatically when a new record is inserted, subject to the database's primary-key configuration."
Q23. What does nullable=False mean?
Interview answer:

"It means the database column cannot contain a SQL NULL value. In my model, the department and salary columns are required."

Your code:
department: Mapped[str] = mapped_column(    String(50),    nullable=False)



Q24. What does nullable=True mean?
Interview answer:

"It means the database column can contain a SQL NULL value. In my model, fields such as email, phone, age, city, and joining date can be left empty in the database."

Remember that a database NULL means the value is missing or unknown; it is different from an empty string.
Q25. Why did you use String(255), Integer, Float, and Date?
Interview answer:

"I use different SQLAlchemy column types according to the kind of information I need to store. String is for text, Integer is for whole numbers, Float is for floating-point numbers, and Date is for calendar dates."

Examples from your model:
Field	Database type	Purpose
name	String(255)	Employee name
age	Integer	Employee age
salary	Float	Employee salary
joining_date	Date	Employee joining date

Q26. What does unique=True mean for email?
Interview answer:

"I set unique=True on the email column so the database prevents duplicate non-null email values. This helps ensure that two employee records do not use the same email address."

Your code also has nullable=True, so email is optional.
Q27. What is the difference between String(20) and Integer for phone numbers?
Interview answer:

"Phone numbers are better stored as strings because they are identifiers, not values used for mathematical calculations. A string can preserve leading zeros and can support symbols such as a plus sign."

For example, +919876543210 is a valid phone-number representation that an integer cannot store directly.

Important correction in your model: You currently have:
phone: Mapped[int | None] = mapped_column(    String(20),    nullable=True)



The Python type and database type do not match. Prefer:
phone: Mapped[str | None] = mapped_column(    String(20),    nullable=True)



Q28. Why is job_title optional?
Your model currently says:
job_title: Mapped[str] = mapped_column(    String(100),    nullable=True)



The database permits NULL, but the Python annotation Mapped[str] says the value should be a string.

If job_title is intended to be optional, use:
job_title: Mapped[str | None] = mapped_column(    String(100),    nullable=True)



Interview answer:

"The job title is optional because an employee record may be created before the job title is provided. I allow the database column to be nullable."

Only use that explanation if it matches your intended application requirements.
4. Questions connecting your schema and model
Q29. Why do you have both EmployeeCreate and Employee?
Interview answer:

"EmployeeCreate validates the information received from the client, while Employee represents the database table. After validating the request, I use the data to create an Employee object and save it in MySQL."

The flow is:
Client sends JSON

EmployeeCreate

Validates the request data

Employee

Creates the SQLAlchemy database object

MySQL employees table


Q30. Why don't you put all validation rules in the SQLAlchemy model?
Interview answer:

"I use Pydantic to validate incoming API data, and I use SQLAlchemy to define the database structure. I can also use database constraints to protect data integrity. Each layer has a different responsibility."
Q31. Why do you use date in both files?
Interview answer:

"I use Python's date type to represent the employee's joining date. In the Pydantic schema, it validates the API input. In the SQLAlchemy model, it maps the field to a database date column."

Your code:
# Pydantic schemajoining_date: date | None = None# SQLAlchemy modeljoining_date: Mapped[date | None] = mapped_column(    Date,    nullable=True)



Q32. Why is EmployeeResponse different from EmployeeDatabaseResponse?
Interview answer:

"EmployeeResponse contains the basic employee details, while EmployeeDatabaseResponse contains additional fields such as email, phone, age, city, and job title. I can choose the response schema according to the data each endpoint needs to return."

A detail to remember: Your EmployeeDataResponse currently uses data: EmployeeResponse, not EmployeeDatabaseResponse. So, even if the database has more fields, an endpoint using EmployeeDataResponse will expose only the fields defined in EmployeeResponse.

If you want all employee fields inside that wrapper, you would need to change the schema to:
class EmployeeDataResponse(BaseModel):    message: str    data: EmployeeDatabaseResponse



Make this change only if your intended API response should include all those fields.
5. Scenario-based interview questions
These questions test whether you understand how the code behaves.
Q33. What happens if the client sends a negative salary?
Interview answer:

"My EmployeeCreate schema has a validation rule that requires salary to be greater than zero. If the client sends a negative salary, FastAPI rejects the request with a 422 validation error before the endpoint processes it."
Q34. What happens if the client sends an invalid email?
Interview answer:

"If the endpoint uses a Pydantic schema with EmailStr for the incoming email field, Pydantic checks the email format and rejects invalid input. In my current code, EmailStr is defined in the database response schema, not in EmployeeCreate."

This distinction matters: your current create schema does not accept an email field.
Q35. What happens if the client sends an employee name with only one character?
Interview answer:

"My EmployeeCreate schema requires the name to have at least two characters. If the client sends a one-character name, Pydantic validation fails and FastAPI returns a 422 error."
Q36. What happens if I change a SQLAlchemy model field?
Interview answer:

"Changing the Python model does not automatically update an existing database table. Base.metadata.create_all() creates missing tables, but it does not perform all schema migrations. For changes to existing tables, I need to update the database schema, preferably using a migration tool such as Alembic."
Q37. Why is it important for the schema and model to match?
Interview answer:

"They should be consistent so the application can validate, store, and return data correctly. If their field names, types, or optional values are inconsistent, the API may produce validation errors or database errors."

6. Final revision sheet
Use this to revise the key concepts before your interview.
Concept	Simple meaning
BaseModel	Base class for Pydantic schemas
Field()	Adds field validation rules
EmployeeCreate	Validates employee creation input
EmployeeUpdate	Defines fields required for updates
EmployeeResponse	Defines basic employee output
EmployeeDatabaseResponse	Defines detailed employee output
ConfigDict(from_attributes=True)	Reads values from object attributes
Base	SQLAlchemy declarative model base
__tablename__	Database table name
Mapped	Type annotation for ORM-mapped attributes
mapped_column()	Defines a database column
primary_key=True	Identifies a row uniquely
nullable=False	Does not allow SQL NULL
unique=True	Enforces uniqueness
String, Integer, Float, Date	Database column types
EmailStr	Validates email format

--------------------------------------------------------------
1. Understand your code first
Your database.py file is responsible for connecting your FastAPI application to the MySQL database and providing database sessions to API endpoints.

1. Environment variables

Read database credentials from the .env file.


2. Database URL and engine

Configure how the application connects to MySQL.


3. Session and Base

Create sessions for database operations and a base class for SQLAlchemy models.


4. get_db()

Provide a database session to an API endpoint and close it after use.


2. Basic interview questions
Q1. What is the purpose of database.py in your project?
Interview answer:

"In my project, database.py manages the database connection. It loads the database configuration, creates the SQLAlchemy engine and session factory, and provides database sessions to my FastAPI endpoints. It also defines the Base class for my database models."
Q2. Which technologies are you using to connect to the database?
Interview answer:

"I am using FastAPI for the API, MySQL as the database, SQLAlchemy as the ORM, and AsyncSession for asynchronous database operations. I use the asyncmy driver to connect SQLAlchemy to MySQL asynchronously."
Q3. What is SQLAlchemy?
Interview answer:

"SQLAlchemy is a Python library that helps us work with databases. It allows us to perform operations like insert, select, update, and delete using Python objects instead of writing every SQL query manually."

Example from your project:
result = await db.execute(select(Employee))employees = result.scalars().all()



This query retrieves employee records using SQLAlchemy.
Q4. What is an ORM?
Interview answer:

"ORM stands for Object-Relational Mapping. It connects Python classes to database tables and Python objects to database records. In my project, the Employee class represents the employees table."
Q5. What is python-dotenv, and why do you use it?
Interview answer:

"I use python-dotenv to load database configuration values from a .env file. This helps me keep database credentials separate from my Python code."

Your code:
from dotenv import load_dotenvload_dotenv()



- load_dotenv() reads the .env file and loads its values into environment variables.
- os.getenv() retrieves those values.
For example, your .env file might contain:
DB_USER=myuser
DB_PASSWORD=mypassword
DB_HOST=localhost
DB_PORT=3306
DB_NAME=employee_db


These are example values, not credentials you should copy blindly. Keep your real .env file private and out of Git.
Q6. What is os.getenv()?
Interview answer:

"os.getenv() is a Python function used to read environment variables. In my project, I use it to get the MySQL username, password, host, port, and database name from the environment."

Your code:
DB_USER = os.getenv("DB_USER", "")DB_PASSWORD = os.getenv("DB_PASSWORD", "")



The first argument is the variable name. The second argument is the default value if that variable is not found.

Important: Your code uses an empty string as the default. If a required setting is missing, the database URL may be invalid. In a real project, I would validate that all required settings are present.
Q7. What is a database URL?
Interview answer:

"A database URL contains the information needed to connect to a database, such as the database type, driver, username, password, host, port, and database name."

Your code:
DATABASE_URL = (    f"mysql+asyncmy://{DB_USER}:{DB_PASSWORD}"    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}")



For example, the URL may look like this:
mysql+asyncmy://myuser:mypassword@localhost:3306/employee_db


Here is what each part means:
Part	Meaning
mysql	Database type
asyncmy	Asynchronous MySQL driver
myuser	Database username
mypassword	Database password
localhost	Database server
3306	MySQL port
employee_db	Database name

Q8. What is asyncmy?
Interview answer:

"asyncmy is a Python driver that allows SQLAlchemy to communicate with MySQL asynchronously. I use it because my project uses asynchronous database operations with AsyncSession."

The driver must be installed in your Python environment for this connection URL to work.
Q9. What is a SQLAlchemy engine?
Interview answer:

"The SQLAlchemy engine manages the connection between my application and the database. It uses the database URL and provides database connections when they are needed."

Your code:
engine = create_async_engine(    DATABASE_URL,    echo=True,    pool_pre_ping=True)



The engine is the central connection manager. It is not the same as a database session.
Q10. What is create_async_engine()?
Interview answer:

"create_async_engine() creates an asynchronous SQLAlchemy engine. It allows my FastAPI application to perform database operations without using the synchronous database engine."

In your code, it is imported from:
from sqlalchemy.ext.asyncio import create_async_engine



Q11. What does echo=True mean?
Interview answer:

"echo=True tells SQLAlchemy to print the SQL statements it executes in the application logs. It helps me understand and debug database queries during development."

For example, you may see a SQL SELECT statement in the terminal.

Note: SQL logs can reveal query details or sensitive values, so avoid enabling verbose SQL logging in production unless it is appropriately controlled.
Q12. What is pool_pre_ping=True?
Interview answer:

"pool_pre_ping=True checks whether a database connection is still alive before SQLAlchemy uses it. It helps avoid errors caused by stale or disconnected connections."

Imagine that MySQL closes an idle connection. The pre-ping check helps SQLAlchemy detect that problem before using the connection.
3. Questions about AsyncSession and sessions
Q13. What is a database session?
Interview answer:

"A database session is used to perform database operations. In my project, I use it to retrieve employees, create new employees, update employee details, and delete employee records."

For example:
result = await db.execute(select(Employee))



Here, db is the database session provided to the endpoint.
Q14. What is AsyncSession?
Interview answer:

"AsyncSession is SQLAlchemy's asynchronous database session. I use it so database operations can be awaited instead of blocking the application in the same way as synchronous operations."

Your import:
from sqlalchemy.ext.asyncio import AsyncSession



Example:
await db.commit()



The await allows the asynchronous operation to complete before the code continues.
Q15. What is async_sessionmaker()?
Interview answer:

"async_sessionmaker() creates a factory for creating asynchronous database sessions. Instead of configuring every session manually, I configure the session factory once and use it whenever an endpoint needs a session."

Your code:
AsyncSessionLocal = async_sessionmaker(    bind=engine,    class_=AsyncSession,    expire_on_commit=False)



- bind=engine: connects the session factory to the database engine.
- class_=AsyncSession: specifies the type of session to create.
- expire_on_commit=False: keeps already-loaded object attributes available after a commit, rather than expiring them automatically.
This setting does not mean that the data can never become outdated in the database.
Q16. What is the difference between an engine and a session?
Interview answer:

"The engine manages database connections, while the session is used to perform database operations. In my project, the engine is created once, and the session factory creates sessions when API endpoints need them."

A simple comparison:
Engine	Session
Manages database connections	Performs database operations
Created with create_async_engine()	Created by AsyncSessionLocal()
Used by the session factory	Used by API endpoints

Q17. Why do you use expire_on_commit=False?
Interview answer:

"I use expire_on_commit=False so that SQLAlchemy does not automatically expire the loaded attributes of an object after a commit. This is useful when I need to return the created or updated employee object in the API response."

For example:
await db.commit()await db.refresh(new_employee)



commit() saves the transaction, and refresh() reloads the object's data from the database.
4. Questions about Base and database models
Q18. What is DeclarativeBase?
Interview answer:

"DeclarativeBase is provided by SQLAlchemy. I use it to define a Base class that my database models inherit from."

Your code:
from sqlalchemy.orm import DeclarativeBaseclass Base(DeclarativeBase):    pass



Q19. Why do you create a Base class?
Interview answer:

"I create a Base class so that my SQLAlchemy models share a common base. SQLAlchemy uses this base to keep track of the model definitions and their table metadata."

For example, your model may look like this:
class Employee(Base):    __tablename__ = "employees"



Because Employee inherits from Base, SQLAlchemy can register its table definition.
Q20. Does defining Base automatically create a MySQL table?
Interview answer:

"No. Defining the Base class and the model describes the table structure, but it does not automatically create the table. In my application, I use Base.metadata.create_all() with the engine connection to create tables that do not already exist."

Your project uses this operation in the FastAPI lifespan setup:
await connection.run_sync(Base.metadata.create_all)



One important detail: create_all() creates missing tables; it does not automatically migrate an existing table when its columns or relationships change.
5. Questions about get_db()
Q21. What is the purpose of get_db()?
Interview answer:

"get_db() provides a database session to my FastAPI endpoints. It creates a session, allows the endpoint to use it, and closes the session when the request finishes."

Your code:
async def get_db():    async with AsyncSessionLocal() as session:        yield session



This function is especially important because you use it to provide database sessions consistently across your API.
Q22. Why do you use async with?
Interview answer:

"I use async with to manage the asynchronous session's lifecycle. It helps ensure that the session is closed when the context finishes, including when an error occurs."

In your code:
async with AsyncSessionLocal() as session:



This creates a session and manages its cleanup.
Q23. Why do you use yield instead of return?
Interview answer:

"I use yield because FastAPI supports yield-based dependencies. It provides the session to the endpoint and allows cleanup to happen after the endpoint has finished using it."

A normal return would end the function immediately and would not provide the same dependency cleanup pattern.
Q24. What is Depends(get_db) in FastAPI?
Interview answer:

"Depends(get_db) tells FastAPI to call get_db() and provide the database session to the endpoint. This avoids creating a new session manually inside every endpoint."

Example from your project:
@app.get("/employees/")async def get_employees(    db: AsyncSession = Depends(get_db)):    result = await db.execute(select(Employee))    employees = result.scalars().all()    return employees



FastAPI obtains the session from get_db() and passes it into the db parameter.
Q25. Does every API request get its own session?
Interview answer:

"Normally, each request that uses this dependency gets its own session. The session is managed for that request and closed after its use. This helps keep database operations separated between requests."

A session is not the same as a permanent database connection. SQLAlchemy manages the underlying connections through the engine's connection pool.
6. Questions about async and error handling
Q26. Why do you use async and await?
Interview answer:

"I use async and await because my application uses asynchronous database operations. async defines an asynchronous function, and await waits for an asynchronous operation to finish without blocking the event loop in the same way as a synchronous call."

Example:
result = await db.execute(select(Employee))await db.commit()



Q27. What happens if the database connection fails?
Interview answer:

"If the database connection fails, the database operation can raise an exception. In my application, I handle database errors in my endpoints and return an appropriate HTTP error response. I also check the database connection during application startup."

Your lifespan setup performs:
await connection.execute(text("SELECT 1"))



This simple query helps verify that the application can communicate with the database during startup.
Q28. Why do you use SELECT 1?
Interview answer:

"SELECT 1 is a simple SQL query that returns the value 1. I use it to check whether the database can execute a basic query successfully without needing to retrieve employee records."

Your code uses it in two places: the application lifespan and the /test-db endpoint.
7. A few important follow-up questions
Q29. Why do you keep database configuration in a separate file?
Interview answer:

"I keep the database configuration in a separate file to make the project organized and easier to maintain. My endpoints can import the database session dependency instead of repeating the connection setup."
Q30. What is connection pooling?
Interview answer:

"Connection pooling means reusing database connections instead of creating a new physical connection for every database operation. SQLAlchemy's engine manages the connection pool, which can improve efficiency."
Q31. What is the difference between synchronous and asynchronous database access?
Interview answer:

"In synchronous code, a database operation generally blocks that execution path until it finishes. In asynchronous code, I use await for supported operations so the event loop can work on other tasks while waiting for the database."
Q32. What packages are needed for this code?
Interview answer:

"I need SQLAlchemy for ORM and session management, asyncmy for asynchronous MySQL connectivity, and python-dotenv to load environment variables from the .env file. I also need a compatible version of Python and the related FastAPI dependencies."

Example installation command:
pip install fastapi uvicorn sqlalchemy asyncmy python-dotenv


If your project already has these packages installed, you do not need to reinstall them.

8. Quick revision: remember these 10 questions
1. What is the purpose of database.py?It configures the database connection and provides sessions to API endpoints.


2. What is SQLAlchemy?It is a Python library for working with databases using Python objects and SQL expressions.


3. What is an engine?It manages database connections.


4. What is AsyncSession?It is used to perform asynchronous database operations.


5. What is async_sessionmaker?It creates a factory for asynchronous database sessions.


6. Why use load_dotenv()?It loads configuration values from the .env file into environment variables.


7. Why use DeclarativeBase?It provides the base class for SQLAlchemy models and their table metadata.


8. Why use Depends(get_db)?It asks FastAPI to provide a database session to the endpoint.


9. Why use yield in get_db()?It provides the session and supports cleanup after the endpoint finishes.


10. Why use pool_pre_ping=True?It checks whether a pooled connection is alive before using it.


9. Final interview answer: explain the entire file
If the interviewer asks, "Can you explain your database configuration code?", you can answer:
"In my Employee Management API project, I use SQLAlchemy with FastAPI to connect to MySQL. First, I load the database configuration from the .env file using python-dotenv and os.getenv(). Then I create an asynchronous engine using create_async_engine() and the asyncmy driver. I use async_sessionmaker() to create database sessions and AsyncSession to perform asynchronous database operations. I define a Base class using DeclarativeBase for my SQLAlchemy models. Finally, I use the get_db() dependency to provide a session to my API endpoints and ensure that the session is cleaned up after use."