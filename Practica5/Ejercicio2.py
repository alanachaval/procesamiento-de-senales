import matplotlib.pyplot as plot
import numpy as np
from scipy.fftpack import ifft

from Practica5.Funciones import Funciones

tiempo = np.linspace(0, 1, 5000)
senal = Funciones.generar_senoidal(tiempo, 3, 20, 0)

f1 = plot.figure(1)
f1.canvas.set_window_title('Original: Sin')
plot.xlabel('Tiempo (en segundos)')
plot.ylabel('Amplitud')
plot.plot(tiempo, senal)

f2 = plot.figure(2)
f2.canvas.set_window_title('Transformada: F(Sin)')
plot.xlabel('Frecuencia (en hertz)')
plot.ylabel('Amplitud')
senal_fft = Funciones.transformada_de_fourier(senal)
senal_fft_plot, frecuencia = Funciones.linspace_transformada(senal_fft, tiempo)
plot.plot(frecuencia, senal_fft_plot)

f3 = plot.figure(3)
f3.canvas.set_window_title('Anti-Transformada: F-1(F(Sin))')
plot.xlabel('Tiempo (en segundos)')
plot.ylabel('Amplitud')
senal_ifft = Funciones.antitrasformada_de_fourier(senal_fft)
plot.plot(tiempo, senal_ifft)

f4 = plot.figure(4)
f4.canvas.set_window_title('Anti-Transformada: F-1(F(Sin)). Mediante scipy, como referencia')
plot.xlabel('Tiempo (en segundos)')
plot.ylabel('Amplitud')
senal_ifft2 = ifft(senal_fft)
plot.plot(tiempo, senal_ifft2)

plot.show()
