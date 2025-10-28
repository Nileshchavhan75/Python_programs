class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    
    def info(self):
        print("Name: ",self.name)
        print("Age: ",self.age)

class Student(Person):
    def __init__(self, name, age, school, grade):
        super().__init__(name,age)
        self.school = school
        self.grade = grade
    
    def studentInfo(self):
        print("School: ",self.school)
        print("Grade: ",self.grade)

s1 = Student("Rutuja", 21, "marathi","A")
s1.info()
s1.studentInfo()
