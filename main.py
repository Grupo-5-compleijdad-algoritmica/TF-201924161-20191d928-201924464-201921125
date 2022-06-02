import pandas as pd
class calle:
  def __init__(self, id, nombre, intersecciones):
    self.id = id
    self.nombre = nombre
    self.intersecciones = intersecciones

class interseccion:
  def __init__(self, id, nombre, destino, distancia, velocidad, Xorigen, Yorigen, Xdestino, Ydestino):
    self.id = id
    self.nombre = nombre
    self.distancia = distancia
    self.velocidad = velocidad
    self.Xorigen = Xorigen
    self.Ydestino = Ydestino
    self.Yorigen = Yorigen
    self.Xdestino = Xdestino

datos = pd.read_csv("./data/Lima-intersecciones.csv", sep = ';', header = None)
grafo = [[] for _ in range(len(datos) + 2)]
intersecciones = []

for linea in datos.index:
  grafo[linea].append(interseccion())
  intersecciones.append(linea[5])  
for i, edges in enumerate(grafo):
  print(f"{i:2}: {edges}")
