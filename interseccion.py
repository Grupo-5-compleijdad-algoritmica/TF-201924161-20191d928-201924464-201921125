class interseccion:
    def __init__(self, calleId, nombre, origen, destino, distancia, velocidad, Xorigen, Yorigen, Xdestino, Ydestino):
        self.calleId = calleId
        self.nombre = nombre
        self.origen = origen
        self.destino = destino
        self.distancia = distancia
        self.velocidad = velocidad
        self.Xorigen = Xorigen
        self.Ydestino = Ydestino
        self.Yorigen = Yorigen
        self.Xdestino = Xdestino

    def getOrigen(self):
        return self.origen

    def getDestino(self):
        return self.destino