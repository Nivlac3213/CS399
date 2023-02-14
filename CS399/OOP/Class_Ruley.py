"""
Molly Ruley
CS 399
This program makes classes and iterates over classes of the same parent"""


class Students:
    def __init__(self, name, student_id, student_name, marks):
        self.name = name
        self.student_id = student_id
        self.student_name = student_name
        self.marks = marks


class Marks:
    def __init__(self, grades):
        self.grades = grades

    def gpa(self):
        gpa = 0.0
        if self.grades >= 90:
            gpa = 4.0
        elif self.grades >= 80:
            gpa = 3.0
        elif self.grades >= 70:
            gpa = 2.0
        else:
            gpa = 1.0
        return gpa


class Undergraduates(Students):
    def __init__(self, name, student_id, student_name, marks, sat_score):
        super().__init__(name, student_id, student_name, marks)
        self.sat_score = sat_score


class Postgraduates(Students):
    def __init__(self, name, student_id, student_name, marks, bachelors_gpa):
        super().__init__(name, student_id, student_name, marks)
        self.bachelors_gpa = bachelors_gpa


Daniel_marks = Marks(85)
Michael_marks = Marks(100)
Autumn_marks = Marks(110)
Gianni_marks = Marks(70)
w = Postgraduates("Daniel", 8, "Daniel Moreno", Daniel_marks.gpa(), 1460)
x = Undergraduates("Michael", 5, "Michael Stalford", Michael_marks.gpa(), 1500)
y = Postgraduates("Autumn", 7, "Autumn Peterson", Autumn_marks.gpa(), 1480)
z = Undergraduates("Gianni", 4, "Gianni Dragos", Gianni_marks.gpa(), 1400)
students_lst = [w, x, y, z]
for _ in students_lst:
    print(f"{_.name}, {_.marks}")

