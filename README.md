# 3005A4
DEMO: https://youtu.be/a6dcisaw9U0


Instructions:
1. Create local database using postgreSQL
2. create students table according to requirements
   CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    enrollment_date DATE);
3. Insert demo data
   INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
   ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
   ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
   ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');
5. run app.py
   python app.py
6. see database changes accodring to data entered in app.py code

app.py:
Connects to a database to perform specific CRUD (Create, Read, Update, Delete) operations

Function dbConnect():
Initializes connection to database using psycopg2 
Also handles errors in case of incorrect credentials
prints message reporting success or failure

Function getAllStudents():
Retrieves and displays all records from the students table
using sql query executed in database seesion by cursor
prints message reporting success or failure

Function addStudent():
Inserts a new student record into the students table.
using sql query executed in database seesion by cursor
prints message reporting success or failure

Function updateStudentEmail():
Updates the email address for a student with the specified student_id
using sql query executed in database seesion by cursor
prints message reporting success or failure

Function deleteStudent():
Deletes the record of the student with the specified student_id
using sql query executed in database seesion by cursor
prints message reporting success or failure

