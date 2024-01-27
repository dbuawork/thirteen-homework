class Person:
    def __init__(self, name, age, gender):
        self._name = name
        self._age = age
        self._gender = gender

    def get_details(self):
        return f"Name: {self._name}, Age: {self._age}, Gender: {self._gender}"

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_age(self, age):
        if isinstance(age, int) and age > 0:
            self._age = age
        else:
            raise ValueError("Age must be a positive integer")

    def get_age(self):
        return self._age

    def set_gender(self, gender):
        self._gender = gender

    def get_gender(self):
        return self._gender


class Teacher(Person):
    def __init__(self, name, age, gender, subject):
        super().__init__(name, age, gender)
        self._subject = subject

    def get_details(self):
        return f"{super().get_details()}, Subject: {self._subject}"

    def set_subject(self, subject):
        self._subject = subject

    def get_subject(self):
        return self._subject

    def teach(self):
        return f"{self._name} is teaching {self._subject}"


class Student(Person):
    def __init__(self, name, age, gender, student_id):
        super().__init__(name, age, gender)
        self._student_id = student_id
        self._courses = []

    def get_details(self):
        return f"{super().get_details()}, Student ID: {self._student_id}"

    def set_student_id(self, student_id):
        self._student_id = student_id

    def get_student_id(self):
        return self._student_id

    def enroll(self, course):
        self._courses.append(course)
        return f"{self._name} has enrolled in {course}"


class Subject:
    def __init__(self, name, code):
        self._name = name
        self._code = code

    def get_details(self):
        return f"Subject: {self._name}, Code: {self._code}"

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_code(self, code):
        self._code = code

    def get_code(self):
        return self._code


class Academy:
    def __init__(self, name):
        self._name = name
        self._teachers = []
        self._students = []
        self._subjects = []

    def add_teacher(self, teacher):
        self._teachers.append(teacher)

    def add_student(self, student):
        self._students.append(student)

    def add_subject(self, subject):
        self._subjects.append(subject)

    def get_teachers(self):
        return self._teachers

    def get_students(self):
        return self._students

    def get_subjects(self):
        return self._subjects


# Приклад використання
python_teacher = Teacher("Dmytro Shebetovskiy", 25, "Male", "Python")

student1 = Student("Dmytro Bondarenko", 22, "Male", "S1")

python_subject = Subject("Python", "PY404")

academy = Academy("Hillel")

academy.add_teacher(python_teacher)


academy.add_student(student1)

academy.add_subject(python_subject)


print("Teachers:")
for teacher in academy.get_teachers():
    print(teacher.get_details())

print("\nStudents:")
for student in academy.get_students():
    print(student.get_details())

print("\nSubjects:")
for subject in academy.get_subjects():
    print(subject.get_details())

print("\nTeaching:")
for teacher in academy.get_teachers():
    print(teacher.teach())

print("\nEnrollment:")
for student in academy.get_students():
    print(student.enroll("Python"))