import numpy as np
array = np.array([[100, 43, 18, 5, 1100, 4],
                 [90, 3, 8, 15, 100, 64]])
coef_correlacion = np.corrcoef(array)
print(array)
print(coef_correlacion)
