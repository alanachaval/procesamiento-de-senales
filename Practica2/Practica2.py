class Practica2:

    def energia_tiempo_discreto(self, datos):
        energia_total = 0
        for d in datos:
            energia_total = + (d ** 2)
        return energia_total

    def aproximar_continua(self, datos, fs):
        return self.energia_tiempo_discreto(datos) / (fs ** 2)

    # def potencia_media_discreta(self, datos):
