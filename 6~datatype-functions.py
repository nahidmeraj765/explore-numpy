# Data Types in NumPy Arrays

'''
int_
float_
bool_
complex_

'''

import numpy as np 

varInt = np.array([1,2,3,4])
print("Data Type: ",varInt.dtype) # Data Type:  int32

varFloat = np.array([1.1,2.2,3.3,4.4])
print("Data Type: ",varFloat.dtype) # Data Type:  float64

varStr = np.array(["a","b","c","d"])
print("Data Type: ",varStr.dtype) # Data Type:  <U1

varStrInt = np.array(["a","b","c","d",1,2,3,4])
print("Data Type: ",varStrInt.dtype) # Data Type:  <U11

# Data Type conversion
x = np.array([1,2,3,4])
print("Data Type: ",x.dtype) # Data Type:  int32

y = np.array(x,dtype = np.int8)
print("Data Type: ",y.dtype) # Data Type:  int8

# int to float conversion
z = np.array([1,2,3,4],dtype="f")
print(z.dtype) # float32
print(z) # [1. 2. 3. 4.]

# int to String conversion
z1 = np.array([1,2,3,4],dtype="S")
print(z1.dtype) # |S1
print(z1) # [b'1' b'2' b'3' b'4']

# conversion with function
k = np.array([1,2,3,4])
print(k) # [1 2 3 4]
print("Data Type: ",k.dtype) # Data Type:  int32
new = np.float32(k) # conversion function
print(new) # [1. 2. 3. 4.]
print("Data Type: ",new.dtype) # Data Type:  float32

# Direct Conversion

var = np.array([1,2,3,4]) # int array
new_1 = var.astype(float) # direct conversion to float
print(var) # [1 2 3 4]
print(new_1) # [1. 2. 3. 4.]


