# #question 1
# import re

# def pattern_search():
#     text = input("Enter a string: ")
#     pattern = input("Enter the pattern to search: ")

#     match = re.search(pattern, text)

#     if match:
#         print(f"Pattern found at position {match.start()} to {match.end()}")
#     else:
#         print("Pattern not found.")

# # Call the function
# pattern_search()

# # #question 2
# import re

# def pattern_match_start():
#     text = input("Enter a string: ")
#     pattern = input("Enter the pattern to match: ")

#     match = re.match(pattern, text)

#     if match:
#         print(f"Pattern found at the start: '{match.group()}'")
#     else:
#         print("No match at the beginning of the string.")

# # Call the function
# pattern_match_start()

# #question 3
# import re

# text = "Hello123, this is a demo text with email test@example.com, phone 123-456-7890, price $99.99, date 28-04-2025, pin 560001, site https://site.com, code A1B2C3, words like apple, Banana, cat."

# # 10 patterns to search
# patterns = [
#     r"\d+",               # 1. All numbers
#     r"[a-z]+",            # 2. All lowercase words
#     r"[A-Z][a-z]+",       # 3. Capitalized words
#     r"\w+",               # 4. All words (alphanumeric)
#     r"\s",                # 5. All whitespace characters
#     r"\d{2}-\d{2}-\d{4}", # 6. Date format dd-mm-yyyy
#     r"\$\d+\.\d{2}",      # 7. Price like $99.99
#     r"\w+@\w+\.\w+",      # 8. Email address
#     r"https?://\S+",      # 9. URL
#     r"\d{3}-\d{3}-\d{4}", # 10. Phone number
# ]

# # Search and display results
# for i, pattern in enumerate(patterns, start=1):
#     result = re.findall(pattern, text)
#     print(f"{i}. Pattern: {pattern} → {result}")

# #question 4
import re

text = "Python is great. I love learning Python. Python is easy."

# Replace 'Python' with 'Java'
new_text = re.sub('Python', 'Java', text)

print("Original Text:", text)
print("Modified Text:", new_text)


# # #question 5
# import re

# text = "Here are some emails: test@example.com, hello123@gmail.com, contact@my-site.org, wrong@format, user@domain.co.in"

# # Pattern to match email addresses
# pattern = r'\b[\w.-]+@[\w.-]+\.\w+\b'

# # Find all email addresses
# emails = re.findall(pattern, text)

# print("Email addresses found:")
# for email in emails:  
#     print(email)
