from database import *


def addStudent():
    students = loadStudents()
 
    try:
        name = input("enter name: ").strip()
        surname = input("enter name: ").strip()
        age = int(input("enter name: "))
 
        grades = input("enter grades: ")
        grades = [int(grades.strip()) for grades in grades.split(",")]
 
        if not name or not surname:
            print("name and surname cannot be empty!")
            return
 
        if age < 17:
            print("age must be greater than 17!")
            return
 
        if not grades or any(grade < 0 and grade > 100 for grade in grades):
            print("grades must be between 0 and 100!")
            return
 
        newStudent = {
            "id": max([student["id"] for student in students], default=0) + 1,
            "name": name,
            "surname": surname,
            "age": age,
            "grades": grades
        }
 
        students.append(newStudent)
 
        if saveStudents(students):
            print("Student added successfully!")
 
    except ValueError:
        print("please enter numeric value...")
 
    except (KeyError, TypeError) as e:
        print("Student data error:", e)

def showAllStudents():
    students = loadStudents()

    if not students:
        print("No students found")
        return

    for s in students:
        print(f"""
        ID: {s["id"]}
        Name: {s["name"]}
        Surname: {s["surname"]}
        Age: {s["age"]}
        Grades: {s["grades"]} 
        """)
def updateStudent():
    students = loadStudents()

    if not students:
        print("No students found.")
        return
    
    studentID = int(input("enter Car ID: "))
    student = None

    for s in students:
        if s["id"] == studentID:
            student = s
            break

    if student is None:
        print("Student not found.")

    else:
        print("Student found.")
        print("""
        1. Update age
        2. Update grade
        """)
        try:

            choice = int(input("Enter choice: "))

            if choice == "1":
                student["age"] = int(input("enter new age: "))
        
            elif choice == "2":
                student["grade"] = int(input("enter new grade: "))

            else:
                print("Wong choice.")

        except ValueError as e:
            print(e)

def removeStudent():
    students = loadStudents()
    
    if not students:
        print("No students found.")
        return
    
    deletedID = int(input("enter deleted student id: "))

    for s in students:
        if s["id"] == deletedID:
            students.remove(s)
            print("Student deleted")
            break

def searchStudent():
    students = loadStudents()
    searchedID = int(input("enter searched student id: "))

    for s in students:
        if s["id"] == searchedID:
            students = s
            break
    else:
        print("Student not found")
        return None