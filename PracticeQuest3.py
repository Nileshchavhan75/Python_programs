num = int(input("Enter Number: "))
if(num % 5 == 0 and num % 11 == 0):
    print(f"{num} is multiple of 5 and 11")
else:
    print(f"{num} is not multiple of 5 and 11")