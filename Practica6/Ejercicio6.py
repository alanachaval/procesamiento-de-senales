import matplotlib.pyplot as plt
import numpy as np

from Senal.Funciones import Funciones

tiempo = np.linspace(0, 1, 40000)
senal = Funciones.generar_senoidal(tiempo, 3, 20, 0)
senal_modulada = Funciones.modular_en_amplitud(senal, tiempo, 5000)

Funciones.plot(1, senal, tiempo, 'Original: Sin', 'Tiempo (en segundos)', 'Amplitud')
Funciones.plot(2, senal_modulada, tiempo, 'Modulada: Sin', 'Tiempo (en segundos)', 'Amplitud')

plt.show()
