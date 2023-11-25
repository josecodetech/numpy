import numpy as np
array = np.array([1, 2, 3, 4, 5])
media_movil = np.convolve(array, np.ones(3)/3, mode='valid')
print(media_movil)