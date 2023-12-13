import numpy as np
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([5, 4, 3, 2, 1])
print(array1)
print(array2)
covarianza = np.cov(array1, array2)[0, 1]
print(covarianza)
