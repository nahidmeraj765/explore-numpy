'''
There are two rules in broadcasting..
1. Same Dimension Rule
2. Shape Compatibility Rule: Starting from the rightmost dimension and moving left, the dimensions of the arrays must either:
Be equal, or One of the dimensions must be '1'
Like, (1,3) + (3,1) -> Broadcasts to (3,3)
And, (2,1) + (2,3) -> Broadcasts to (2,3)
Again, (1,3) + (1,4) -> Broadcasting Error
'''

import numpy as np

var1 = np.array([[1,2,3]]) # (1,3)
print(var1) # [1,2,3]
print(var1.shape) # (3,)

var2 = np.array([[1],[2],[3]]) # (3,1)
print(var2) 
'''
[[1]
 [2]
 [3]]
 '''
print(var2.shape) # (3,1)

print(var1 + var2)
'''
[[2 3 4]
 [3 4 5]
 [4 5 6]]
'''
