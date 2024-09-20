# Sort Array: Ordered sequence is any sequence that has an order corresponding to elements, like numeric or alphabetical, ascending or descending
import numpy as np 

# *Sorting 1-D array (ascending) -> np.sort()
var = np.array([3,2,2,4,3,7,6,4,5]) # 1-D
# index   ->    0 1 2 3 4 5 6 7 8
sort_arr = np.sort(var) # will sort the array ascending to descending
print(sort_arr) # [2 2 3 3 4 4 5 6 7]

# *Sorting 1-D array (alphabetical) -> np.sort()
var1 = np.array(['w','a','m','c','y','t'])
sort_arr1 = np.sort(var1) # will sort the array alphabetically
print(sort_arr1) # ['a' 'c' 'm' 't' 'w' 'y']

# *Sorting 2-D array (ascending) -> np.sort()
var22 = np.array([[2,1,4],[8,4,3],[7,6,2]]) # 2-D
sort_arr22 = np.sort(var22)
print(sort_arr22)
'''
[[1 2 4]
 [3 4 8]
 [2 6 7]]
'''


