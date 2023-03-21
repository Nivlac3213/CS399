"""
Tri Phan
13 February 2023
CS 399 Intermediate Python Programming
Object-Oriented Programming In Python - Student, Marks, Undergraduate, and Postgraduate
"""

# Class Stuff
class Student:

    def __init__(self, name: str, student_id: float, student_name: str, marks: float):
        self.name = name
        self.student_id = student_id
        self.student_name = student_name
        self.marks = marks

    def get_name(self):
        return self.get_name()

    def get_student_id(self):
        return self.student_id

    def get_student_name(self):
        return self.student_name

    def get_marks(self):
        return self.marks


class Undergraduate(Student):
    def __init__(self, name, student_id, student_name, marks, sat_score):
        super().__init__(name, student_id, student_name, marks)
        self.sat_score = sat_score


class Postgraduate(Student):
    def __init__(self, name, student_id, student_name, marks, bachelors_gpa):
        super().__init__(name, student_id, student_name, marks)
        self.sat_score = bachelors_gpa


# Examples
Ian = Undergraduate('Ian', 2512697, 'Ian Jones', 60, 1220)
John = Undergraduate('John', 3213544, 'Johnny Test', 60, 1500)
Mabel = Undergraduate('Mabel', 1531858, 'Mabel Pines', 60, 1312)
Marissa = Postgraduate('Marissa', 1531578, 'Marissa Jenkins', 60, 3.8)
Manny = Postgraduate('Manny', 3654875, 'Manny Timmy', 60, 2.6)
Warna = Postgraduate('Warna', 1542368, 'Warna Brothas', 60, 4.3)

#Poly
students = [Ian, John, Mabel, Marissa, Manny, Warna]
for student in students:
    print(student.name, ',', student.student_name, ' has Marks:', student.marks)
    print('Are they an Undergrad?', isinstance(student, Undergraduate), '\n')
