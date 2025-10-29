class Student:
    def __init__(self,name, math, english, science):
        self.name = name
        self.math = math
        self.english = english
        self.science = science

    def info(self):
        print("Marks of -",self.name)
        print("Math: ",self.math)
        print("English: ",self.english)
        print("Science: ",self.science)
    
    def ave(self):
        print("Average: ",(self.math+self.english+self.science)/ 3)

s1 = Student("Nilesh", 65,75,85)
s1.info()
s1.ave()