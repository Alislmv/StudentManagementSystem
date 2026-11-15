from student import *
from database import *
from utils import *


def menu():
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
            choice = getFloat("enter your choice: ")

            if choice == 1:
                addStudent()
                saveStudents()

            elif choice == 2:
                showAllStudents()

            elif choice == 3:
                updateStudent()
                saveStudents()

            elif choice == 4:
                removeStudent()
                saveStudents()

            elif choice == 5:
                searchStudent()

            elif choice == 6:
                print("Exiting...")

            else:
                print("Wrong choice")

        except ValueError as e:
            print(e)