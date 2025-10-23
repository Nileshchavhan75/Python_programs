Num = int(input("Enter Number: "))
Num2 = int(input("Enter Second Number: "))
Num3 = int(input("Enter third Number: "))

if(Num >= Num2 and Num >= Num3):
    print(f"{Num} is Greater than all three Number")
elif(Num2 >= Num3):
    print(f"{Num2} is Greater than all three Number" )
else:
    print(f"{Num3} is Greater than all three number")