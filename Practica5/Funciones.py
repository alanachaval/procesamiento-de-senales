import numpy as np
from scipy.fftpack import fft


class Funciones:

    @staticmethod
    def generar_senoidal(linspace, amplitud, freuencia, fase):
        senal = np.sin(fase + linspace * freuencia * 2 * np.pi) * amplitud
        return senal

    @staticmethod
    def transformada_de_fourier(senal):
        return fft(senal)

    @staticmethod
    def antitrasformada_de_fourier(senal):
        return np.flip(Funciones.transformada_de_fourier(senal)) / len(senal)

    @staticmethod
    def generar_diente_de_sierra(linspace, amplitud, freuencia, fase):
        senal = np.zeros(len(linspace))
        offset = fase * amplitud / (2 * np.pi)
        for i in range(len(linspace)):
            senal[i] = 2 * ((linspace[i] * freuencia * amplitud + offset) % amplitud) - amplitud
        return senal

    @staticmethod
    def linspace_transformada(senal, linspace):
        espacio_entre_muestras = linspace[1] - linspace[0]
        frecuencia_maxima = 1.0 / (2.0 * espacio_entre_muestras)
        return np.fft.fftshift(senal), np.linspace(-frecuencia_maxima, frecuencia_maxima, len(linspace))
