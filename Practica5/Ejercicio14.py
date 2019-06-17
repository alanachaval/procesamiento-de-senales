import matplotlib.pyplot as plt
import numpy as np

from Practica5.Funciones import Funciones

tiempo = np.linspace(0, 1, 5000)
senal = Funciones.generar_diente_de_sierra(tiempo, 3, 20, np.pi)

f1 = plt.figure(1)
f1.canvas.set_window_title('Diente de sierra periodica')
plt.xlabel('Tiempo (en segundos)')
plt.ylabel('Amplitud')
plt.plot(tiempo, senal)

senal_fft = Funciones.transformada_de_fourier(senal)
f2 = plt.figure(2)
f2.canvas.set_window_title('Transformada diente de sierra periodica')
plt.xlabel('Frecuencia (en hertz)')
plt.ylabel('Amplitud')
senal_fft_plot, frecuencia = Funciones.linspace_transformada(senal_fft, tiempo)
plt.plot(frecuencia, senal_fft)

senal_no_periodica = np.zeros(5000)
for i in range(250 * 9, 250 * 10):
    senal_no_periodica[i] = senal[i]
f3 = plt.figure(3)
f3.canvas.set_window_title('Diente de sierra')
plt.xlabel('Tiempo (en segundos)')
plt.ylabel('Amplitud')
plt.plot(tiempo, senal_no_periodica)

senal_no_periodica_fft = Funciones.transformada_de_fourier(senal_no_periodica)
f4 = plt.figure(4)
f4.canvas.set_window_title('Transformada diente de sierra')
plt.xlabel('Frecuencia (en hertz)')
plt.ylabel('Amplitud')
senal_no_periodica_fft_plot, frecuencia = Funciones.linspace_transformada(senal_no_periodica_fft, tiempo)
plt.plot(frecuencia, senal_no_periodica_fft_plot)

plt.show()
