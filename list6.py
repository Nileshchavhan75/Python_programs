list = [12, 34, 56, 78]
sum_digits_list = []

for num in list:
    sum_digits = 0
    for digit in str(num): 
        sum_digits += int(digit)
    sum_digits_list.append(sum_digits)

print("Sum of digits in list:", sum_digits_list)
