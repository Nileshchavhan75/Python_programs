from packegeEx import series

num = int(input("Enter the number for factorial:: "))
print(f"Factorial of: ",series.factorial(num))

num = int(input("Enter the number for fibonacci series:: "))
print("fibonacci series: ",series.fibonacci(num))
   
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
print("Expontial series: ",series.exponential_series(x,y))
