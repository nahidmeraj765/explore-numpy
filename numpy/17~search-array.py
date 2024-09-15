# Search Array: Search an array for a certain value and return the indexes that get a match
import numpy as np

# *Searching array -> np.where()
var = np.array([1,2,3,4,2,5,6,2,7]) # 1-D
# index   ->    0 1 2 3 4 5 6 7 8
x = np.where(var==2) # will find all the index number of '2' 
print(x) # (array([1, 4, 7], dtype=int64),)
y = np.where((var%2)==0) # will find all the index number of all elements that are divisible by '2'
print(y) # (array([1, 3, 4, 6, 7], dtype=int64),)

# *Search Sorted Array: which performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order -> np.searchsorted()
var1 = np.array([1,2,3,4,6,7,8]) # Sorted array
# index   ->     0 1 2 3 4 5 6
x1 = np.searchsorted(var1,5) # will display the particular index position where to set the element in that sorted array
print(x1) # 4
x2 = np.searchsorted(var1,5,side="right") # will display the particular index position where to set the element from the 'right' side in that sorted array
print(x2) # 4
x3 = np.searchsorted(var1,[3,4,5]) # will display the array of index position where to set the element in that sorted array
print(x3) # [2 3 4]