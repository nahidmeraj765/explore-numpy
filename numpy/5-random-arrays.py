# create numpy arrays with random arrays

# *rand() : This function is used to generate a random value between 0 to 1

import numpy as np

var = np.random.rand(4) # random array - 1-D
print(var) # generate a random value between 0 to 1

var1 = np.random.rand(2,5) # 2-D
print(var1)

# *randn() : This function is used to generate a random value close to zero. This may return positive or negative number as well

var2 = np.random.randn(4) # 1-D
print(var2) # generate a random value close to zero (+ve || -ve)

# *ranf() : The function for doing random sampling in numpy. It returns an array of specified shape and fills it with random floats in the half open interval [0.0,1.0)

var3 = np.random.ranf(5) # 1-D
print(var3) # generate a random value between 0(include) to 1(exclude) ~ [0.0,1.0)

# *randint() : The function is used to generate a random number between a given range

var4 = np.random.randint(5,20,5) # randint(min,max,total_num)
print(var4) # generate 5 random number between a given range (5 to 20)