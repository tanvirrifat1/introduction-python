# class Phone:
#     price = 5054654
#     color = "black"
#     brand = "samsung"

#     features = ["camera", "fingerprint", "face unlock", "fast charging"]

#     def call(self):
#         print("Calling...")

#     def send_message(self, phone, sms):
#         text = f"sending sms to : {phone} with message : {sms}"
#         return text


# my_phone = Phone()
# res = my_phone.send_message(123456789, "hello")
# print(res)


class Student:
    def __init__(self, name, current_class, id):
        self.name = name
        self.current_class = current_class
        self.id = id

    def __repr__(self):
        return (
            f"student name : {self.name}, class : {self.current_class}, id : {self.id}"
        )


class Teacher:
    def __init__(self, name, subject, id):
        self.name = name
        self.subject = subject
        self.id = id

    def __repr__(self):
        return f"teacher name : {self.name}, subject : {self.subject}, id : {self.id}"


class School:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []

    def add_teacher(self, name, subject):
        id = len(self.teachers) + 101
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)

    def add_student(self, name, fee):
        if fee < 6500:
            return "not enough fee"
        else:
            id = len(self.students) + 1
            student = Student(name, "class 1", id)
            self.students.append(student)
            return f"student {name}added successfully with id {id}, extra monry : {fee - 6500}"

    def __repr__(self):
        result = f"Welcome to school {self.name}\n"
        result += "Teachers:\n"
        for teacher in self.teachers:
            result += str(teacher) + "\n"
        result += "Students:\n"
        for student in self.students:
            result += str(student) + "\n"
        return result


phitron = School("web development school")

phitron.add_student("rifat", 7000)
phitron.add_student("sifat", 15000)

phitron.add_teacher("dfs", "python")
phitron.add_teacher("siffgsdfgat", "javascript")


print(phitron)
