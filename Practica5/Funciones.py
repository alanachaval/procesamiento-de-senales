import numpy as np
from scipy.fftpack import fft


class Funciones:

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
