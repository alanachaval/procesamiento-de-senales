import matplotlib.pyplot as plt
import numpy as np

from Senal.Funciones import Funciones

size = 50
ventana = np.array(range(size))

rectangular = Funciones.ventana_rectangular(size)
triangular = Funciones.ventana_triangular(size)
hamming = Funciones.ventana_hamming(size)

Funciones.scatter(1, rectangular, ventana, 'Rectangular', 'Numero de muestra', 'Amplitud')
Funciones.scatter(1, triangular, ventana, 'Triangular', 'Numero de muestra', 'Amplitud')
Funciones.scatter(1, hamming, ventana, 'Hamming', 'Numero de muestra', 'Amplitud')

plt.show()
