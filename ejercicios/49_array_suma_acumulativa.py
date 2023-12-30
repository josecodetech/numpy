import numpy as np
array = np.array([[10, 2, 3], [4, 51, 6], [6, 9, 12]])
suma_acumulativa = array.cumsum(axis=1)
print(array)
print(suma_acumulativa)
