# Write a program that asks the user to input a number and divides 100 by that number.
# Handle the case when the user enters zero or something that’s not a number.

# try:
#     num = int(input("Enter a number: "))
#     result = 100 / num
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
#     result = None
# except ValueError:
#     print("Please enter a valid number.")
#     result = None
# except Exception as e:
#     print("An unexpected error occurred:", e)
#     result = None
# finally:
#     if result is not None:
#         print("Result:", result)

# try:
#     num = int(input("Enter number to print square: "))
#     result = num * num
# except ValueError:
#     print("Invalid input. Please enter a number")
#     result = None
# except Exception as e:
#     print("Exception: ",e)
#     result = None
# finally:
#     if result is not None:
#         print("Result: ",result)

# try:
#     num = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     result = num/num2
# except ValueError:
#     print("Invalid input.Please enter a number")
#     result = None
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
#     result = None
# finally:
#     if result is not None:
#         print("Result: ",result)

try:
    password = input("Enter password: ")
    if len(password) < 6:
        raise ValueError("Password too short. Must be at least 6 characters.")
    print("Password accepted")
except ValueError as e:
    print("Exception:", e)

# try:
#     age = int(input("Enter your age: "))
#     if age < 18:
#         raise ValueError("You must be at least 18 years old to register.")
#     print("Registration successful")
# except ValueError as e:
#     print("Exception: ",e)
    
# try:
#     num1 = int(input("Enter first num: "))
#     num2 = int(input("Enter second number: "))
#     result = num1/num2
#     print("Result: ",result)
# except ZeroDivisionError:
#     print("Can not divide with zero")
# except ValueError:
#     print("Please Enter valid number")
# finally:
#     print("Operation Completed")