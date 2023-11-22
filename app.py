# PostgreSQL database adapter
import psycopg2
from psycopg2 import sql

'''
Function dbConnect():
Initialize connection to database 
handles errors in case of incorrect credentials 
'''
def dbConnect():
#connection attempt
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="password",
            host="localhost",
            port="5432",
            database="3005A4"
        )
        return connection
#error handling
    except psycopg2.Error as e:
        print("Error connecting to database:", e)
        return None

'''
Function getAllStudents():
Retrieves and displays all records from the students table
'''
def getAllStudents():
#establish connection to database
    connection = dbConnect()
    if connection:
        try:
#execute PostgreSQL command in database session to fetch student data
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM students")
                students = cursor.fetchall()
                for student in students:
                    print(student)
#Error handling
        except psycopg2.Error as e:
            print("Error fetching data:", e)
        finally:
            connection.close()

'''
Function addStudent():
Inserts a new student record into the students table.
'''
def addStudent(first_name, last_name, email, enrollment_date):
#establish connection to database
    connection = dbConnect()
    if connection:
        try:
#execute PostgreSQL command in database session to fetch student data
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
                    (first_name, last_name, email, enrollment_date)
                )
                connection.commit()
                print("Student added successfully.")
#exception handling
        except psycopg2.IntegrityError as e:
            print("Error adding student:", e)
            connection.rollback()
        finally:
            connection.close()

'''
Function updateStudentEmail():
Updates the email address for a student with the specified student_id.
'''
def updateStudentEmail(student_id, new_email):
#establish database connection
    connection = dbConnect()
    if connection:
        try:
#execute PostgreSQL command in database session 
#to update the email for a student with the specified student_id
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE students SET email = %s WHERE student_id = %s",
                    (new_email, student_id)
                )
                connection.commit()
                print("Email updated successfully.")
#exception handling
        except psycopg2.Error as e:
            print("Error updating email:", e)
            connection.rollback()
        finally:
            connection.close()

'''
Function deleteStudent():
Deletes the record of the student with the specified student_id.
'''
def deleteStudent(student_id):
#establish connection to database
    connection = dbConnect()
    if connection:
        try:
#execute PostgreSQL command in database session 
#to delete the record of the student with the specified student_id
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM students WHERE student_id = %s",
                    (student_id,)
                )
                connection.commit()
                print("Student deleted successfully.")
#exception handling
        except psycopg2.Error as e:
            print("Error deleting student:", e)
            connection.rollback()
        finally:
            connection.close()

#testing functions
if __name__ == "__main__":
    getAllStudents()
    addStudent("New", "Student", "new.student@example.com", "2023-09-03")
    updateStudentEmail(1, "john.new@example.com")
    deleteStudent(2)
    getAllStudents()
