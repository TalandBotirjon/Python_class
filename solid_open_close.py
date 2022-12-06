from abc import ABC, abstractmethod


class Employee(ABC):

    def __int__(self, name: str, salary:str):
        self.name = name
        self.salary = salary

    @abstractmethod
    def work(self):
        pass


class Tester(Employee):

    def __int__(self, name:str, salary: str):
        super(Tester, self).__int__(name, salary)

    def test(self):
        return f"{self.name} is testing."

    def work(self):
        self.test()


class Developer(Employee):

    def __init__(self, name: str, salary: str):
        super(Developer, self).__init__(name, salary)

    def develop(self):
        return f"{self.name} is developer."

    def work(self):
        self.develop()


class Company:

    def __init__(self, name: str):
        self.name = name

    def work(self, employee: Employee):
        employee.work()




