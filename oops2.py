class Student:
    def __init__(self, name, math, english, marathi):
        self.name = name
        self.math = math
        self.english = english
        self.marathi = marathi

    def info(self):
        print("Name: ",self.name)
        print("Math: ",self.math)
        print("English: ",self.english)
        print("Marathi: ",self.marathi)
        print((self.math + self.english + self.marathi) / 3)

s1 = Student("Rutuja",95,65,85)
s1.info()
        