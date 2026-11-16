from student import *
from database import *
from utils import *

def menu():
    loadStudents()

    while True:
        print("""
            === Student Management System ===
            1. Add Student
            2. Show All Students
            3. Update Student
            4. Remove Student
            5. Search Student
            6. Exit
        """)

        try:
            choice = getInt("enter your choice: ")

            if choice == 1:
                addStudent()

            elif choice == 2:
                showAllStudents()

            elif choice == 3:
                updateStudent()

            elif choice == 4:
                removeStudent()
            elif choice == 5:
                searchStudent()

            elif choice == 6:
                print("Exiting...")
                break

            else:
                print("Wrong choice")

        except ValueError as e:
            print(e)

menu()