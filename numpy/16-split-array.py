# Split Array - Splitting breaks one array into multiple
import numpy as np

# *Spiting in 1-D arrays
x = np.array([1,2,3,4,5,6]) # 1-D
arr = np.array_split(x,3) # will split the array into three parts
print(arr) # [array([1, 2]), array([3, 4]), array([5, 6])]
print(type(arr)) # <class 'list'>
print(arr[0]) # [1 2]

# *Spiting in 2-D arrays
y = np.array([[1,2,3],[4,5,6],[7,8,9]]) # 2-D
print(np.shape(y)) # (3,3)
arr1 = np.array_split(y,3) # will split the array into three parts
print(arr1) # [array([[1, 2, 3]]), array([[4, 5, 6]]), array([[7, 8, 9]])]
print(type(arr1)) # <class 'list'>
print(arr1[0]) #  [[1 2 3]]

# *Spiting in 2-D arrays with axis wise
z = np.array([[11,22,33],[44,55,66],[77,88,99]]) # 2-D
print(np.shape(z)) # (3,3)
arr11 = np.array_split(z,3,axis=1) # will split the array into two parts -> row wise
print(arr11)
'''
[array([[11],
       [44],
       [77]]), array([[22],
       [55],
       [88]]), array([[33],
       [66],
       [99]])]
'''