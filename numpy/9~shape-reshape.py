import numpy as np

# *Shape
var = np.array([[1,2],[1,2]]) # creating a 2-D array
print(var) # [[1 2] [1 2]]
print(var.shape) # (2,2)

var1 = np.array([1,2,3,4],ndmin=4) # creating a 4-D array
print(var1) # [[[[1 2 3 4]]]]
print(var1.ndim) # 4
print(var1.shape) # (1, 1, 1, 4)

# *Reshape
# *1-D to 2-D
var3 = np.array([1,2,3,4,5,6])
print(var3) # [1 2 3 4 5 6]
print(var3.ndim) # 1
new_var = var3.reshape(3,2) # reshape to 3 by 2 matrix
print(new_var)
'''
[[1 2]
 [3 4]
 [5 6]]
 '''
print(new_var.ndim) # 2

# 1-D to 3-D
var4 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(var4) # [1 2 3 4 5 6 7 8 9 10 11 12]
print(var4.ndim) # 1
new_var1 = var4.reshape(2,3,2) # reshape
print(new_var1)
'''
[[[ 1  2]
  [ 3  4]
  [ 5  6]]

 [[ 7  8]
  [ 9 10]
  [11 12]]]
 '''
print(new_var1.ndim) # 3

# * 3-D to 1-D
one = new_var1.reshape(-1) # [ 1  2  3  4  5  6  7  8  9 10 11 12]
print(one)
print(one.ndim) # 1