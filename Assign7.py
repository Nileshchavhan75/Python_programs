# class Person:
#     def setData(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address


#     def printDetails(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Address:", self.address)

# p1 = Person()
# p1.setData("shivay", 25, "Jalgoan")
# p1.printDetails()

#question 2
# Creating a class Car
# class Car:
#     wheels = 4

#     def __init__(self, brand, color):
#         self.brand = brand   
#         self.color = color   

#     def show(self):
#         print("Brand:", self.brand)
#         print("Color:", self.color)
#         print("Wheels:", Car.wheels)

# car1 = Car("Toyota", "Red")
# car1.show()

#question 3
# # Multilevel Inheritance
# class Grandparent:
#     def show_grandparent(self):
#         print("I am the Grandparent.")

# class Parent(Grandparent):
#     def show_parent(self):
#         print("I am the Parent.")

# class Child(Parent):
#     def show_child(self):
#         print("I am the Child.")

# # Create object of Child
# c = Child()
# c.show_grandparent()
# c.show_parent()
# c.show_child()

# #question 4
# class Student:
#     def __init__(self):
#         self.admno = 0
#         self.name = ""
#         self.english = 0.0
#         self.science = 0.0
#         self.maths = 0.0
#         self.total = 0.0

#     def take_data(self):
#         self.admno = int(input("Enter Admission Number: "))
#         self.name = input("Enter Name: ")
#         self.english = float(input("Enter English Marks: "))
#         self.science = float(input("Enter Science Marks: "))
#         self.maths = float(input("Enter Maths Marks: "))

#     def calculate_total(self) -> float:
#         self.total = self.english + self.science + self.maths
#         return self.total

#     def show_data(self):
#         print("\n--- Student Information ---")
#         print(f"Admission No: {self.admno}")
#         print(f"Name: {self.name}")
#         print(f"English: {self.english}")
#         print(f"Science: {self.science}")
#         print(f"Maths: {self.maths}")
#         print(f"Total Marks: {self.total}")

# # Main Program
# s1 = Student()
# s1.take_data()
# s1.calculate_total()
# s1.show_data()

# # question 5
# class Batsman:
#     def __init__(self):
#         self.bcode = ""
#         self.bname = ""
#         self.innings = 0
#         self.notout = 0
#         self.runs = 0
#         self.batAverage = 0.0

#     def read_data(self):
#         self.bcode = input("Enter Batsman Code: ")
#         self.bname = input("Enter Batsman Name: ")
#         self.innings = int(input("Enter number of Innings: "))
#         self.notout = int(input("Enter number of Not Outs: "))
#         self.runs = int(input("Enter total Runs: "))

#     def cal_average(self):
#         if self.innings - self.notout != 0:
#             self.batAverage = self.runs / (self.innings - self.notout)
#         else:
#             self.batAverage = 0.0  # Avoid division by zero

#     def display_data(self):
#         print("\n--- Batsman Details ---")
#         print("Code:", self.bcode)
#         print("Name:", self.bname)
#         print("Innings:", self.innings)
#         print("Not Outs:", self.notout)
#         print("Runs:", self.runs)
#         print("Batting Average:", round(self.batAverage, 2))


# # Driver code
# b = Batsman()
# b.read_data()
# b.cal_average()
# b.display_data()

#question 6
# class Test:
#     def __init__(self):
#         self.TestCode = 0
#         self.Description = ""
#         self.NoCandidate = 0
#         self.CenterReqd = 0

#     def CALCNTR(self):
#         # Calculate number of centers required
#         self.CenterReqd = (self.NoCandidate // 100) + 1

#     def SCHEDULE(self):
#         self.TestCode = int(input("Enter Test Code: "))
#         self.Description = input("Enter Description: ")
#         self.NoCandidate = int(input("Enter Number of Candidates: "))
#         self.CALCNTR()  # Call to calculate center required

#     def DISPTEST(self):
#         print("\n--- Test Details ---")
#         print("Test Code:", self.TestCode)
#         print("Description:", self.Description)
#         print("Number of Candidates:", self.NoCandidate)
#         print("Centers Required:", self.CenterReqd)


# # Driver code
# t = Test()
# t.SCHEDULE()
# t.DISPTEST()

#question 7
# class Flight:
#     def __init__(self):
#         self.flight_no = 0
#         self.destination = ""
#         self.distance = 0.0
#         self.fuel = 0.0

#     def CALFUEL(self):
#         if self.distance <= 1000:
#             self.fuel = 500
#         elif self.distance <= 2000:
#             self.fuel = 1100
#         else:
#             self.fuel = 2200

#     def fuelinfo(self):
#         self.flight_no = int(input("Enter Flight Number: "))
#         self.destination = input("Enter Destination: ")
#         self.distance = float(input("Enter Distance: "))
#         self.CALFUEL()

#     def showinfo(self):
#         print("\n--- Flight Information ---")
#         print("Flight Number:", self.flight_no)
#         print("Destination:", self.destination)
#         print("Distance:", self.distance)
#         print("Fuel Required:", self.fuel)


# # Driver code
# f = Flight()
# f.fuelinfo()
# f.showinfo()

# #question 8
# class Book:
#     def __init__(self):
#         self.book_no = 0
#         self.book_title = ""
#         self.price = 0.0

#     def input(self):
#         self.book_no = int(input("Enter Book Number: "))
#         self.book_title = input("Enter Book Title: ")
#         self.price = float(input("Enter Price per Copy: "))

#     def total_cost(self, n):
#         return self.price * n

#     def purchase(self):
#         n = int(input("Enter number of copies to purchase: "))
#         total = self.total_cost(n)
#         print(f"Total cost for {n} copies: ₹{total:.2f}")


# # Driver Code
# b = Book()
# b.input()
# b.purchase()


# #question 9
# class Report:
#     def __init__(self):
#         self.ad_no = 0
#         self.name = ""
#         self.marks = []

#     def getAvg(self):
#         self.ad_no = int(input("Enter 4-digit Admission Number: "))
#         self.name = input("Enter Name: ")

#         print("Enter marks for 5 subjects:")
#         self.marks = [float(input(f"Subject {i+1}: ")) for i in range(5)]

#     def displayInfo(self):
#         average = sum(self.marks) / len(self.marks)
#         print("\n----- Student Report -----")
#         print(f"Admission No: {self.ad_no}")
#         print(f"Name: {self.name}")
#         print(f"Marks: {self.marks}")
#         print(f"Average Marks: {average:.2f}")


# # Driver Code
# r = Report()
# r.getAvg()
# r.displayInfo()

