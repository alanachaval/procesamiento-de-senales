import matplotlib.pyplot as plot
import numpy as np

from Practica5.Funciones import Funciones

tiempo = np.linspace(0, 1, 5000)
senal = Funciones.generar_diente_de_sierra(tiempo, 3, 20, np.pi)

f1 = plot.figure(1)
f1.canvas.set_window_title('Diente de sierra periodica')
plot.xlabel('Tiempo (en segundos)')
plot.ylabel('Amplitud')
plot.plot(tiempo, senal)

senal_fft = Funciones.transformada_de_fourier(senal)
f2 = plot.figure(2)
f2.canvas.set_window_title('Transformada diente de sierra periodica')
plot.xlabel('Frecuencia (en hertz)')
plot.ylabel('Amplitud')
senal_fft_plot, frecuencia = Funciones.linspace_transformada(senal_fft, tiempo)
plot.plot(frecuencia, senal_fft)

senal_no_periodica = np.zeros(5000)
for i in range(250 * 9, 250 * 10):
    senal_no_periodica[i] = senal[i]
f3 = plot.figure(3)
f3.canvas.set_window_title('Diente de sierra')
plot.xlabel('Tiempo (en segundos)')
plot.ylabel('Amplitud')
plot.plot(tiempo, senal_no_periodica)

senal_no_periodica_fft = Funciones.transformada_de_fourier(senal_no_periodica)
f4 = plot.figure(4)
f4.canvas.set_window_title('Transformada diente de sierra')
plot.xlabel('Frecuencia (en hertz)')
plot.ylabel('Amplitud')
senal_no_periodica_fft_plot, frecuencia = Funciones.linspace_transformada(senal_no_periodica_fft, tiempo)
plot.plot(frecuencia, senal_no_periodica_fft_plot)

plot.show()
