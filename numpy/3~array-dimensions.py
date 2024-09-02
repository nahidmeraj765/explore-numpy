'''
Dimensions in Arrays
* 1-D Arrays: [1 2 3 4]
* 2-D Arrays: [[1 2 3 4]]
* 3-D Arrays: [[[1 2 3 4]]] 
* Higher Dimensional Arrays -> Right to Left block counting
'''
import numpy as np

oneD = np.array([1,2,3,4]) # creating an '1-D' array
print(oneD) # [1 2 3 4]
print(oneD.ndim) # 1 -> 1-D Array

twoD = np.array([[1,2,3,4],[1,2,3,4]]) # creating a '2-D' array
print(twoD) # [[1 2 3 4] [1 2 3 4]]
print(twoD.ndim) # 2 -> 2-D Array

threeD = np.array([[[1,2,3,4],[1,2,3,4],[1,2,3,4]]]) # creating a '3-D' array
print(threeD) # [[[1 2 3 4] [1 2 3 4] [1 2 3 4]]]
print(threeD.ndim) # 3 -> 3-D Array

multiD = np.array([1,2,3,4],ndmin = 10) # creating a '10-D' array
print(multiD) # [[[[[[[[[[1 2 3 4]]]]]]]]]]
print(multiD.ndim) # 10 -> 10-D Array



