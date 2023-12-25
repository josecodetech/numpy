import numpy as np
array = np.array([[1, 2, 3], [41, 53, 6], [4, 5, 6], [10,1,5]])
maximo = array.max(axis=0)
print(array)
print(f'fila que contiene el maximo valor {maximo}')