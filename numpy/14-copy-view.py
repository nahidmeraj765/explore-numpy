# Copy vs View
import numpy as np

# *Copy array
var = np.array([1,2,3,4])
copy_var = var.copy() # var.copy()
print("Var: ",var) # [1 2 3 4]
print("Copy: ",copy_var) # [1 2 3 4]

# *Changing the value
var[2] = 98
print("Changed Var: ",var) # [1 2 98 4]
print("Changed Copy: ",copy_var) # same as before -> [1 2 3 4]

# *View array
var1 = np.array([1,3,5,7])
view_var1 = var1.view() # var.view()
print("Var1: ",var1) # [1 3 5 7]
print("View: ",view_var1) # [1 3 5 7]

# *Changing the value
var1[1] = 99
print("Changed Var: ",var1) # [1 99 5 7]
print("Changed View: ",view_var1) # also change -> [1 99 5 7]