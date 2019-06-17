import matplotlib.pyplot as plot
import numpy as np

from Practica5.Funciones import Funciones

tiempo = np.linspace(0, 0.01, 5000)
senal = Funciones.generar_diente_de_sierra(tiempo, 5, 5000, np.pi)

f1 = plot.figure(1)
f1.canvas.set_window_title('Diente de sierra periodica')
plot.xlabel('Tiempo (en segundos)')
plot.ylabel('Amplitud')
plot.plot(tiempo, senal)

senal_fft = Funciones.transformada_de_fourier(senal)
f2 = plot.figure(2)
f2.canvas.set_window_title('Transformada diente de sierra periodica')
plot.xlabel('Tiempo (en segundos)')
plot.ylabel('Amplitud')
plot.plot(tiempo, senal_fft)

senal_no_periodica = np.zeros(5000)
for i in range(100 * 24, 100 * 25):
    senal_no_periodica[i] = senal[i]
f3 = plot.figure(3)
f3.canvas.set_window_title('Diente de sierra')
plot.xlabel('Tiempo (en segundos)')
plot.ylabel('Amplitud')
plot.plot(tiempo, senal_no_periodica)

senal_no_periodica_fft = Funciones.transformada_de_fourier(senal_no_periodica)
f4 = plot.figure(4)
f4.canvas.set_window_title('Transformada diente de sierra')
plot.xlabel('Tiempo (en segundos)')
plot.ylabel('Amplitud')
plot.plot(tiempo, senal_no_periodica_fft)

plot.show()
