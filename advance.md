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