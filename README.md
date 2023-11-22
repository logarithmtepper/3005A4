# 3005A4
101144900

app.py
-connects to a database to perform specific CRUD (Create, Read, Update, Delete) operations


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
