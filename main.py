import hq as hq
import pandas as pd
import networkx as nx
import calle as c
import interseccion as i
from datetime import datetime
import heapq as hq
from collections import defaultdict
import math

def actualizar_hora(g, intersecciones, hora):
    for i in range(len(intersecciones)):
        g[intersecciones[i].getOrigen()][intersecciones[i].getDestino()]['weight'] = intersecciones[i].getFactorTrafico(hora)

def dijkstra(listaAdy, nodoInicial):
  visitado = defaultdict(lambda: False)
  recorrido = defaultdict(lambda: None)
  distanciaNodoAcumulado = defaultdict(lambda: math.inf)
  distanciaNodoAcumulado[nodoInicial] = 0
  queue = [(0, nodoInicial)]
  while queue:
    pesoAcumulado, nodoActual = hq.heappop(queue)
    if not visitado[nodoActual]:
      visitado[nodoActual] = True
      for nodoVecino, peso in listaAdy[nodoActual]:
        f = pesoAcumulado + peso
        if f < distanciaNodoAcumulado[nodoVecino]:
          distanciaNodoAcumulado[nodoVecino] = f
          recorrido[nodoVecino] = nodoActual
          hq.heappush(queue, (f, nodoVecino))
  return recorrido, distanciaNodoAcumulado

def CaminoMenor(grafo, nodoInicial, nodoFinal):
  path, distanciaNodoAcumulado = dijkstra(grafo, nodoInicial)
  TerminoCamino = False
  nodoAnterior = nodoFinal
  caminoCorto = [nodoFinal]
  while not TerminoCamino:
    nodoAnterior = path[int(nodoAnterior)]
    caminoCorto.insert(0, nodoAnterior)
    if nodoAnterior == nodoInicial:
      TerminoCamino = True
  return caminoCorto, distanciaNodoAcumulado[nodoFinal]


if __name__ == "__main__":
    datosIntersecciones = pd.read_csv("./data/Lima-intersecciones.csv", sep=';', header=None)
    datosCalles = pd.read_csv("./data/Lima-calles.csv", sep=';', header=None)

    calles = []
    intersecciones = []
    conexiones = []
    ubicaciones = {}
    listaAdy = defaultdict(list)

    hora = int(datetime.now().strftime('%H'))

    for linea in datosCalles.index:
        calles.append(c.calle(datosCalles[0][linea], datosCalles[1][linea], datosCalles[2][linea]))

    for linea in datosIntersecciones.index:
        intersecciones.append(i.interseccion(datosIntersecciones[1][linea], datosIntersecciones[2][linea],
                                             datosIntersecciones[5][linea], datosIntersecciones[6][linea],
                                             datosIntersecciones[7][linea], datosIntersecciones[8][linea],
                                             datosIntersecciones[11][linea], datosIntersecciones[12][linea],
                                             datosIntersecciones[13][linea], datosIntersecciones[14][linea]))

    '''
    DIBUJAR EL GRAFO
    for i in range(len(intersecciones)):
        ubicaciones[intersecciones[i].getOrigen()] = (intersecciones[i].getOrigenX(), intersecciones[i].getOrigenY())
        ubicaciones[intersecciones[i].getDestino()] = (intersecciones[i].getDestinoX(), intersecciones[i].getDestinoY())
    '''
    inicio = input("Ingrese el ID de la intersección de inicio: ")
    final = input("Ingrese el ID de la intersección de destino: ")

    print("\n------------------RUTAS---------------------\n")
    print("1. Ruta más corta según tiempo (con tráfico)")
    print("2. Ruta más corta según tiempo (sin tráfico)")
    print("3. Ruta más corta según distancia\n")
    opcion = input("Elija una opción: ")

    if opcion == '1':
        for i in range(len(intersecciones)):
            listaAdy[intersecciones[i].getOrigen()].append(
                (intersecciones[i].getDestino(), intersecciones[i].getFactorTrafico(hora)))
            '''
                DIBUJAR EL GRAFO
            conexiones.append((intersecciones[i].getOrigen(), intersecciones[i].getDestino(),
                               {'weight': intersecciones[i].getFactorTrafico(hora)}))
            '''
    elif opcion == '3':
        for i in range(len(intersecciones)):
            listaAdy[intersecciones[i].getOrigen()].append(
                (intersecciones[i].getDestino(), intersecciones[i].getDistancia()))
            '''
                DIBUJAR EL GRAFO
            conexiones.append((intersecciones[i].getOrigen(), intersecciones[i].getDestino(),
                               {'weight': intersecciones[i].getDistancia}))
            '''
    else:
        for i in range(len(intersecciones)):
            listaAdy[intersecciones[i].getOrigen()].append(
                (intersecciones[i].getDestino(), intersecciones[i].getTiempo()))
            '''
                DIBUJAR EL GRAFO
            conexiones.append((intersecciones[i].getOrigen(), intersecciones[i].getDestino(),
                               {'weight': intersecciones[i].getTiempo()}))
            '''

    ''' 
    DIBUJAR EL GRAFO
    g = nx.Graph()
    g.add_nodes_from(ubicaciones.keys())
    g.add_edges_from(conexiones)
    '''


    path, distancia = CaminoMenor(listaAdy, int(inicio), int(final))

    print(path)