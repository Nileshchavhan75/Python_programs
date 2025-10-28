my_list = [10, 5, 20, 8, 2, 15]

largest = 0
second_largest = -1

for num in my_list:
    if num > largest:  
        second_largest = largest  
        largest = num  
    elif num > second_largest and num != largest:  
        second_largest = num 
        
if second_largest == float('-inf'):
    print("No second largest number found")
else:
    print("Second largest number in the list:", second_largest)
