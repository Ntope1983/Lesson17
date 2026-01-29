"""
# Sort the students list in descending order by grade
# Python uses the __lt__ method we defined in the Student class to compare students
# reverse=True makes the highest grades come first
"""
import random


class Student:
    def __init__(self, fullname):
        self.fullname = fullname
        self.grade = -1

    def __str__(self):
        return f"{self.fullname}has grade: {self.grade}"

    def __lt__(self, other):
        return self.grade < other.grade


def grade_student(student):
    student.grade = random.randint(0, 10)


def average(lista):
    sum_grade = 0
    for student in lista:
        sum_grade += student.grade
    print(f"The average of the Students grade is: {sum_grade / len(lista)}")


students = [
    "Alex Johnson",
    "Maria Gonzalez",
    "Daniel Thompson",
    "Emily Chen",
    "Michael Brown",
    "Sophia Martinez",
    "James Wilson",
    "Aisha Rahman",
    "Benjamin Carter",
    "Olivia Anderson"
]
total_students = [Student(student) for student in students]

for student in total_students:
    grade_student(student)
total_students.sort(reverse=True)
for student in total_students:
    print(student)

