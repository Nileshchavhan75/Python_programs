class Employee:
    def salary(self):
        print("Salary not specified")

class Developer(Employee):
    def __init__(self,sal):
        self.di_salary = sal

    def salary(self):
        print("Developer salary is: ",self.di_salary)

class Designer(Employee):
    def __init__(self,sal):
        self.dev_salary = sal

    def  salary(self):
        print("Designer salary is: ",self.dev_salary)

E = Employee()
D = Developer(60000)
d = Designer(50000)

E.salary()
D.salary()
d.salary()