# Access 3-D arrays

# - To access elements from 3-D arrays we can use comma separated integers representing the dimensions and the index of the element.

import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# Access the third element of the second array of the first array:
print((arr[0, 1, 2]))
