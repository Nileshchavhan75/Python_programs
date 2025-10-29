# class Father:
#     def __init__(self,fname,fage):
#         self.fname = fname
#         self.fage = fage

#     def displayFatherInfo(self):
#         print("Name",self.fname)
#         print("Age",self.fage)

# class Mather:
#     def __init__(self,name,hobby):
#         self.name = name
#         self.hobby = hobby
    
#     def displayMotherInfo(self):
#         print("Name: ",self.name)
#         print("Hobby",self.hobby)
    
# class Child(Father,Mather):
#     def __init__(self,fname,fage,name,hobby,school):
#         Father.__init__(self, fname,fage)
#         Mather.__init__(self, name,hobby)
#         self.school = school

#     def displayChild(self):
#         print("School",self.school)

# c1 = Child("Abc",30,"Mnc","cooking","mj")
# c1.displayFatherInfo()
# c1.displayMotherInfo()
# c1.displayChild()


class Father:
    def __init__(self,fname):
        self.fname = fname
    
    def show_father(self):
        print("Father Name: ",self.fname)

class Mother:
    def __init__(self,mname):
        self.mname = mname
    
    def show_mother(self):
        print("Mathor Name: ",self.mname)

class Child(Father,Mother):
    def __init__(self, fname, mname,child_name):
        Father.__init__(self, fname)
        Mother.__init__(self,mname)
        self.child_name = child_name

    def child(self):
        print("Child Name: ",self.child_name)
    
c = Child("Abhishek","Ashvariya","Arjun")
c.show_father()
c.show_mother()
c.child()
        
        