# Marcello Novak
# 2/23/2021
# This program is a demonstration of OOP in Python
# This program was created with github copilot

# Create student parent class
class Student:
    def __init__(self, name: str, student_id: int, student_name: str, marks: int,):
        self.name = name
        self.student_id = student_id
        self.student_name = student_name
        self.marks = marks

# I legitimately don't know what this is supposed to do
# We already have an attribute for marks within student
# So I'm not sure what to put here
class Marks:
    def __init(self, marks: int):
        self.marks = marks

# Undergraduate extends Student
class Undergraduate(Student):
    # Inherited Attributes from Student
    def __init__(self, name: str, student_id: int, student_name: str, marks: int,
                 # Unique Attributes for Undergraduate
                 sat_score: int):

        # Initialize the inherited attributes
        Student.__init__(self, name, student_id, student_name, marks)
        # Initialize the unique attributes
        self.sat_score = sat_score

# Postgraduate extends Student
class Postgraduate(Student):
    # Inherited Attributes from Student
    def __init__(self, name: str, student_id: int, student_name: str, marks: int,
                 # Unique Attributes for Postgraduate
                 bachelors_gpa: float):

        # Initialize the inherited attributes
        Student.__init__(self, name, student_id, student_name, marks)
        # Initialize the unique attributes
        self.bachelors_gpa = bachelors_gpa


student1 = Undergraduate("Mark", 2690173, "Mark Smith", 3.0, 1000)
student2 = Postgraduate("John", 2690174, "John Smith", 3.0, 3.4)
student3 = Undergraduate("Jane", 2690175, "Jane Smith", 1.2, 1500)
student4 = Postgraduate("Mary", 2690176, "Mary Smith", 3.3, 2.6)

students = [student1, student2, student3, student4]
for student in students:
    print(student.name, student.marks)

# I'm also not sure how to test_SUSlist_HW this program, but I iterated over
# the list and provided the output described in canvas? Idk. Sorry.