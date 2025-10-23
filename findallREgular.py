# import re

# text = "Summer is sunny and sweet"
# patter = r'\b[Ss]\w*'
# check = re.findall(patter,text)
# print(check)

import re

text = "Big brown bears are bold"
patter = r'\b[Bb]\w*'
check = re.findall(patter, text)
print(check)
