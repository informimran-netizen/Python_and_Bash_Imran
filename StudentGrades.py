students = {
    "Ali": 95,
    "Rahul": 86,
    "Ahmed": 78,
    "Omkar": 69,
    "Sameer": 56,
}
student = input("Enter student name: ")
if student in students:
    print("Student exists")
else:
    print("Student does not exist")
grade = int(input("Enter grade: "))
students[student] = grade
for student, grade in students.items():
    print(f"{student}: {grade}")