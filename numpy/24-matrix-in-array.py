# Matrix in array
# Create Matrix
import numpy as np 

var = np.matrix([[1,2,3],[4,5,6]])
print(var)
'''
[[1 2 3]
 [4 5 6]]
'''
print(type(var)) # <class 'numpy.matrix'>

# Matrix addition using '+' operator
var1 = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
var2 = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
matrix_add = var1 + var2
print(matrix_add)
'''
[[ 2  4  6]
 [ 8 10 12]
 [14 16 18]]
'''

# Matrix subtraction using '-' operator
var3 = np.matrix([[9,8,7],[6,5,4],[3,2,1]])
var4 = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
matrix_sub = var3 - var4
print(matrix_sub)
'''
[[ 8  6  4]
 [ 2  0 -2]
 [-4 -6 -8]]
'''

# Matrix multiplication using '*' operator
var5 = np.matrix([[9,8,7],[6,5,4],[3,2,1]])
var6 = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
matrix_mul = var5*var6
print(matrix_mul)
'''
[[ 90 114 138]
 [ 54  69  84]
 [ 18  24  30]]
'''

# Note: For matrix multiplication to work, you need the number of columns in the first matrix to match the number of rows in the second matrix.
x = np.matrix([[1,2,3],[4,5,6]]) # (2x3)
y = np.matrix([[1,2,3],[4,5,6]]) # (2x3)
transpose = y.T # makes y from (2x3) to (3x2)
z = x*transpose # Using matrix multiplication (transpose to match dimensions)
print(z)
'''
[[14 32]
 [32 77]]
'''



