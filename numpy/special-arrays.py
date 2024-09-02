# Special numpy arrays

import numpy as np

# *zero's array : all elements filled with 0's

arr_zero = np.zeros(4) # creating a 1-D array of 4 elements filled with 0's
print(arr_zero) # [0. 0. 0. 0.]

arr_zero2 = np.zeros((3,4)) # creating a 2-D array of 3 rows and 4 columns filled with 0's
print(arr_zero2)

# *one's array : all elements filled with 1's

arr_one = np.ones(4) # creating a 1-D array of 4 elements filled with 1's
print(arr_one) # [1. 1. 1. 1.]

arr_one2 = np.ones((2,3)) # creating a 2-D array of 2 rows and 3 columns filled with 1's
print(arr_one2)

# *empty array : all elements filled with previous array's store data

arr_empty = np.empty(4) 
print(arr_empty) # [1. 1. 1. 1.]

# *range array :  an array with a range of elements

arr_range = np.arange(4)
print(arr_range) # [0 1 2 3]

arr_range = np.arange(3,7) # will contain all the values from the staring point to the ending point of the arange function
print(arr_range) # [3 4 5 6]

# *diagonal array : element filled with 1's

arr_diag = np.eye(3) # square matrix
print(arr_diag)

arr_diag1 = np.eye(4,3) # non-square matrix
print(arr_diag1)

# *create an array with values that are spaced linearly in a specified interval

arr_lin = np.linspace(0,10,num=5)
print(arr_lin) # [ 0.   2.5  5.   7.5 10. ]

arr_lin = np.linspace(0,20,num=5)
print(arr_lin) # [ 0.  5. 10. 15. 20.]






