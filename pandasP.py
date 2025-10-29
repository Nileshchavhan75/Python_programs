# import pandas as pd

# # Creating a DataFrame
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Age': [24, 27, 22]
# }
# df = pd.DataFrame(data)

# print(df)

# # Accessing a column
# print("Names column:\n", df['Name'])

# # Descriptive statistics
# print("Average age:", df['Age'].mean())


# import pandas as pd
# data = {
#     'Name': ['Nilesh','Shubham','prathmesh','sakshi','Rutuja'],
#     'subject':['English','python','java','iks','math'],
#     'score':[88,76,95,35,85]
# }

# pf = pd.DataFrame(data)
# print(pf)

# print("marks",pf[pf['score'] > 90])

import pandas as pd 
data = [10,20,30,40,50,60]
s = pd.Series(data)
print(s)
