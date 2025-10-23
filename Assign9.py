# def divide_numbers(a, b):
#     try:
#         result = a / b
#         print("Result:", result)
#     except ZeroDivisionError:
#         print("Error: Division by zero is not allowed.")

# # Example usage
# num1 = int(input("Enter numerator: "))
# num2 = int(input("Enter denominator: "))
# divide_numbers(num1, num2)

# def read_file(filename):
#     file = None
#     try:
#         file = open(filename, "r")
#         content = file.read()
#         print("File content:\n", content)
#     except FileNotFoundError:
#         print("Error: File not found.")
#     finally:
#         if file:
#             file.close()
#             print("File has been closed.")

# # Example usage
# filename = input("Enter filename to read: ")
# read_file(filename)

# # Define a user-defined exception
# class UnderAgeError(Exception):
#     pass

# def check_age(age):
#     if age < 18:
#         raise UnderAgeError("You must be at least 18 years old.")
#     else:
#         print("Age is valid. You are allowed.")

# # Main code
# try:
#     age = int(input("Enter your age: "))
#     check_age(age)
# except UnderAgeError as e:
#     print("User-defined Exception:", e)
# except ValueError:
#     print("Please enter a valid number.")
