# A = [
#     [10,20],
#     [21,22]
# ]
# B = [
#     [11,12],
#     [31,32]
# ]
# Add = [
#     [0,0],
#     [0,0]
# ]
# for i in range(len(A)):
#     for j in range(len(B[0])):
#         Add[i][j] = A[i][j] + B[i][j]

# print("Addition of two matrices")
# for row in Add:
#     print(row)



# # question No: 2
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# # Transpose using list comprehension
# transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

# # Print transposed matrix
# print("Transpose of the matrix is:")
# for row in transpose:
#     print(row)

# Question No: 3

# li = [10,11,12,13,14,15,16,17,18,20]

# Addition = 0
# for i in li:
#     if i % 2 == 0:
#         Addition += i

# print("Addition of even number in list: ",Addition)

# #question No:4

# li = [10,20,30,40]
# li2 = [21,22,23,24]

# concat = li+li2
# print(concat)

##question No: 5
# li = [10,11,12,10,15,10,20]
# print("10 found: ",li.count(10))

#question No:6
# A = {1,2,3,4}
# B = {3,4,5,6}

# print("Commen Element: ",A.intersection(B))

# #Question No:7
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}

# # Unique in set1: elements in set1 but not in set2
# unique_in_set1 = set1 - set2

# # Unique in set2: elements in set2 but not in set1
# unique_in_set2 = set2 - set1

# # OR: All unique elements in both sets (excluding common ones)
# unique_in_both = set1 ^ set2  # symmetric difference

# print("Unique in set1:", unique_in_set1)
# print("Unique in set2:", unique_in_set2)
# print("Unique in both sets (not common):", unique_in_both)
 
# #Question No: 8
# tup = (10,20,30,40,50,60)

# ele = int(input("Enter Element: "))

# if ele in tup:
#     print(f"{ele} exit in the tuple")
# else:
#     print(f"{ele} doesn't exit the tuple")

##question No: 9
# List with duplicates
# my_list = [1, 2, 3, 2, 4, 5, 1, 6, 3]

# # Convert list to set to remove duplicates
# my_set = set(my_list)

# # Print results
# print("Original List:", my_list)
# print("Set (duplicates removed):", my_set)

# # #question No: 10
# tup = (1,2,3,4,5,6)
# list =list(tup)
# list.append(44)
# b = [5,3,6]

# final = list + b
# print(final)

##question No: 11
# dic = {
#     'A': [80, 90],
#     'B': [85, 95]
# }

# # Find the key (student) with the maximum average
# max_avg = max(dic.keys(), key=lambda x: sum(dic[x]) / len(dic[x]))

# print("Top student:", max_avg)

##question 12

# str = ["shiv","shivay","ganesh","arjun"]

# lenght = []

# for li in str:
#     if len(li) % 2 == 0:
#         lenght.append(len(li))

# print(lenght)

##uquestion13
# original = {'a': 1, 'b': 2, 'c': 3}

# # Dictionary comprehension
# copy_dict = {key: value for key, value in original.items()}

# print("Copied Dictionary:", copy_dict)

#Question 14
# people = [
#     {'name': 'Alice', 'age': 30, 'salary': 40000},
#     {'name': 'Bob', 'age': 25, 'salary': 60000},
#     {'name': 'Charlie', 'age': 22, 'salary': 45000},
#     {'name': 'David', 'age': 35, 'salary': 30000}
# ]

# Filter people with salary < 50000 and sort by age
# filtered_sorted = sorted(
#     [person for person in people if person['salary'] < 50000],
#     key=lambda x: x['age']
# )

# # Output result
# for person in filtered_sorted:
#     print(person)


##question
def print_squares(coords):
    x, y, z = coords
    print(f"Squares: X²={x**2}, Y²={y**2}, Z²={z**2}")

# Example usage
print_squares((2, 3, 4))


