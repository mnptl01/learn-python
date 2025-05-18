class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        print(f"Role is {self.role} in {self.department} department, and salary is $ {self.salary}")

class Engineer(Employee):
    def __init__(self, name, age):
         self.name = name
         self.age = age
         super().__init__("engineer","it", 50000)


e1 = Employee("salesman", "eng", 2000)
e1.showDetails()

e2 = Engineer("sahil", 29)
e2.showDetails()