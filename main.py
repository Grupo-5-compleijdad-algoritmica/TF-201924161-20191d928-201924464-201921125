import os.path
import tkinter

import hq as hq
import pandas as pd
import folium
import webbrowser
from tkinter import *
from tkinter import ttk
from geojson import Point, Feature, FeatureCollection, dump, LineString
import calle as c
import interseccion as i
from datetime import datetime
import heapq as hq
from collections import defaultdict
import math
import os

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

    calles = {}
    intersecciones = {}
    ubicaciones = {}
    listaAdy = defaultdict(list)

    hora = int(datetime.now().strftime('%H'))

    for linea in datosCalles.index:
        calles[datosCalles[0][linea]] = c.calle(datosCalles[0][linea], datosCalles[1][linea], datosCalles[2][linea])

    for linea in datosIntersecciones.index:
        intersecciones[(datosIntersecciones[5][linea], datosIntersecciones[6][linea])] = (i.interseccion(datosIntersecciones[1][linea], datosIntersecciones[2][linea],
                                             datosIntersecciones[5][linea], datosIntersecciones[6][linea],
                                             datosIntersecciones[7][linea], datosIntersecciones[8][linea],
                                             datosIntersecciones[11][linea], datosIntersecciones[12][linea],
                                             datosIntersecciones[13][linea], datosIntersecciones[14][linea]))

    screen = Tk()
    screen.title("Tu Ruta")
    screen.geometry("500x600")
    screen.config(background="#213141")
    screen.resizable(False, False)

    titulo = Label(text="Tu ruta", font=("Cambria", 20), bg="#56C3D3", width="550", height="3")
    titulo.pack()

    inicio = StringVar()
    final = StringVar()
    opcion = IntVar()

    def CalcularRuta():
        if opcion.get() == 1:
            for clave in intersecciones:
                listaAdy[intersecciones[clave].getOrigen()].append(
                    (intersecciones[clave].getDestino(), intersecciones[clave].getFactorTrafico(hora)))

        elif opcion.get() == 3:
            for clave in intersecciones:
                listaAdy[intersecciones[clave].getOrigen()].append(
                    (intersecciones[clave].getDestino(), intersecciones[clave].getDistancia()))
        else:
            for clave in intersecciones:
                listaAdy[intersecciones[clave].getOrigen()].append(
                    (intersecciones[clave].getDestino(), intersecciones[clave].getTiempo()))

        try:
            path, distancia = CaminoMenor(listaAdy, int(inicio.get()), int(final.get()))

            m = folium.Map(location=(intersecciones[(path[0], path[0 + 1])].getOrigenX(),
                                 intersecciones[(path[0], path[0 + 1])].getOrigenY()), zoom_start=17)

            features = []

            print(path)

            anterior = -1

            for indice in range(len(path) - 1):
                if anterior != int(intersecciones[(path[indice], path[indice + 1])].getCalleId()):
                    Calles.insert("", END, values=(intersecciones[(path[indice], path[indice + 1])].getCalleId(), calles[intersecciones[(path[indice], path[indice + 1])].getCalleId()].getNombre()))
                    anterior = int(intersecciones[(path[indice], path[indice + 1])].getCalleId())
                linea = LineString([(intersecciones[(path[indice], path[indice + 1])].getOrigenY(),
                                 intersecciones[(path[indice], path[indice + 1])].getOrigenX()), (
                                intersecciones[(path[indice], path[indice + 1])].getDestinoY(),
                                intersecciones[(path[indice], path[indice + 1])].getDestinoX())])
                features.append(Feature(geometry=linea))

            feature_collection = FeatureCollection(features)

            with open('ruta.geojson', 'w') as f:
                dump(feature_collection, f)

            rutaData = os.path.join("ruta.geojson")
            folium.GeoJson(rutaData, name='ruta').add_to(m)
            m.save("index.html")
            webbrowser.open_new_tab('index.html')
        except:
            ErrorLabel = Label(screen, text="No se ha encontrado ninguna ruta. Inténtelo de nuevo").place(x=10, y=330)


    IdLabel = Label(screen, text="Ingrese el ID de la intersección: ", font=15).place(x=10, y=120)
    inicioLabel = Label(screen, text="ID Punto de inicio: ").place(x=10, y=150)
    InicioTextBox = Entry(screen, textvariable=inicio).place(x=120, y=150)
    finalLabel = Label(screen, text="ID Punto de destino: ").place(x=10, y=180)
    FinalTextBox = Entry(screen, textvariable=final).place(x=130, y=180)
    RutasLabel = Label(screen, text="Ingrese el la ruta que desea calcular: ", font=15).place(x=10, y=120)
    Ruta1 = Radiobutton(screen, text="Ruta más corta según tiempo (con tráfico)", value=1, variable=opcion).place(x=10, y=210)
    Ruta2 = Radiobutton(screen, text="Ruta más corta según tiempo (sin tráfico)", value=2, variable=opcion).place(x=10, y=240)
    Ruta3 = Radiobutton(screen, text="Ruta más corta según distancia", value=3, variable=opcion).place(x=10, y=270)
    FinalButton = Button(screen, text="Calcular ruta", width=30, command=CalcularRuta).place(x=50, y=300)
    IdLabel = Label(screen, text="Ruta de viaje: ", font=15).place(x=10, y=370)
    Calles = ttk.Treeview(screen, columns=(1, 2), show="headings", height=7)
    Calles.place(x=10, y=400)
    Calles.column(1, width=150)
    Calles.column(2, width=310)

    Calles.heading(1, text="ID", anchor=CENTER)
    Calles.heading(2, text="Calle", anchor=CENTER)

    screen.mainloop()

