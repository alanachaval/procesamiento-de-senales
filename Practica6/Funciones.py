import numpy as np


class Funciones:

    @staticmethod
    def modular_en_amplitud(senal, linspace, frecuencia_portadora):
        return senal * np.sin(linspace * frecuencia_portadora)
