list = [10, 5, 20, 8, 2, 15]

smallest = list[0]  

for num in list:
    if num < smallest:  
        smallest = num
print("Smallest number in the list:", smallest)
