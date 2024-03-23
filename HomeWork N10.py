# ООП та Класи

class University:
    def __init__(self, name):
        self.name = name
        self.faculties = []

    def add_faculty(self, faculty):
        self.faculties.append(faculty)


class Faculty:
    def __init__(self, name):
        self.name = name
        self.years = []

    def add_year(self, year):
        self.years.append(year)


class YearOfStudy:
    def __init__(self, year_number):
        self.year_number = year_number
        self.subjects = []
        self.students = []

    def add_subject(self, subject):
        self.subjects.append(subject)

    def add_student(self, student):
        self.students.append(student)


class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def teach(self):
        print(f"{self.name} is teaching {self.subject}")


class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {}

    def take_exam(self, subject, grade):
        self.grades[subject] = grade


class Subject:
    def __init__(self, name):
        self.name = name