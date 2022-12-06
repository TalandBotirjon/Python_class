from abc import ABC, abstractmethod


class Payer(ABC):

    @abstractmethod
    def pay(self):
        pass


class Member(ABC):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def save_database(self):
        pass


class Teacher(Member, Payer):

    def __init__(self, name, age, teacher_id):
        super(Teacher, self).__init__(name, age)
        self.teacher_id = teacher_id

    def save_database(self):
        return f"Save Teacher data a database."

    def pay(self):
        return f"Teacher paying."


class Manager(Member, Payer):

    def __init__(self, name, age, manager_id):
        super(Manager, self).__init__(name, age)
        self.manager_id = manager_id

    def save_database(self):
        return f"Save manager data a database."

    def pay(self):
        return f"Manager paying."


class Student(Member):
    def __init__(self, name, age, student_id):
        super(Student, self).__init__(name, age)
        self.student_id = student_id

    def save_database(self):
        return f"Save student data a database."


payers: list[Payer] = [Teacher('John', 24, '123'), Manager('Mary', 32, '321')]
for payer in payers:
    print(payer.pay())

