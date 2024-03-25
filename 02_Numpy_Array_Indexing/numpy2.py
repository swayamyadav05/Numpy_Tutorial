# Access 2-D arrays

# - To access elements from 2-D arrays we can use comma separated integers representing the dimension and the index of the element.

# - Think of 2-D arrays like a table with rows and columns, where the dimension represents the row and the index.

import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# print("2nd element on 1st row:", arr[0, 1])
# print("5th element in 2nd row:", arr[1, 4])


# Access the element ont the first row, second column:
print("Element on 1st row, 2nd column:", arr[0, 1])

# Access the element ont the 2nd row, 5th column:
print("Element on 2nd row, 5th column:", arr[1, 4])
