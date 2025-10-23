import re
text = "Name: Nilesh_08, BOB: 05-06-2002, Email: nchavhan544@gmail.com, Phone: 7507487803, Pin: 201545" 
print(re.findall(r'\w+',text))
print(re.findall(r'\d',text))
print(re.findall(r'\D',text))
print(re.findall(r'\s',text))
print(re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b',text))
print(re.findall(r'\b\d{10}\b',text))
print(re.findall(r'\b\d{2}-\d{2}-\d{4}\b',text))
print(re.findall(r'[A-Z][a-z]*b',text))
print(re.findall(r'\b\d{6}\b',text))
print(re.findall(r'\b\w+\d+\b'))