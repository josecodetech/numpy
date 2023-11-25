import numpy as np
x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 1, 4, 9, 16])
x_new = 2.5
y_new = np.interp(x_new, x, y)
print(y_new)
