import matplotlib.pyplot as plt
import numpy as np

from Senal.Funciones import Funciones

tiempo = np.linspace(0, 1, 5000)
senal = Funciones.generar_diente_de_sierra(tiempo, 3, 20, np.pi)
senal_fft = Funciones.transformada_de_fourier(senal)
senal_fft_plot, frecuencia = Funciones.linspace_transformada(senal_fft, tiempo)
senal_no_periodica = np.zeros(5000)
for i in range(250 * 9, 250 * 10):
    senal_no_periodica[i] = senal[i]
senal_no_periodica_fft = Funciones.transformada_de_fourier(senal_no_periodica)
senal_no_periodica_fft_plot, frecuencia = Funciones.linspace_transformada(senal_no_periodica_fft, tiempo)

Funciones.plot(1, senal, tiempo, 'Diente de sierra periodica', 'Tiempo (en segundos)', 'Amplitud')
Funciones.plot(2, senal_fft_plot, frecuencia, 'Transformada diente de sierra periodica', 'Frecuencia (en hertz)',
               'Amplitud')
Funciones.plot(3, senal_no_periodica, tiempo, 'Diente de sierra', 'Tiempo (en segundos)', 'Amplitud')
Funciones.plot(4, senal_no_periodica_fft_plot, frecuencia, 'Transformada diente de sierra', 'Frecuencia (en hertz)',
               'Amplitud')

plt.show()
