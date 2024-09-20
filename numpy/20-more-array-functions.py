'''
Arithmetic Functions:
-Shuffle
-Unique
-Resize
-Flatten
-Ravel
'''
import numpy as np 

# *Shuffle array -> np.random.shuffle()
var = np.array([1,3,2,4,7])
np.random.shuffle(var)
print(var) # [2 3 4 1 7] -> will vary

# *Unique array -> np.unique()
var1 = np.array([1,2,3,3,2,5])
x = np.unique(var1) # there will be no repeated element
print(x) # [1 2 3 5]

# will also show the index value 
y = np.unique(var1,return_index=True)
print(y) # (array([1, 2, 3, 5]), array([0, 1, 2, 5], dtype=int64))

# will also count the number of elements
z = np.unique(var1,return_index=True,return_counts=True)
print(z) # (array([1, 2, 3, 5]), array([0, 1, 2, 5], dtype=int64), array([1, 2, 2, 1], dtype=int64))

# * Resize array -> np.resize()
var3 = np.array([1,2,3,4,5,6])
r = np.resize(var3,(2,3)) # two rows & three columns
print(r)
'''
[[1 2 3]
 [4 5 6]]
'''
r1 = np.resize(var3,(3,2)) # three rows & two columns
print(r1)
'''
[[1 2]
 [3 4]
 [5 6]]
'''

# *Flatten array
var7 = np.array([[1,2],[3,4],[5,6]])
print(var7.flatten()) # [1 2 3 4 5 6]
print(var7.flatten(order="F")) # [1 3 5 2 4 6]

# *Ravel array
print(np.ravel(var7)) # [1 2 3 4 5 6]
print(np.ravel(var7,order="K")) # [1 2 3 4 5 6]

'''
Order: {'C', 'F', 'A', 'K'}, Optional
*'C' means to flatten in row-major (C-style) order.
*'F' means to flatten in column-major (Fortran-style) order.
*'A' means to flatten in column-major order if `a` is Fortran *contiguous* in memory, row-major order otherwise.
*'K' means to flatten `a` in the order the elements occur in memory
The default is 'C'.
'''