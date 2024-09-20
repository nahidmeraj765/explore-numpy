# *Inserting in array using np.insert()

import numpy as np

# Insertion in 1-D array
var = np.array([1,2,3,4,5,6,8,9,10]) # 1-D
insert_var = np.insert(var,6,7) # np.insert(array,position,value)
print(insert_var) # [ 1  2  3  4  5  6  7  8  9 10]

var1 = np.array([10,20,30,40,50])
v1 = np.insert(var1,(1,3,5),90) # inserting multiple 90 -> in 1st 3rd and 5th position
print(v1) # [10 90 20 30 90 40 50 90]

var2 = np.array([1,3,5,7,9,11,13])
v2 = np.insert(var2,(1,3,5),(2,4,6)) # # inserting multiple values 2 4 6 -> in 1st 3rd and 5th position
print(v2) # [ 1  2  3  5  4  7  9  6 11 13]
print(type(v2)) # <class 'numpy.ndarray'>

# Insertion in 2-D array
var33 = np.array([[1,2,3],[4,5,6]]) # 2-D
v33 = np.insert(var33,1,[7,8,9],axis=0) # np.insert(array,position,value,axis)
print(v33)
'''
axis = 0 -> row wise
[[1 2 3]
 [7 8 9] -> 1st position
 [4 5 6]]
 '''

var44 = np.array([[2,4,6],[8,10,12]]) # 2-D
v44 = np.insert(var44,1,[14,16],axis=1) # axis = 1 -> column wise
print(v44)
'''
[[ 2 14  4  6]
 [ 8 16 10 12]]
 '''
