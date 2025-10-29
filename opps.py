# class Car:
#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price

#     def Info(self):
#         print(f"Brand: {self.brand}")
#         print(f"Price: {self.price}")


# c1 = Car("audi", 125.5)
# c1.Info()
    

# class Employee:
#     def __init__(self,name,id,salary):
#         self.name = name
#         self.id = id
#         self.salary = salary

#     def info(self):
#         print("Name: ",self.name)
#         print("id: ",self.id)
#         print("salary: ",self.salary)


# e1 = Employee("Rutuja", 14, 25000)
# e1.info()

# class Car:
#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price
    
#     def display(self):
#         print("Brand: ",self.brand)
#         print("price: ",self.price)
    
# c1 = Car("TATA", 250000)
# c1.display()

# class Book:
#     def __init__(self, title,author,price):
#         self.title = title
#         self.author = author
#         self.price = price
    
#     def info(self):
#         print("Title: ",self.title)
#         print("author: ",self.author)
#         print("price: ",self.price)

# b = Book("Rich dad poor dad","Robert",850)
# b.info()

# class Pen:
#     def __init__(self,color,brand):
#         self.color = color
#         self.brand = brand

#     def show_details(self):
#         print("color: ",self.color)
#         print("brand: ",self.brand)

# p = Pen("blue","parker")
# p2 = Pen("Black","Cello")
# p.show_details()
# print("------------")
# p2.show_details()

class Student:
    def __init__(self, name, marks):
        self.name =name
        self.__marks = marks

    def getMarks(self):
        return self.__marks
    
    def setMarks(self,marks):
        if marks > 0 and marks < 100:
            self.__marks = marks
        else:
            print("No marks obtained")
        
    def show(self):
        print("Name: ",self.name)
        print("Marks: ",self.__marks)
    
s = Student("Nilesh", 78)
print("getting marks: ",s.getMarks())
s.show()
s.setMarks(90)
s.show()