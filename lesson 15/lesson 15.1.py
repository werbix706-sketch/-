class GroupFullError(Exception):
    pass

class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupFullError('Група вже заповнена')
        self.group.add(student)

class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

gr = Group('PD1')
st1 = Student('Lena', 'Mitrova')
gr.add_student(st1)
try:
    for i in range(10):
        student = Student('Student', f'Student{i + 1}')
        gr.add_student(student)

except GroupFullError as e:
    print(e)