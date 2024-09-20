# Creating numpy Arrays
import numpy as np

x = [1,2,3,4]
y = np.array(x) # creating an array using numpy
z = np.array([1,2,3,4,5])
print(y) # [1 2 3 4]
print(z) # [1 2 3 4 5]
print(type(y)) # <class 'numpy.ndarray'>

l = []
for i in range(1,5):
    n = input("enter: ")
    l.append(n)
print(np.array(l)) # ['1' '2' '3' '4'] - as strings