import numpy as np
# Crear un array de ejemplo
datos_originales = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# Escribir datos en un archivo .npy
nombre_archivo = 'datos.npy'
np.save(nombre_archivo, datos_originales)
# Leer datos del archivo .npy
datos_leidos = np.load(nombre_archivo)
# Mostrar los datos originales y los datos leídos
print("Datos originales:")
print(datos_originales)
print("\nDatos leidos del archivo:")
print(datos_leidos)

