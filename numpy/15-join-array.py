# Join Array - Joining means putting contents of two or more arrays in a single array
import numpy as np

# *Join Array in 1-D arrays with np.concatenate()

var1 = np.array([1,2,3,4]) # 1-D
var2 = np.array([5,6,7,8]) # 1-D
concat_var = np.concatenate((var1,var2)) # will merge both arrays var1 & var2
print(concat_var) # [1 2 3 4 5 6 7 8]

# *Join Array in 2-D arrays with np.concatenate()

var11 = np.array([[1,2],[3,4]]) # 2-D
var22 = np.array([[5,6],[7,8]]) # 2-D
concat_var11 = np.concatenate((var11,var22)) 
print(concat_var11)
'''
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
'''
concat_var22 = np.concatenate((var11,var22),axis=1) # row wise 
print(concat_var22)
'''
[[1 2 5 6]
 [3 4 7 8]]
'''
concat_var33 = np.concatenate((var11,var22),axis=0) # column wise 
print(concat_var33)
'''
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
'''

# *Join Array in 2-D arrays with np.stack()
x = np.array([[1,2],[5,6]]) # 2-D
y = np.array([[3,4],[7,8]]) # 2-D
z = np.stack((x,y),axis=1) # np.stack() -> column wise
print(z)
'''
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]
  '''

horizontal = np.hstack((x,y)) # will horizontally merge -> row wise
print(horizontal)
'''
[[1 2 3 4]
 [5 6 7 8]]
'''
vertical = np.vstack((x,y)) # will vertically merge -> column wise
print(vertical)
'''
[[1 2]
 [5 6]
 [3 4]
 [7 8]]
'''
height = np.dstack((x,y)) # will merge -> height wise
print(height)
'''[[[1 3]
  [2 4]]

 [[5 7]
  [6 8]]]
'''

