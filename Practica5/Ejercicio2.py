import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import ifft

from Practica5.Funciones import Funciones

tiempo = np.linspace(0, 1, 5000)
senal = Funciones.generar_senoidal(tiempo, 3, 20, 0)
senal_fft = Funciones.transformada_de_fourier(senal)
senal_fft_plot, frecuencia = Funciones.linspace_transformada(senal_fft, tiempo)
senal_ifft = Funciones.antitrasformada_de_fourier(senal_fft)
senal_ifft_scipy = ifft(senal_fft)

Funciones.plot(1, senal, tiempo, 'Original: Sin', 'Tiempo (en segundos)', 'Amplitud')
Funciones.plot(2, senal_fft_plot, frecuencia, 'Transformada: F(Sin)', 'Frecuencia (en hertz)', 'Amplitud')
Funciones.plot(3, senal_ifft, tiempo, 'Anti-Transformada: F-1(F(Sin))', 'Tiempo (en segundos)', 'Amplitud')
Funciones.plot(4, senal_ifft_scipy, tiempo, 'Anti-Transformada: F-1(F(Sin)). Mediante scipy, como referencia',
               'Tiempo (en segundos)', 'Amplitud')

plt.show()
