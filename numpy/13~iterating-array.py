# Iterating NumPy Arrays
import numpy as np

# * 1-D array iteration
var = np.array([1,2,3,4]) # 1-D
print(var) # [1 2 3 4]

for i in var:
    print(i) 
'''
1
2
3
4
'''

for a in np.nditer(var):
    print(a)
'''
1
2
3
4
'''

for b in np.ndenumerate(var):
    print(b)
'''
((0,), 1)
((1,), 2)
((2,), 3)
((3,), 4)
'''

# * 2-D array iteration
var2 = np.array([[1,2,3],[4,5,6]]) # 2-D
print(var2)
'''
[[1 2 3]
 [4 5 6]]
'''
for j in var2:
    print(j)
'''
[1 2 3]
[4 5 6]
'''
# value iteration in 2-D arrays
for k in var2:
    for l in k:
        print(l)
'''
1
2
3
4
5
6
'''

# * 3-D array iteration

var3 = np.array([[[1,2,3,4],[10,20,30,40]],[[5,6,7,8],[50,60,70,80]]]) # 3-D
print(var3)
'''
[[[ 1  2  3  4]
  [10 20 30 40]]

 [[ 5  6  7  8]
  [50 60 70 80]]]
'''
print(var3.ndim) # 3

for m in var3:
    for n in m:
        for o in n:
            print(o)
'''
1
2
3
4
10
20
30
40
5
6
7
8
50
60
70
80
'''

# * iteration function -> (nditer())

for x in np.nditer(var3):
    print(x)
'''
1
2
3
4
10
20
30
40
5
6
7
8
50
60
70
80
'''

# * iteration function with indexing -> (ndenumerate())

for z in np.ndenumerate(var3):
    print(z)
'''
((0, 0, 0), 1)
((0, 0, 1), 2)
((0, 0, 2), 3)
((0, 0, 3), 4)
((0, 1, 0), 10)
((0, 1, 1), 20)
((0, 1, 2), 30)
((0, 1, 3), 40)
((1, 0, 0), 5)
((1, 0, 1), 6)
((1, 0, 2), 7)
((1, 0, 3), 8)
((1, 1, 0), 50)
((1, 1, 1), 60)
((1, 1, 2), 70)
((1, 1, 3), 80)
'''

