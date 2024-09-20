# Filter Array: Getting some elements out of an existing array and creating a new array out of them
import numpy as np

arr = np.array([1,2,3,4]) # 1-D
filter_arr = [True,False,False,True]
new_arr = arr[filter_arr] # compare the corresponding indexes of both arrays and will filter only the 'True' values
print(new_arr) # [1 4]
print(type(new_arr)) # <class 'numpy.ndarray'>