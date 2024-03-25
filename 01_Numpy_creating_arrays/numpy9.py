# Higher Dimensional Arrays

# - An array can have any number of dimensions.
# - When the array is created, you can define th enumber of dimensions by using the ndmin argument.

# Create an array with 5 dimensions and verify that it has 5 dimensions:
import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print("number of dimensions :", arr.ndim)
