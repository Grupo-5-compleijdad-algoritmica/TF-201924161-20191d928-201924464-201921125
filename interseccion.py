class interseccion:
    def __init__(self, calleId, nombre, origen, destino, distancia, velocidad, origenX, origenY, destinoX, destinoY):
        self.calleId = calleId
        self.nombre = nombre
        self.origen = origen
        self.destino = destino
        self.distancia = distancia
        self.velocidad = velocidad
        self.origenX = origenX
        self.destinoX = destinoX
        self.origenY = origenY
        self.destinoY = destinoY

    def getOrigen(self):
        return self.origen

    def getDestino(self):
        return self.destino

    def getOrigenX(self):
        return self.origenX

    def getOrigenY(self):
        return self.origenY

    def getDestinoX(self):
        return self.destinoX

    def getDestinoY(self):
        return self.destinoY
