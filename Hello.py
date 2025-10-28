# n = int(input("Enter number: "))

# for i in range(n):  # Outer loop for rows
#     for j in range(n):  # Inner loop for columns
#         print("*", end='')  # Print '*' without a newline
#     print()  # Move to the next line after each row
n = int(input("Enter number: "))

for i in range(1, n + 1):  # Outer loop for rows
    print(" " * (n - i), end='')  # Printing spaces
    print("* " * i)  # Printing stars
