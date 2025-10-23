# file = open("demo.txt","w")
# file.write("Welcome to the Python")
# file.close()

# file = open("demo.txt","r")
# data = file.read()
# print(data)
# file.close()

##question No: 2
# file = open("demo.txt","a")
# file.write("\nthis is new data")
# file.close()

# file = open("demo.txt", "r")

# for line in file:
#     print(line.strip())  # .strip() removes extra \n

# file.close()

#quesrion no:1
# Open original file in read mode
# with open("demo.txt", "r") as file:
#     content = file.read()

# # Reverse the content
# reversed_content = content[::-1]

# # Write reversed content to new file
# with open("reversed.txt", "w") as new_file:
#     new_file.write(reversed_content)

# print("Reversed content written to 'reversed.txt'")

##question 3
# import pickle

# data = {"name": "Shiv", "age": 21, "marks": [80, 85, 90]}

# # Open file in write-binary mode
# with open("student.pkl", "wb") as file:
#     pickle.dump(data, file)

# print("Data written to file using pickle.")

#question 4
# This program reads content from "demo.txt" using the with clause

# with open("demo.txt", "r") as file: 
#     content = file.read()
#     print("File Content:\n", content)

#question 5
# Accept input from user
user_input = input("Enter a string: ")

# Write the input to a file
with open("user_text.txt", "w") as file:
    file.write(user_input)

# Read the content from the file
with open("user_text.txt", "r") as file:
    content = file.read()
    print("\nContent from file:")
    print(content)