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

    def getFactorTrafico(self, hora):
        if 0 < hora <= 7:
            return self.velocidad * self.distancia
        elif 7 < hora <= 9:
            return self.velocidad * self.distancia * 3
        elif 9 < hora <= 17:
            return self.velocidad * self.distancia * 1.5
        elif 17 < hora <= 21:
            return self.velocidad * self.distancia * 3
        else:
            return self.velocidad * self.distancia * 1.5

    def getTiempo(self):
        return self.distancia * self.velocidad

    def getOrigen(self):
        return self.origen

    def getDestino(self):
        return self.destino

    def getDistancia(self):
        return self.distancia

    def getOrigenX(self):
        return self.origenX

    def getOrigenY(self):
        return self.origenY

    def getDestinoX(self):
        return self.destinoX

    def getDestinoY(self):
        return self.destinoY

    def getCalleId(self):
        return self.calleId
