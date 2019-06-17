import numpy as np
import matplotlib.pyplot as plt

from Practica5.Funciones import Funciones as FuncionesPractica5
from Practica6.Funciones import Funciones

tiempo = np.linspace(0, 1, 40000)
senal = FuncionesPractica5.generar_senoidal(tiempo, 3, 20, 0)
senal_modulada = Funciones.modular_en_amplitud(senal, tiempo, 5000)

FuncionesPractica5.plot(1, senal, tiempo, 'Original: Sin', 'Tiempo (en segundos)', 'Amplitud')
FuncionesPractica5.plot(2, senal_modulada, tiempo, 'Modulada: Sin', 'Tiempo (en segundos)', 'Amplitud')

plt.show()
