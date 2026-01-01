from student import Student
from storage import load_students, save_students
from utils import find_student

def add_student():
    students = load_students()
    student_id = input("Student ID: ")

    if find_student(students, student_id):
        print("Student already exists.")
        return

    name = input("Name: ")
    age = input("Age: ")
    course = input("Course: ")

    student = Student(student_id, name, age, course)
    students.append(student.to_dict())
    save_students(students)

    print("Student added successfully.")

def view_students():
    students = load_students()
    if not students:
        print("No records found.")
        return
    for s in students:
        print(s)

def delete_student():
    students = load_students()
    student_id = input("Enter Student ID to delete: ")

    student = find_student(students, student_id)
    if not student:
        print("Student not found.")
        return

    students.remove(student)
    save_students(students)
    print("Student deleted successfully...")

def menu():
    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Delete Student")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

menu()
