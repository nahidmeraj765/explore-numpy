# Slicing NumPy Arrays
import numpy as np

# *1-D array slicing
x1 = np.array([1,2,3,4,5,6]) # 1-D
# indexing:    0 1 2 3 4 5 (positive)
# indexing:  -6 -5 -4 -3 -2 -1 (negative)
# x1[start:stop] -> start(include) to stop(exclude)
print(x1[1:3]) # [2 3]
print(x1[1:]) # index 1 to end -> [2 3 4 5 6]
print(x1[:3]) # index 0 to 2 -> [1 2 3]
print(x1[::2]) # start to end with one step -> [1 3 5]
# x1[start:stop:step] -> step - gap
print(x1[0:5:2]) # [1 3 5]
print(x1[-3:-1]) # last index to 2nd last index -> [4 5]
print(x1[-1:-4]) # []

# *2-D array slicing
x2 = np.array([[1,2],[3,4],[5,6]]) # 2-D
print(x2.ndim) # 2
print(x2.shape) # (3,2)
print(x2[0,0:1]) # in 1st row (element's index 0) -> [1]
print(x2[2,:]) # in 3rd row (element's index 0 to 1) -> [5 6]

# *3-D array slicing
x3 = np.array([[[1,2,3,4],[5,6,7,8]],[[1,3,5,7],[2,4,6,8]],[[10,20,30,40],[50,60,70,80]]]) # 3-D
print(x3)
print(x3.ndim) # 3
print(x3.shape) # (3,2,4)
print(x3[0,1,0:3]) # [5 6 7]
print(x3[2,0,1:3]) # [20 30]