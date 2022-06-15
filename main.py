import pandas as pd
import calle as c
import interseccion as i

datosIntersecciones = pd.read_csv("./data/Lima-intersecciones.csv", sep=';', header=None)
datosCalles = pd.read_csv("./data/Lima-calles.csv", sep=';', header=None)

calles = []
intersecciones = []
conexiones = []

for linea in datosCalles.index:
    calles.append(c.calle(datosCalles[0][linea], datosCalles[1][linea], datosCalles[2][linea]))

for linea in datosIntersecciones.index:
    intersecciones.append(i.interseccion(datosIntersecciones[1][linea], datosIntersecciones[2][linea],
                                         datosIntersecciones[5][linea], datosIntersecciones[6][linea],
                                         datosIntersecciones[7][linea], datosIntersecciones[8][linea],
                                         datosIntersecciones[11][linea], datosIntersecciones[13][linea],
                                         datosIntersecciones[12][linea], datosIntersecciones[14][linea]))

for i in range(len(intersecciones)):
    conexiones.append((intersecciones[i].getOrigen(), intersecciones[i].getDestino()))