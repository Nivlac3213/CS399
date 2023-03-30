"""
Author:     Calvin Henggeler
Date:       February 2, 2023
Course:     SUSlist_HW Intermediate Python

Description:
            This python file is made to complete Homework 2 on the topic of
            Object-Oriented Programming (OOP).
Disclaimers:
            None, No Artificial Intelligence tools used
Sources:
            No external Sources Used
"""

# =========================================================================== #
#                                   Imports                                   #
# =========================================================================== #
from random import randint


# =========================================================================== #
#                                   Classes                                   #
# =========================================================================== #
class Marks:
    """
    Marks Super Class
    IDK what this is, Grades probably?
    """
    # --- Attributes --- #
    course = " "
    letter_grade = " "
    percent = 0.0

    # ---  Methods  --- #
    def __init__(self, course: str, percent: float):
        self.course = course
        self.percent = percent
        self.letter_grade = (self.calculate_letter_grade(self.percent))

    @property
    def percent(self):
        return self._percent

    @percent.setter
    def percent(self, value: float):
        """
        Ensures that grades are a real value > 0
        :param value: grade percentage -> float
        :return: None
        """
        if value < 0:
            raise ValueError("Grade below 0% is not possible")
        self._percent = value

    @staticmethod
    def calculate_letter_grade(grade_percentage):
        """
        gets the represented letter grade given a numerical value of the grade.
        :param grade_percentage: float value representing numerical grade
        :return: str of letter grade
        """
        if grade_percentage < 60:
            return "F"
        elif 60 <= grade_percentage < 70:
            return "D"
        elif 70 <= grade_percentage < 80:
            return "C"
        elif 80 <= grade_percentage < 90:
            return "B"
        elif 90 <= grade_percentage:
            return "A"


class Student:
    """
    Student Super Class
    """
    # --- Attributes --- #
    student_name = " "      # string for name
    student_id = 0          # id number
    marks = []              # list of marks of the student

    # ---  Methods  --- #
    def __init__(self, name: str, student_id: int):
        self.student_name = name
        self.student_id = student_id
        self.marks = []

    def add_grade(self, new_mark: Marks):
        """
        adds a new mark/grade to the student profile (marks array attribute)
        :param new_mark: Marks Object
        :return:
        """
        self.marks.append(new_mark)

    def print_grades(self):
        """
        Prints the student grades in a table
        :return: None
        """
        print("Course  |  Letter  |  Percent")
        for mark in self.marks:
            print(f"{mark.course.ljust(6)}  |  {mark.letter_grade.ljust(6)}  |  {mark.percent:.2f}%")


class Undergraduate(Student):
    """
    Undergraduate Student subclass
    """
    # --- Attributes --- #
    sat_score = 0

    # ---  Methods  --- #
    def __init__(self, name: str, student_id: int, sat_score: int):
        super().__init__(name=name, student_id=student_id)
        self.sat_score = sat_score


class Postgraduate(Student):
    """
    Postgraduate Student subclass
    """
    # --- Attributes --- #
    bachelors_gpa = 0

    # ---  Methods  --- #
    def __init__(self, name: str, student_id: int, bachelors_gpa: float):
        super().__init__(name=name, student_id=student_id)
        self.bachelors_gpa = bachelors_gpa


# =========================================================================== #
#                              Execution/Test Code                            #
# =========================================================================== #
if __name__ == '__main__':
    # Create new undergraduate student objects
    StudentX = Undergraduate(name="Calvin Henggeler", student_id=1234567, sat_score=1500)
    print(f"Student {StudentX.student_id}, whose name is {StudentX.student_name},"
          f"scored a {StudentX.sat_score} on the SAT.\n")

    # Add and print Grades
    mark1 = Marks(course="CEC320", percent=91.2)   # These are not real
    mark2 = Marks(course="EE401", percent=75.69)
    mark3 = Marks(course="COM221", percent=40.04)
    StudentX.add_grade(mark1)
    StudentX.add_grade(mark2)
    StudentX.add_grade(mark3)

    StudentX.print_grades()

    # Creating some other classes
    StudentY = Postgraduate("Ed Post", 1010101, 3.95)
    vars(StudentY)

    mark1 = Marks(course="CEC420", percent=randint(1, 100))   # These are not real
    mark2 = Marks(course="EE225", percent=randint(1, 100))
    mark3 = Marks(course="SUSlist_HW", percent=randint(1, 100))
    StudentY.add_grade(mark1)
    StudentY.add_grade(mark2)
    StudentY.add_grade(mark3)

    StudentZ = Student("Matthew Jaffe", 1111111)
    vars(StudentZ)

    mark1 = Marks(course="CEC320", percent=randint(1, 100))   # These are not real
    mark2 = Marks(course="EE-401", percent=randint(1, 100))
    mark3 = Marks(course="COM221", percent=randint(1, 100))
    StudentZ.add_grade(mark1)
    StudentZ.add_grade(mark2)
    StudentZ.add_grade(mark3)

    # testing instances
    print("\nTesting if object are instances of a class")

    print("StudentX")
    print(isinstance(StudentX, Undergraduate))
    print(isinstance(StudentX, Postgraduate))
    print(isinstance(StudentX, Student))
    print("StudentY")
    print(isinstance(StudentY, Undergraduate))
    print(isinstance(StudentY, Postgraduate))
    print(isinstance(StudentY, Student))
    print("StudentZ")
    print(isinstance(StudentZ, Undergraduate))
    print(isinstance(StudentZ, Postgraduate))
    print(isinstance(StudentZ, Student))

    student_roster = [StudentX, StudentY, StudentZ]

    for student in student_roster:
        print(f"\n{student.student_name} ID: {student.student_id}")
        student.print_grades()
