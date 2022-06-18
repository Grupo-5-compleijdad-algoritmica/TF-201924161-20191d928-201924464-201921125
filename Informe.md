![](https://i.ibb.co/zSJ1ksK/Sin-t-tulo.png)
# Aplicación Waze (Complejidad algoritmica)
#### Docente
Reyes Silva, Patricia Daniela
#### Integrantes
- Cordova Jimenez, Heber (u201924464)
- León Huanaquiri, Jack Ronaldo (u201921125)
- Medrano Jacobo, Alejandro (u201924161)
- Sakuda Nakamatsu, Gonzalo (u20191d928)

#### Sección 
WS6B

---

## Introducción
En la actualidad, una de las formas más comunes de trasladarnos rápidamente por una ciudad es haciendo uso de vehículos particulares. Para esto, necesitamos un conocimiento previo de las rutas que recorreremos en nuestro trayecto, tráfico de la ciudad, entre otras de las cuales pocas veces sabemos. Para solucionar esto existen múltiples **aplicaciones** que nos ayudan a realizar esta tarea, indicando cual es una ruta segura, corta, rápida, entre otras, para llegar a un determinado destino. 

Por ello, en el presente trabajo, veremos el proceso de implementación de Waze, una aplicación de escritorio que nos ayudará a movilizarnos por la ciudad de Lima de la manera más rápida posible tomando en cuenta los factores de tráfico horario, distancias de recorrido y velocidades permitidas por tramos.

---
## Área de la Ciudad
En esta sección, se detallará las específicaciones del área de mapa abarcado para el desarrollo de la aplicación.

### Descripción de la ciudad elegida
La ciudad elegida para el proyecto es Lima, ciudad capital del Perú flanqueada por el desierto costero y extendida  sobre los valles de los ríos Chillón, Rímac y Lurín.. Según el censo de 2017, es el departamento con mayor población con 8 millones 574 mil 974 habitantes.

Cuenta con una superficie de 2638 km² y 43 distritos (Lima, Ancón, Ate, Barranco, Breña, Carabayllo, Chaclacayo, La Victoria, San Borja, entre otros) con una extensión aproximada de 1500 cuadras.

## **Descripción del conjunto de datos**
En esta sección se mostrarán el modelo de datos considerados para la elaboración del mapa de la ciudad de Lima así como para la obtención de las rutas óptimas en estima de los criterios de distancia y tráfico vehicular.

### Datos consignados por intersección
Los datos consignados que representan las intersecciones de la ciudad se encuentran en el archivo Lima intersecciones (Lima-intersecciones.csv). Este grupo de datos cuenta con los siguientes campos:

| Nombre del Campo | Descripciones |
|----------------- | ------------- |
| ID_Reg | ID del registro de la intersección |
| ID_Calle | Identificador de la calle asociada a la unión de dos intersecciones |
| Nombre_Calle | Nombre de la calle |
| ID_Calle_origen | Identificador único de la calle origen asociada a una intersección origen |
| ID_Calle_destino | Identificador único de la calle destino asociado a una intersección destino |
| ID_Interseccion_Origen | Identificador único de la intersección origen |
| ID_Interseccion_destino | Identificador único de la intersección destino |
| Distancia_En_Km | Distancia en Km entre la intersección origen y la intersección destino |
| Velocidad_En_KmH | Velocidad en Km/h a la que se puede recorrer la distancia entre la intersección origen y la intersección destino |
| Costo_1 | Costo (esfuerzo) de recorrer la distancia entre la intersección origen y destino |
| Costo_2 | Costo (esfuerzo) inverso de recorrer la distancia entre la intersección origen y destino | 
| Latitud_Origen_x1 | Latitud en la que se ubica la intersección origen |
| Longitud_Origen_y1 | Longitud en la que se ubica la intersección origen |
| Latitud_Destino_x2 | Latitud en la que se ubica la intersección destino |
| Longitud_Destino_y2 | Longitud en la que se ubica la intersección destino |

> *Fuente: Elaboración propia*

---

## **Diseño del sistema de tráfico**
El costo por transitar por una calle en la aplicación está basado en tres factores: distancia, velocidad máxima permitida y tráfico.

La fórmula general de cálculo de costo es:

$$ costo = distancia \times velocidad maxima \times trafico $$

Donde:\
**Costo:** Esfuerzo necesario para recorrer la calle. \
**Distancia:** Distancia en Km entre el punto origen de la calle y el punto de llegada.\
**Velocidad maxima:** Velocidad máxima en Km/h que se permite transitar.\
**Tráfico:** Factor de tráfico añadido

Para calcular el tráfico horario en una determinada calle se hace uso de los siguientes criterios:

| Rango Horario | Tráfico |
| ------------- | ------- |
| 00:00 - 07:00 | Sin tráfico |
| 07:00 - 09:00 o 17:00 - 21:00 | Factor x3 |
| 09:00 - 17:00 o 21:00 - 00:00 | Factor x1.5 |

> *Fuente: Elaboración propia*

Según el horario en el que se calcule una ruta el costo de las calles se multiplica por el factor correspondiente de la tabla.

En código esto se implementa en la función **getFactorTrafico().**

```python 
def getFactorTrafico(self, hora):
    if 0 < hora <= 7:
        return self.velocidad * self.distancia
    elif 7 < hora <= 9:
        return self.velocidad * self.distancia * 3
    elif 9 < hora <= 11:
        return self.velocidad * self.distancia * 1.5
    elif 17 < hora <= 21:
        return self.velocidad * self.distancia * 1.5
```

Con el cambio del costo realizado se procede a calcular la mejor ruta con el algoritmo **Dijkstra** la cual se explica a continuación:

### **Cálculo de la mejor ruta**
Para calcular la mejor ruta por la que se puede ir desde un punto inicial a un punto final se hace uso del algoritmo Dijkstra.

El algoritmo Dijkstra es un algoritmo centrado en el cálculo del camino más corto dado un vertice de inicio. Desde el vertice seleccionado el algoritmo empieza a explorar todos los caminos mas cortos hacia el resto de vertices. Una vez encontrado el vertice que nos interese podemos culminar su ejecución.

#### **Algoritmo**

**Entrada:** Grafo ponderado $G=(V, E)$ dirigido de $n$ vértices con pesos positivos; $a$ y $z$ vértices distintos tales que exista algún camino de $a$ a $z$.

**Salida:** Peso de un camino de coste mínimo de $a$ a $z$.

**Paso 1:** Definimos: $S0=\phi, T0=V$. Asignamos a cada vértice $v$ en $V$ una etiqueta como sigue: $L(v)=0$ si $v=a$ y $L(v)=\infty$ para va.

**Paso 2:** Para $i=1,2, ... ,n$: Supongamos que hemos construido los conjuntos $S0, S1, ..., Si-1$. Hacemos $Ti-1=V \div Si-1$.Si $z \in Si-1$, definimos $S = Si-1$ y detenemos la construcción. En caso contrario, escogemos el primer vértice u en $Ti-1$ con la menor etiqueta, es decir, 

$$
L(u) = mín { L(v) |  v \in Ti-1 }
$$ 

Definimos $ui-1=u$ | $Si=Si-1{ ui-1 }={ u0, u1, ..., ui-1 }$, (decimos que u entra), $Ti=V \div Si$ y para cada vértice $v$ en $Ti$ adyacente a $u$ cambiamos su etiqueta $L(v)$ por la nueva etiqueta mín ${L(v), L(u) + p(u, v)}$:

$$
L(v) \leftarrow mín {L(v), L(u)+p(u, v)}
$$ 

Es decir, actualizamos la etiqueta de los vecinos de $u$ por fuera de $Si$.

**Paso 3:** Si $i=n$, definimos $S=S_n$ y nos detenemos, Si $i<n$, hacemos $i=i+1$ y vamos al paso 2. (Salas, 2008, p. 3)

## **Conclusiones**

## **Referencias**

+ Presidencia del Consejo de Ministros. (2021). Lima Metropolitana: Información territorial de la provincia de Lima. [https://cdn.www.gob.pe/uploads/document/file/1903877/Lima%20Metropolitana_Informaci%C3%B3n%20Territorial%20Completo.pdf](https://cdn.www.gob.pe/uploads/document/file/1903877/Lima%20Metropolitana_Informaci%C3%B3n%20Territorial%20Completo.pdf "Visitar Lima Metropolitana: Información territorial de la provincia de Lima.") [Consulta: 16 de junio de 2022]
+ Salas, A.H. (2008, octubre). Acerca del Algoritmo de Dijkstra. https://arxiv.org/pdf/0810.0075.pdf [Consulta: 17 de junio de 2022]