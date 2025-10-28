list = [10, 5, 20, 8, 2, 15]
largest = list[0] 
for num in list:
    if num > largest:
        largest = num

print("Largest number in the list:", largest)
