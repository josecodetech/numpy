import numpy as np
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([3, 4, 5, 6, 7])
elementos_comunes = np.intersect1d(array1, array2)
print(array1)
print(array2)
print(elementos_comunes)
