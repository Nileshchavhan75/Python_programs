
# def area(l, w):
#     return l * w

# length = float(input("Enter the length: "))
# width = float(input("Enter width: "))
# print("Area of RectAngle: ",area(length,width))

# #question 2
# Lambda function to add two numbers
# add = lambda x, y: x + y

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# result = add(num1, num2)
# print("Sum:", result)

#question3
# def reverseString(st):
#     return st[::-1]

# str = input("Enter a string: ")
# print("Reverse: ",reverseString(str))

#question4
# def factorial(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     return fact

# num = int(input("Enter the Number: "))
# print("Factorial of Number: ", factorial(num))

#question5
# import Arithmatic
# num = int(input("Enter the number: "))
# print("Square of number: ",Arithmatic.square(num))

#question 6
# def calling(a,b):
#     def multiplication(a,b):
#         return a * b
#     print("Multiplication: ",multiplication(a,b))

# number1 = int(input("Enter number: "))
# number2 = int(input("Enter second: "))

# calling(number1,number2)

#question 7
# def checkPolindrome(st):
#     return st[::-1]

# str = input("Enter String: ")
# check = checkPolindrome(str)

# if(check == str):
#     print(f"{str} is polindrome")
# else:
#     print(f"{str} is not polindrome")

#question 8
# def count_case(text):
#     upper = 0
#     lower = 0

#     for char in text:
#         if char.isupper():
#             upper += 1
#         elif char.islower():
#             lower += 1

#     print("Uppercase Letters:", upper)
#     print("Lowercase Letters:", lower)

# string = input("Enter a string: ")
# count_case(string)

# #question 9
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Get number of terms from user
terms = int(input("Enter number of terms: "))

print("Fibonacci Series:")
for i in range(terms):
    print(fibonacci(i), end=" ")

#question 10
# Getting command-line arguments directly (excluding the script name)
args = input("Enter numbers separated by space: ").split()
numbers = [int(num) for num in args]
result = sum(numbers)
print("Result:", result)
