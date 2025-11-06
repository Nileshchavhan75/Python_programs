# num = int(input("Enter number: "))

# count = 0
# i = 1
# while(i <=num):
#     if(num % i == 0):
#         count = count + 1
#     i = i + 1

# if(count == 2):
#     print("is prime number")
# else:
#     print("is not prime number")

num = int(input("Enter Number: "))

x = 0
y = 1
z = 0
while(z <= num):
    print(z, end=" ")
    x = y
    y = z 
    z = x + y
