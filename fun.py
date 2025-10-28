# def Lenth(list):
#     num = len(list)
#     return num

# def Print_list(list):
#     for item in list:
#         print(item, end = " ")
#     return

# list = ["Nilesh","prathmesh","shivay"]
# list2 = [10,20,30,40,50]
# Print_list(list)


# list2 = [10,20,30,40,50]
# Print_list(list)

# def factorial_num(n):
#     fact = 1
#     for item in range(1, n + 1):
#         fact *= item
#     return fact

# fact = factorial_num(5)
# print(fact)

# def convert_inr(n):
#     doler = 85
#     inr = doler *n
#     return inr

# Indien = convert_inr(10)
# print(Indien)

# def checkEvenOdd(n):
#     if(n % 2 == 0):
#         return "Even"
#     else:
#         return "odd"
    
# print(checkEvenOdd(10))

# def fact(n):
#     if(n == 0 or n == 1):
#         return 1
#     else:
#         return n * fact(n - 1)

# print(fact(5))

# def sumOfNumber(n):
#     if(n == 0):
#         return 0
#     else:
#         return n + sumOfNumber(n - 1)

# print(sumOfNumber(10))

# def print_list(list, idx = 0):
#     if(idx == len(list)):
#         return
#     print(list[idx])
#     print_list(list, idx +1)

# list = ["Nilesh", "Falguni", "Sakshi", "Shardha"]
# print_list(list)

# def ff():
#     global m  # Declare 'm' as global
#     m = 10  # Assign value to 'm'
#     print("m value inside function:", m)

# ff()  # Call the function

# print("m value outside function:", m)  # Access global 'm'

# local variable

# def funct():
#     z=10
#     print("local variable value",z)

# funct()


# def printing(n):
#     if n > 0:
#         printing(n - 1)  # First recursive call (prints in increasing order)
#         print(n)         # Print after recursive call (ensures order)
#     else:
#         return

# printing(5)

