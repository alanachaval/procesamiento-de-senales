import numpy as np
import matplotlib.pyplot as plt

from Practica5.Funciones import Funciones as FuncionesPractica5
from Practica6.Funciones import Funciones

tiempo = np.linspace(0, 1, 40000)
senal = FuncionesPractica5.generar_senoidal(tiempo, 3, 20, 0)
senal_modulada = Funciones.modular_en_amplitud(senal, tiempo, 5000)

f1 = plt.figure(1)
f1.canvas.set_window_title('Original: Sin')
plt.xlabel('Tiempo (en segundos)')
plt.ylabel('Amplitud')
plt.plot(tiempo, senal)

f2 = plt.figure(2)
f2.canvas.set_window_title('Modulada: Sin')
plt.xlabel('Tiempo (en segundos)')
plt.ylabel('Amplitud')
plt.plot(tiempo, senal_modulada)

plt.show()
