import matplotlib.pyplot as plt
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

    @staticmethod
    def plot(id, senal, linspace, title, xlabel, ylabel):
        fig = plt.figure(id)
        fig.canvas.set_window_title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.plot(linspace, senal)

    @staticmethod
    def scatter(id, senal, linspace, title, xlabel, ylabel):
        fig = plt.figure(id)
        fig.canvas.set_window_title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.scatter(linspace, senal)

    @staticmethod
    def modular_en_amplitud(senal, tiempo, frecuencia_portadora):
        return senal * np.cos(tiempo * frecuencia_portadora * 2 * np.pi)

    @staticmethod
    def ventana_rectangular(size):
        ventana = np.ones(size)
        return ventana

    @staticmethod
    def ventana_triangular(size):
        ventana = np.array(range(size))
        centro = 1.0 * size / 2.0
        ventana = 1.0 - abs(ventana + 0.5 - centro) / centro
        return ventana

    @staticmethod
    def ventana_hamming(size):
        n = np.array(range(size))
        ventana = 0.54 - 0.46 * np.cos(2 * np.pi * (n + 0.5) / size)
        return ventana
