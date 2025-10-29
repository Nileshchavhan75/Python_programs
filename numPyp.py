# import numpy as np
# arr = np.array([1,2,3,4,5,6,7])
# print(arr)
# print(arr[0])
# print(arr[2])
# print(arr[-1])

# print("sum: ",np.sum(arr))
# print("Mean: ",np.mean(arr))
# print("Max: ",np.max(arr))
# print("Min: ",np.min(arr))

# import numpy as np 

# matrix = np.array([[1,2],[3,4],[5,6]])
# print("Original matrix: \n",matrix)
# print("Transposed matrix: \n",matrix.T)

# import numpy as np

# # Creating a 2D array
# arr2d = np.array([[1, 2], [3, 4]])
# print("2D Array:\n", arr2d)

# # Transpose of the array
# print("Transpose:\n", np.transpose(arr2d))

# # Multiply all values by 2
# print("Multiplied by 2:\n", arr2d * 2)

import numpy as np 
arr = np.array([1,2,3,4,5,6,7,8,9,10])
summ = (arr[arr%2==0])
even = (np.sum(summ))
print(even)
print(summ)

# import numpy as np
# matrix = np.array([[2,3],[4,5]])
# print("Max: ",np.max(matrix))
# print("Min:: ",np.min(matrix))
# print("Transport: ",np.transpose(matrix))
# print("Multi: ",matrix * 2)