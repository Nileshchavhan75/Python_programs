# result = None
# try:
#     num = int(input("Enter number: "))
#     num2 = int(input("Enter second number: "))
#     result = num/num2
# except ZeroDivisionError:
#     print("Can not divide by zero")

# except ValueError:
#     print("Enter valide number")

# except Exception as e:
#     print("Exception: ",e)

# finally:
#     if result is not None:
#         print("Result: ",result)

class UnderAgeError(Exception):
    pass
def check_Age(age):
    if age < 18:
        raise UnderAgeError("you are not eligible")
    else:
        print("You are Eligible")

try:
    age = int(input("Enter your age: "))
    check_Age(age)
except UnderAgeError as e:
    print("Exception: ",e)
except ValueError:
    print("Please Enter valide number")



# class NegativeNumberError(Exception):
#     pass
# def check_number(n):
#     if n < 0:
#         raise NegativeNumberError("Negative numbers are not allowed")
#     else:
#         print("valid Number")
    
# try:
#     num = int(input("Enter number: "))
#     check_number(num)
# except NegativeNumberError as e:
#     print("Error: ",e)
# except ValueError:
#     print("please enter valide number")

class InvalidPasswordError(Exception):
    pass
def check_password(password):
    if len(password) < 6:
        raise InvalidPasswordError("Password must be 6 characters")
    else:
        print("Password Accepted")

try:
    pas = input("Enter password: ")
    check_password(pas)
except InvalidPasswordError as e:
    print("Error: ",e)
except Exception as e:
    print("Exception",e)
