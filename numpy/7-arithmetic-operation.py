'''
Arithmetic Operation in NumPy Arrays
a+b -> np.add(a,b)
a-b -> np.subtract(a,b)
a*b -> np.multiply(a,b)
a/b -> np.divide(a,b)
a%b -> np.mod(a,b)
a**b -> np.power(a,b)
1/a -> np.reciprocal(a)
'''

# *1-D Arrays

import numpy as np 

# * Addition
var = np.array([1,2,3,4])
var_add = var + 3; # adding 3
print(var_add) # [4 5 6 7]

x = np.array([1,2,3,4])
y = np.array([1,2,3,4])
sum = x + y # adding x & y arrays
print(sum) # [2 4 6 8]

# * using arithmetic add() function
x = np.array([1,2,3,4])
y = np.array([1,2,3,4])
sum = np.add(x,y) # adding x & y arrays
print(sum) # [2 4 6 8]

# *Subtraction
var = np.array([5,6,7,8])
var_add = var - 3; # subtracting 3
print(var_add) # [2 3 4 5]

x1 = np.array([5,6,7,8])
y1 = np.array([1,2,3,4])
sub = x1 - y1 # subtracting y1 from x1 arrays
print(sub) # [4 4 4 4]

# *Modulus
k = np.array([8,6,5,4])
mod = k % 3 # mod by 3
print(mod) # [2 0 2 1]

# *Reciprocal
j = np.array([1,2,3,4])
result = np.reciprocal(j) # 1/j
print(result) # [1 0 0 0]

# *2-D Arrays

# *Addition
var21 = np.array([[1,2,3,4],[1,2,3,4]])
var31 = np.array([[1,2,3,4],[1,2,3,4]])
sum22 = np.add(var21,var31)
print(sum22) # [[2 4 6 8] [2 4 6 8]]


