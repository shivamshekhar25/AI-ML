# Student Enrolments

# Given a list of tuples with information (name, subject):

# 1 List all unique courses.





students = [
    ("Shivam", "Python"),
    ("Aman", "English"),
    ("Rahul", "Python"),
    ("Priya", "Math"),
    ("Aman", "English")
]
courses = set()

for student in students:
    courses.add(student[1])

print(courses)



# 2 List students enrolled in English.

students = [
    ("Shivam", "Python"),
    ("Aman", "English"),
    ("Rahul", "Python"),
    ("Priya", "Math"),
    ("Neha", "English"),
    ("Aman", "English")
]

english_students = []

for student in students:
    if student[1] == "English":
        english_students.append(student[0])

print(english_students)



# 3 Create a dictionary (student, set of courses).


students = [
    ("Shivam", "Python"),
    ("Aman", "English"),
    ("Rahul", "Python"),
    ("Priya", "Math"),
    ("Neha", "English"),
    ("Aman", "English")
]

student_courses = {}

for student in students:
    name = student[0]
    course = student[1]

    if name not in student_courses:
        student_courses[name] = set()

    student_courses[name].add(course)

print(student_courses)