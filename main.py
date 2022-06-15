import pandas as pd
import networkx as nx
import calle as c
import interseccion as i


def calcular_factor_trafico(velocidad, distancia, hora):
    if 0 < hora <= 7:
        return velocidad * distancia
    elif 7 < hora <= 9:
        return velocidad * distancia * 3
    elif 9 < hora <= 17:
        return velocidad * distancia * 1.5
    elif 17 < hora <= 21:
        return velocidad * distancia * 3
    else:
        return velocidad * distancia * 1.5


if __name__ == "__main__":
    datosIntersecciones = pd.read_csv("./data/Lima-intersecciones.csv", sep=';', header=None)
    datosCalles = pd.read_csv("./data/Lima-calles.csv", sep=';', header=None)

    calles = []
    intersecciones = []
    conexiones = []
    ubicaciones = {}

    for linea in datosCalles.index:
        calles.append(c.calle(datosCalles[0][linea], datosCalles[1][linea], datosCalles[2][linea]))

    for linea in datosIntersecciones.index:
        intersecciones.append(i.interseccion(datosIntersecciones[1][linea], datosIntersecciones[2][linea],
                                             datosIntersecciones[5][linea], datosIntersecciones[6][linea],
                                             datosIntersecciones[7][linea], datosIntersecciones[8][linea],
                                             datosIntersecciones[11][linea], datosIntersecciones[12][linea],
                                             datosIntersecciones[13][linea], datosIntersecciones[14][linea]))

    for i in range(len(intersecciones)):
        conexiones.append((intersecciones[i].getOrigen(), intersecciones[i].getDestino()))
        ubicaciones[intersecciones[i].getOrigen()] = (intersecciones[i].getOrigenX(), intersecciones[i].getOrigenY())
        ubicaciones[intersecciones[i].getDestino()] = (intersecciones[i].getDestinoX(), intersecciones[i].getDestinoY())

    g = nx.Graph()
    g.add_nodes_from(ubicaciones.keys())
    g.add_edges_from(conexiones)
