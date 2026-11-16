from database import *
from utils import *

def addStudent():
    students = loadStudents()
 
    try:
        name = getText("enter name: ").strip()
        surname = getText("enter surname: ").strip()
        age = getInt("enter age: ")
 
        grades = getFloat("enter grades: ")
        grades = [int(grades.strip()) for grades in grades.split(",")]
 
        if not name or not surname:
            print("name and surname cannot be empty!")
            return
 
        if age < 17:
            print("age must be greater than 17!")
            return
 
        if not grades or any(grade < 0 or grade > 100 for grade in grades):
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
    
    studentID = getFloat("enter Car ID: ")
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

            choice = getFloat("Enter choice: ")

            if choice == "1":
                newAge = getInt("Enter new age: ")

                if newAge >= 17:
                    student["age"] = newAge
                    saveStudents(students)
                    print("Age updated successfully!")
                else:
                    print("Age must be 17 or older!")
        
            elif choice == "2":
                newGrade = getInt("Enter new grade: ")
                student["grades"].append(newGrade)
                saveStudents(students)
                print("Grade added successfully!")

            else:
                print("Wong choice.")

        except ValueError as e:
            print(e)

def removeStudent():
    students = loadStudents()
    
    if not students:
        print("No students found.")
        return
    
    deletedID = getFloat("enter deleted student id: ")

    for s in students:
        if s["id"] == deletedID:
            students.remove(s)
            saveStudents(students)
            print("Student deleted")
            break
    else:
        print("Student not found.")

def searchStudent():
    students = loadStudents()
    searchedID = getFloat("enter searched student id: ")

    for s in students:
        if s["id"] == searchedID:
            print(f"""
            ID: {s["id"]}
            Name: {s["name"]}
            Surname: {s["surname"]}
            Age: {s["age"]}
            Grades: {s["grades"]}
        """)
        break
    else:
        print("Student not found.")