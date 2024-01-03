import math
import matplotlib as plt
import numpy as np

# Pide al usuario que introduzca el número de filas
filas = int(input("Plantas: "))

# Pide al usuario que introduzca el número de columnas
columnas = int(input("Places: "))

# Crea una matriz vacía de tamaño indefinido
almacen = np.full([filas, columnas], "[]")
ascensor = np.full([filas, 1], "[]")

# Crea una matriz de separación entre ambas
separation = np.full([filas, 1], "|")

# Las juntamos
estructure = np.concatenate((ascensor, separation, almacen), axis=1)

# La printeamos
for filas in estructure:
    print(*filas)