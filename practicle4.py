a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Numbers before swapping -> A:", a, "B:", b)

# Swapping without temp variable
a, b = b, a  

print("Numbers after swapping -> A:", a, "B:", b)
