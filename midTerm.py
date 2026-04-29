class Student:
    def __init__(self, student_id, name, department, is_enrolled):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.is_enrolled = is_enrolled


class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)


student1 = Student(1, "Rifat Miah", "CSE", True)
student2 = Student(2, "Rahim Uddin", "EEE", True)
student3 = Student(3, "Karim Khan", "BBA", False)


StudentDatabase.add_student(student1)
StudentDatabase.add_student(student2)
StudentDatabase.add_student(student3)


for student in StudentDatabase.student_list:
    print(f"Student Id: {student.student_id}")
    print(f"Name: {student.name}")
    print(f"Department: {student.department}")
    print(f"Enrolled: {student.is_enrolled}")


for student in StudentDatabase.student_list:
    print(student.student_id, student.name, student.department, student.is_enrolled)
