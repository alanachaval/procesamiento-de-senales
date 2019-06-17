import matplotlib.pyplot as plot
import numpy as np
from scipy.fftpack import fft, ifft


class Ejercicio1:

    @staticmethod
    def transformada_de_fourier(senal):
        return fft(senal)

    @staticmethod
    def antitrasformada_de_fourier(senal):
        return np.flip(Ejercicio1.transformada_de_fourier(senal)) / len(senal)


tiempo = np.linspace(0, 30, 600)
senal = np.sin(tiempo * 2 * np.pi)

f1 = plot.figure(1)
f1.canvas.set_window_title('1')
plot.xlabel('Tiempo (en segundos)')
plot.ylabel('Amplitud')
plot.plot(tiempo, senal)

f2 = plot.figure(2)
f2.canvas.set_window_title('2')
plot.xlabel('Tiempo (en segundos)')
plot.ylabel('Amplitud')
senal_fft = Ejercicio1.transformada_de_fourier(senal)
plot.plot(tiempo, senal_fft)

f3 = plot.figure(3)
f3.canvas.set_window_title('3')
plot.xlabel('Tiempo (en segundos)')
plot.ylabel('Amplitud')
senal_ifft = Ejercicio1.antitrasformada_de_fourier(senal_fft)
plot.plot(tiempo, senal_ifft)

f4 = plot.figure(4)
f4.canvas.set_window_title('4')
plot.xlabel('Tiempo (en segundos)')
plot.ylabel('Amplitud')
senal_ifft2 = ifft(senal_fft)
plot.plot(tiempo, senal_ifft2)

plot.show()
