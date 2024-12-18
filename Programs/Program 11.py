# Write a program to create a 2D array using NumPy, add 5 to the array and display it.

import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

y = x + 5

print("Original Array:")
print(x)

print("Updated Array (after adding 5):")
print(y)
