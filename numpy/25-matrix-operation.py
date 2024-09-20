import numpy as np 

# *Matrix addition using np.add()
var1 = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
var2 = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
mat_add = np.add(var1,var2) # np.add()
print(mat_add)
'''
[[ 2  4  6]
 [ 8 10 12]
 [14 16 18]]
'''

# *Matrix subtraction using np.subtract()
var3 = np.matrix([[9,8,7],[6,5,4],[3,2,1]])
var4 = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
mat_sub = np.subtract(var3,var4)
print(mat_sub)
'''
[[ 8  6  4]
 [ 2  0 -2]
 [-4 -6 -8]]
'''

# *Matrix multiplication using dot()
var5 = np.matrix([[9,8,7],[6,5,4],[3,2,1]])
var6 = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
mat_mul = var3.dot(var4) # matrix1.dot(matrix2)
print(mat_mul)
'''
[[ 90 114 138]
 [ 54  69  84]
 [ 18  24  30]]
'''