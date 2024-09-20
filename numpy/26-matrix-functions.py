# Matrix Functions in NumPy Arrays
'''
-Transpose
-Swapaxes
-Inverse
-Power
-Determinate
'''
import numpy as np

# *Transpose Matrix
# Transpose Matrix using np.transpose()
mat = np.matrix([[1,2,3],[4,5,6]])
print(mat)
'''
[[1 2 3]
 [4 5 6]]
'''
tran_mat = np.transpose(mat)
print(tran_mat)
'''
[[1 4]
 [2 5]
 [3 6]]
'''
print(mat.T) # shortcut -> matrix.T
'''
[[1 4]
 [2 5]
 [3 6]]
'''

# *Swap-Axes Matrix
# Swap Axes Matrix using np.swapaxes()  
var7 = np.matrix([[1,2],[3,4]])
print(var7)
'''
[[1 2]
 [3 4]]
'''
swap_mat = np.swapaxes(var7,0,1) # np.swapaxes(matrix,row,column)
print(swap_mat)
'''
[[1 2]
 [3 4]]
'''

# *Inverse Matrix
# Inverse Matrix using np.linalg.inv()
var9 = np.matrix([[1,2],[3,4]])
print(var9)
'''
[[1 2]
 [3 4]]
'''
inverse_mat = np.linalg.inv(var9)
print(inverse_mat)
'''
[[-2.   1. ]
 [ 1.5 -0.5]]
'''

# *Power Matrix
# Power Matrix using np.linalg.Matrix_Power()
var99 = np.matrix([[1,2],[3,4]])
var_power99 = np.linalg.matrix_power(var99,3) # np.linalg.Matrix_Power(matrix,value) -> where n>0 
print(var_power99) # will return (var3)^3 = var3*var3*var3
'''
[[ 37  54]
 [ 81 118]]
'''
print(var99*var99*var99)
'''
[[ 37  54]
 [ 81 118]]
'''

# Identity Matrix using np.linalg.Matrix_Power()
var77 = np.matrix([[1,2],[3,4]])
var_power77 = np.linalg.matrix_power(var77,0) # np.linalg.Matrix_Power(matrix,value) -> where n=0 
print(var_power77) # will return an identity matrix with respect of the given matrix 
'''
[[1 0]
 [0 1]]
'''

# Inverse Matrix x Power Matrix using np.linalg.Matrix_Power()
var66 = np.matrix([[1,2],[3,4]])
var_power66 = np.linalg.matrix_power(var77,-2) # np.linalg.Matrix_Power(matrix,value) -> where n<0 
print(var_power66) # when using np.linalg.matrix_power(var66, -2), it first computes the inverse of the given matrix (var66) and then raises that inverse matrix to the positive power of 2
'''
[[ 5.5  -2.5 ]
 [-3.75  1.75]]
'''

# Clarification
var44 = np.matrix([[1,2],[3,4]])
inverse44 = np.linalg.inv(var44)
print(inverse44)
'''
[[-2.   1. ]
 [ 1.5 -0.5]]
'''
power44 = np.linalg.matrix_power(inverse44,2)
print(power44)
'''
[[ 5.5  -2.5 ]
 [-3.75  1.75]]
'''

# *Finding Determinant using np.linalg.det()
var29 = np.matrix([[1,3,5],[2,4,6],[3,4,3]])
determinant_var29 = np.linalg.det(var29) # will return the determinant of the matrix
print(determinant_var29) # 4.0
