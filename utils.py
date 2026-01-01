def find_student(students, student_id):
    for student in students:
        if student["student_id"] == student_id:
            return student
    return None
