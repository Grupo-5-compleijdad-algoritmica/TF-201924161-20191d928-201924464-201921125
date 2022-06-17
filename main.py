import pandas as pd
import networkx as nx
import calle as c
import interseccion as i
from datetime import datetime

def actualizar_hora(g, intersecciones, hora):
    for i in range(len(intersecciones)):
        g[intersecciones[i].getOrigen()][intersecciones[i].getDestino()]['weight'] = intersecciones[i].getFactorTrafico(hora)


if __name__ == "__main__":
    datosIntersecciones = pd.read_csv("./data/Lima-intersecciones.csv", sep=';', header=None)
    datosCalles = pd.read_csv("./data/Lima-calles.csv", sep=';', header=None)

    calles = []
    intersecciones = []
    conexiones = []
    ubicaciones = {}

    hora = int(datetime.now().strftime('%H'))

    for linea in datosCalles.index:
        calles.append(c.calle(datosCalles[0][linea], datosCalles[1][linea], datosCalles[2][linea]))

    for linea in datosIntersecciones.index:
        intersecciones.append(i.interseccion(datosIntersecciones[1][linea], datosIntersecciones[2][linea],
                                             datosIntersecciones[5][linea], datosIntersecciones[6][linea],
                                             datosIntersecciones[7][linea], datosIntersecciones[8][linea],
                                             datosIntersecciones[11][linea], datosIntersecciones[12][linea],
                                             datosIntersecciones[13][linea], datosIntersecciones[14][linea]))

    for i in range(len(intersecciones)):
        ubicaciones[intersecciones[i].getOrigen()] = (intersecciones[i].getOrigenX(), intersecciones[i].getOrigenY())
        ubicaciones[intersecciones[i].getDestino()] = (intersecciones[i].getDestinoX(), intersecciones[i].getDestinoY())

    inicio = input("Ingrese el ID de la intersección de inicio: ")
    final = input("Ingrese el ID de la intersección de destino: ")

    print("\n------------------RUTAS---------------------\n")
    print("1. Ruta más corta según tiempo (con tráfico)")
    print("2. Ruta más corta según tiempo (sin tráfico)")
    print("3. Ruta más corta según distancia\n")
    opcion = input("Elija una opción: ")

    if opcion == '1':
        for i in range(len(intersecciones)):
            conexiones.append((intersecciones[i].getOrigen(), intersecciones[i].getDestino(),
                               {'weight': intersecciones[i].getFactorTrafico(hora)}))

    g = nx.Graph()
    g.add_nodes_from(ubicaciones.keys())
    g.add_edges_from(conexiones)

    print(nx.dijkstra_path(g, source=int(inicio), target=int(final)))