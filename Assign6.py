# # Program to count characters, alphabets, digits, special symbols, and words

# # Taking input from user
# tex = input("Enter text: ")

# # Initializing counters
# total_characters = len(text)
# alphabets = 0
# digits = 0
# special_symbols = 0

# # Counting alphabets, digits and special symbols
# for char in text:
#     if char.isalpha():
#         alphabets += 1
#     elif char.isdigit():
#         digits += 1
#     elif not char.isspace():
#         special_symbols += 1

# # Counting words
# words = len(text.split())

# # Printing results
# print("\n--- Result ---")
# print("Total Characters (including spaces):", total_characters)
# print("Total Alphabets:", alphabets)
# print("Total Digits:", digits)
# print("Total Special Symbols:", special_symbols)
# print("Total Words:", words)

# ##Question 2
# Function to convert string into title case
# def convert_to_title(text):
#     return text.title()

# str = input("Enter a string: ")
# result = convert_to_title(str)
# print("Title Case String:", result)

# #question 3
# # # Function to delete all occurrences of a character from string
# def deleteChar(string, char):
#     new_string = ""
#     for ch in string:
#         if ch != char:
#             new_string += ch
#     return new_string

# str = input("Enter a string: ")
# delete = input("Enter the character to delete: ")
# result = deleteChar(str, delete)
# print("String after deleting character:", result)

#question 4
# # Function to find sum of digits in a string
# def sumOfDigits(string):
#     total = 0
#     for ch in string:
#         if ch.isdigit():
#             total += int(ch)
#     return total

# str = input("Enter a string with some digits: ")
# result = sumOfDigits(str)
# print("Sum of digits in the string:", result)

# #question 5
# Function to replace spaces with hyphens
def replaceWithHyphen(sentence):
    return sentence.replace(" ", "-")

str = input("Enter a sentence: ")
result = replaceWithHyphen(str)
print("Modified sentence:", result)
