class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


class Teacher(Person):
    def __init__(self, name, age, gender, subject):
        super().__init__(name, age, gender)
        self.subject = subject

    def get_details(self):
        return f"{super().get_details()}, Subject: {self.subject}"

    def teach(self):
        return f"{self.name} is teaching {self.subject}"


class Student(Person):
    def __init__(self, name, age, gender, student_id):
        super().__init__(name, age, gender)
        self.student_id = student_id
        self.courses = []

    def get_details(self):
        return f"{super().get_details()}, Student ID: {self.student_id}"

    def enroll(self, course):
        self.courses.append(course)
        return f"{self.name} has enrolled in {course}"


class Subject:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def get_details(self):
        return f"Subject: {self.name}, Code: {self.code}"


class Academy:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []
        self.subjects = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_student(self, student):
        self.students.append(student)

    def add_subject(self, subject):
        self.subjects.append(subject)

    def get_teacher_details(self):
        return [teacher.get_details() for teacher in self.teachers]

    def get_student_details(self):
        return [student.get_details() for student in self.students]

    def get_subject_details(self):
        return [subject.get_details() for subject in self.subjects]


# Приклад використання
python_teacher = Teacher("Dmytro Shebetovskiy", 25, "Male", "Python")

student1 = Student("Dmytro Bondarenko", 22, "Male", "S1")

python_subject = Subject("Python", "PY404")


academy = Academy("Hillel")

academy.add_teacher(python_teacher)

academy.add_student(student1)

academy.add_subject(python_subject)

print("Teachers:")
for teacher_detail in academy.get_teacher_details():
    print(teacher_detail)

print("\nStudents:")
for student_detail in academy.get_student_details():
    print(student_detail)

print("\nSubjects:")
for subject_detail in academy.get_subject_details():
    print(subject_detail)

print("\nTeaching:")
for teacher in academy.teachers:
    print(teacher.teach())

print("\nEnrollment:")
for student in academy.students:
    print(student.enroll("Python"))