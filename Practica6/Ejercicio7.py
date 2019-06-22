import numpy as np
import matplotlib.pyplot as plt

from Senal.Funciones import Funciones

fs = 44000
fportadora = 5000
tiempo = np.linspace(0, 1, fs)
senal = Funciones.generar_senoidal(tiempo, 600, 20, 0)
senal_modulada = Funciones.modular_en_amplitud(senal, tiempo, fportadora)
senal_demodulada = Funciones.demodular_en_amplitud(senal_modulada, tiempo, fportadora)
senal_demodulada_fft = Funciones.transformada_de_fourier(senal_demodulada)
senal_demodulada_fft_plot, frecuencia = Funciones.linspace_transformada(senal_demodulada_fft, tiempo)

Funciones.plot(1, senal, tiempo, 'Original: Sin', 'Tiempo (en segundos)', 'Amplitud')
Funciones.plot(2, senal_modulada, tiempo, 'Modulada: Sin', 'Tiempo (en segundos)', 'Amplitud')
Funciones.plot(3, senal_demodulada, tiempo, 'Demodulada: Sin', 'Tiempo (en segundos)', 'Amplitud')
Funciones.plot(4, senal_demodulada_fft_plot, frecuencia, 'Demodulada FFT: Sin', 'Frecuencia (en Hertz)', 'Amplitud')

plt.show()
