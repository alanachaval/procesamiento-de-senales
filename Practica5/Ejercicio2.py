import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import ifft

from Practica5.Funciones import Funciones

tiempo = np.linspace(0, 1, 5000)
senal = Funciones.generar_senoidal(tiempo, 3, 20, 0)
senal_fft = Funciones.transformada_de_fourier(senal)
senal_fft_plot, frecuencia = Funciones.linspace_transformada(senal_fft, tiempo)
senal_ifft = Funciones.antitrasformada_de_fourier(senal_fft)
senal_ifft2 = ifft(senal_fft)

f1 = plt.figure(1)
f1.canvas.set_window_title('Original: Sin')
plt.xlabel('Tiempo (en segundos)')
plt.ylabel('Amplitud')
plt.plot(tiempo, senal)

f2 = plt.figure(2)
f2.canvas.set_window_title('Transformada: F(Sin)')
plt.xlabel('Frecuencia (en hertz)')
plt.ylabel('Amplitud')
plt.plot(frecuencia, senal_fft_plot)

f3 = plt.figure(3)
f3.canvas.set_window_title('Anti-Transformada: F-1(F(Sin))')
plt.xlabel('Tiempo (en segundos)')
plt.ylabel('Amplitud')
plt.plot(tiempo, senal_ifft)

f4 = plt.figure(4)
f4.canvas.set_window_title('Anti-Transformada: F-1(F(Sin)). Mediante scipy, como referencia')
plt.xlabel('Tiempo (en segundos)')
plt.ylabel('Amplitud')
plt.plot(tiempo, senal_ifft2)

plt.show()
