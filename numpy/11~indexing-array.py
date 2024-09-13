# Indexing NumPy Arrays
import numpy as np

# *1-D array indexing
var = np.array([1,2,3,4]) # 1-D
#               0 1 2 3
#             -4 -3 -2 -1
print(var[1]) # 2
print(var[-2]) # 3

# *2-D array indexing
var2 = np.array([[1,2],[3,4]]) # 2-D
print(var2)
print(var2.ndim) # 2
print(var2[0,1]) # 2
print(var2[1,1]) # 4

# *3-D array indexing
var3 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]]) # 3-D
print(var3)
print(var3.ndim) # 3
print(var3[1,0,1]) # 6
print(var3.shape) # (2,2,2)

var31 = np.array([[[1,2],[3,4,7]],[[5,6],[7,8,9]]],dtype=object) # Create an object array with varying lengths of inner lists or with different data types
print(var31.shape) # (2,2)


