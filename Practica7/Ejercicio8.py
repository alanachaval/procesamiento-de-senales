import matplotlib.pyplot as plt
import numpy as np

from Senal.Funciones import Funciones

size = 50
ventana = np.array(range(size))

rectangular = Funciones.ventana_rectangular(size)
triangular = Funciones.ventana_triangular(size)
hamming = Funciones.ventana_hamming(size)

Funciones.stem(1, rectangular, ventana, 'Rectangular', 'Numero de muestra', 'Amplitud')
Funciones.stem(2, triangular, ventana, 'Triangular', 'Numero de muestra', 'Amplitud')
Funciones.stem(3, hamming, ventana, 'Hamming', 'Numero de muestra', 'Amplitud')

plt.show()
