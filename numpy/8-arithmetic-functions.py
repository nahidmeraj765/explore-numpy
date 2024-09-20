'''
Arithmetic Functions
np.min(x)
np.max(x)
np.argmin(x)
np.argmax(x)
np.sqrt(x)
np.sin(x)
np.cos(x)
np.cumsum(x)
'''

import numpy as np

# * 1-D Arrays
var = np.array([10,2,13,4,7])
maximum = np.max(var) # will find the maximum value of the array
minimum = np.min(var) # will find the minimum value of the array
max_pos = np.argmax(var) # will find the maximum value's position in the array
min_pos = np.argmin(var) # will find the minimum value's position in the array
square_root = np.sqrt(var) # will find the square root value of each element in the array 
sine_value =  np.sin(var) # will find the sine value of each element in the array 
cosine_value = np.cos(var) # will find the cosine value of each element in the array
community_sum = np.cumsum(var) # first index value will be fixed and will continuously add the current value with the previous value
print("Community Sum : ",community_sum) # [10,2,13,4,7] -> [10 12 25 29 36]

print("Maximum Value: ",maximum) # 13
print("Minimum Value: ",minimum) # 2
print("Maximum Value's Position: ",max_pos) # 2
print("Minimum Value's Position: ",min_pos) # 1
print("Square Root Value: ",square_root) # [3.16227766 1.41421356 3.60555128 2.         2.64575131]
print("Sine Value: ",sine_value) # [-0.54402111  0.90929743  0.42016704 -0.7568025   0.6569866 ]
print(cosine_value) # [-0.83907153 -0.41614684  0.90744678 -0.65364362  0.75390225]

# *2-D array
var1 = np.array([[1,2,3,4],[5,6,7,8]])
max2 = np.max(var1,axis=1) # axis = 0 -> column ~ axis = 1 -> row
max3 = np.max(var1,axis=0) # column wise
print(max2) # [4 8] ~ 1's row max value = 4 & 2nd row max value = 8
print(max3) # [5 6 7 8] ~ column wise maximum value
