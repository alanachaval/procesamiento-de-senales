import matplotlib.pyplot as plot
import numpy as np
from scipy.fftpack import ifft

from Practica5.Funciones import Funciones

tiempo = np.linspace(0, 30, 600)
senal = np.sin(tiempo * 2 * np.pi)

f1 = plot.figure(1)
f1.canvas.set_window_title('Original: Sin')
plot.xlabel('Tiempo (en segundos)')
plot.ylabel('Amplitud')
plot.plot(tiempo, senal)

f2 = plot.figure(2)
f2.canvas.set_window_title('Transformada: F(Sin)')
plot.xlabel('Tiempo (en segundos)')
plot.ylabel('Amplitud')
senal_fft = Funciones.transformada_de_fourier(senal)
plot.plot(tiempo, senal_fft)

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
