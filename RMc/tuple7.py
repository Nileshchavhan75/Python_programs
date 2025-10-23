tuple = (10,20,30,40,50,60)
x = 50
i = 0
for ie in tuple:
    if(ie == x):
        print("Element found at index:", i)
        break
    i = i + 1
else:
        print("Not found")

