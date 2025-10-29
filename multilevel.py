# class Animal:
#     def __init__(self,name):
#         self.name = name
    
#     def speak(self):
#         print("Name: ",self.name)
# class Lion(Animal):
#     def __init__(self,name,breed):
#         super().__init__(name)
#         self.breed = breed

#     def showBreed(self):
#         print("Breed: ",self.breed)

# class WildAni(Lion):
#     def __init__(self,name,breed,owner):
#         super().__init__(name,breed)
#         self.owner = owner
    
#     def showAnimal(self):
#         print("Owner: ",self.owner)
    
# A = WildAni("scarface","Wild Animal","Nilesh")
# A.speak()
# A.showBreed()
# A.showAnimal()

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def show_person(self):
        print("Name: ",self.name)
        print("Age: ",self.age)

class Student(Person):
    def __init__(self, name, age,stud_id):
        super().__init__(name,age)
        self.stud_id = stud_id

    def show_student(self):
        print("Student ID: ",self.stud_id)

class CollegeStudent(Student):
    def __init__(self, name, age, stud_id, collegeName):
        super().__init__(name, age, stud_id)
        self.collegeName = collegeName
    
    def show_college(self):
        print("College: ",self.collegeName)

c = CollegeStudent("Nilesh",22,12,"JSMP")
c.show_person()
c.show_student()
c.show_college()

        
        