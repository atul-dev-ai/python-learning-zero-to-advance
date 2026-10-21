import numpy as np
# Concatenation joins arrays along an existing axis

a = np.array([10, 20, 30])
b = np.array([40, 50, 60])

result = np.concatenate((a, b))
print(result)