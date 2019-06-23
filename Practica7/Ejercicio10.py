import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft

from Senal.Funciones import Funciones

size_window = 100
offset = np.zeros(1000, dtype=np.complex_)
n_muestra = np.array(range(size_window + 2 * len(offset)))

ventanas_funcs = [(0, Funciones.ventana_rectangular, 'Rectangular'),
                  (1, Funciones.ventana_triangular, 'Triangular'),
                  (2, Funciones.ventana_hamming, 'Hamming')]
for i, func, nombre in ventanas_funcs:
    ventana = np.concatenate((offset, func(size_window), offset))
    ventana_fft = fft(ventana)
    ventana_fft_modulo = np.abs(ventana_fft)
    ventana_fft_modulo_plot, frecuencia = Funciones.linspace_transformada(ventana_fft_modulo, n_muestra)
    Funciones.plot(i * 3, ventana_fft_modulo_plot, frecuencia, nombre + ' - Modulo de Transformada',
                   'Numero de muestra',
                   'Amplitud')
    max_value = np.max(ventana_fft_modulo_plot)
    ventana_fft_modulo_decibeles_plot = (20 * np.log10(ventana_fft_modulo_plot / max_value))
    Funciones.plot(i * 3 + 1, ventana_fft_modulo_decibeles_plot, frecuencia,
                   nombre + ' - Modulo de Transformada en Decibeles', 'Numero de muestra', 'Amplitud (dB)')
    ventana_fft_fase = np.angle(ventana_fft, deg=True)
    Funciones.plot(i * 3 + 2, ventana_fft_fase, frecuencia, nombre + ' - Fase de Transformada', 'Numero de muestra',
                   'Fase (Grados)')

plt.show()
