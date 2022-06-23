import numpy as np
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

np_height = np.array(height)
np_weight = np.array(weight)

print(type(np_height))
# Calculate bmi
bmi = np_weight / np_height ** 2

# Print the result
print(bmi)
