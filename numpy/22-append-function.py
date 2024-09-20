# *Appending array using np.append()
import numpy as np 

# Appending in 1-D array

var3 = np.array([2,4,6,8,10,12,14,16])
v3 = np.append(var3,18) # will append 8 at the end of the array
print(v3) # [ 2  4  6  8 10 12 14 16 18]

var4 = np.array([1,2,3,4])
v4 = np.append(var4,[5,6,7,8]) # will append all the values at the end of the array
print(v4) # [1 2 3 4 5 6 7 8]

# Appending in 2-D array
var77 = np.array([[1,2,3],[4,5,6]]) # 2-D
v7 = np.append(var77,[[7,8,9]],axis=0) # row wise
print(v7)
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]
'''

var88 = np.array([[2,4,6],[1,3,5]]) # 2-D
v8 = np.append(var88,[[8,10],[7,9]],axis=1) # column wise
print(v8)
'''
[[ 2  4  6  8 10]
 [ 1  3  5  7  9]]
'''

v99 = np.array([[2,3],[4,5]])
v9 = np.append(v99,[[6,7]]) # didn't specify the axis parameter
# the output is flattened into a 1D array
print(v9) # [2 3 4 5 6 7]
