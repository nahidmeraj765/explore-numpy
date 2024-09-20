# Deleting array using -> np.delete()

import numpy as np

# Deletion in 1-D array 
var = np.array([1,2,3,4,5,6])
# index  ->     0 1 2 3 4 5
del_v = np.delete(var,3) # will delete 3rd index's value 4
print(del_v) # [1 2 3 5 6]

# np.delete(array,position_to_delete)

var1 = np.array([2,3,4,5,7])
x1 = np.delete(var1,[1,3]) # passing a list of indices
# will delete 1st and 3rd index's value 2 and 5 respectively
print(x1) # [2 4 7]

var2 = np.array([2,3,4,5,7])
x2 = np.delete(var1,(1,3)) # passing a tuple of indices
# will delete 1st and 3rd index's value 2 and 5 respectively
print(x2) # [2 4 7]

# Deletion in 2-D array
var98 = np.array([[1,3,5],[7,8,9]])
v98 = np.delete(var98,(0,1)) # will delete the 0th and 1st index's value
# didn't specify the axis parameter
# the output is flattened into a 1D array
print(v98) # [5 7 8 9]

var55 = np.array([[1,2,3],[4,5,6],[7,8,9]])
v55 = np.delete(var55,0,axis=0) # will delete the 0th index -> 1st column -> row wise
print(v55)
'''
[[4 5 6]
 [7 8 9]]
'''

var67 = np.array([[10,20,30],[40,50,60]])
v67 = np.delete(var67,2,axis=1) # will delete the 2nd index -> means the 3rd column -> column wise
print(v67)
'''
[[10 20]
 [40 50]]
'''
