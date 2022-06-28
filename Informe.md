![](https://i.ibb.co/zSJ1ksK/Sin-t-tulo.png)
# Aplicación Tu Ruta 
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
En la actualidad, una de las formas más comunes de trasladarnos rápidamente por una ciudad es haciendo uso de vehículos particulares. Para esto, necesitamos un conocimiento previo de las rutas que recorreremos en nuestro trayecto, tráfico de la ciudad, entre otras de las cuales pocas veces sabemos. Para solucionar esto existen múltiples aplicaciones que nos ayudan a realizar esta tarea, indicando cual es una ruta segura, corta, rápida, entre otras, para llegar a un determinado destino. 

Por ello, en el presente trabajo, veremos el proceso de implementación de Waze, renombrado como Tu Ruta, una aplicación de escritorio que nos ayudará a movilizarnos por la ciudad de Lima de la manera más rápida posible tomando en cuenta los factores de tráfico horario, distancias de recorrido y velocidades permitidas por tramos.

---

## **Objetivos**
En esta sección se definirán los objetivos generales y específicos que han propuesto lograr en el desarrollo y cumplimiento del presente trabajo.

### Objetivo General
Construir una aplicación que permita encontrar rutas para transporte terrestre entre dos puntos, considerando que estas rutas sean las más rápidas en cuanto a factores de distancias y tráfico vehicular en la ciudad de Lima en el año 2022.

### Objetivos Especificos
+ Construir sets de datos de información de la calles e intersecciones de la ciudad de Lima en el año 2022.
+ Identificar las velocidades de transporte permitidas de cada intersección entre calles de Lima en el año 2022.
+ Reconocer y analizar las horas de alto y bajo tráfico de las calles de la ciudad de Lima en el año 2022.
+ Construir algoritmo que calcule pesos en relación con los factores de distancia y tráfico de las calles de Lima en el año 2022. 
+ Construir algoritmos que busquen rutas rápidas o de menor peso obtenidos a través del algoritmo de cálculo de pesos de bordes o calles en la ciudad de Lima en el año 2022.
+ Construir la interfaz gráfica de usuario considerando criterios de User *Experience (UX)* que permita mostrar de forma gráfica las calles y rutas obtenidas de la calles de Lima en el año 2022.

---
## Área de la Ciudad
En esta sección, se detallará las específicaciones del área de mapa abarcado para el desarrollo de la aplicación.

### Descripción de la ciudad elegida
La ciudad elegida para el proyecto es Lima, ciudad capital del Perú flanqueada por el desierto costero y extendida  sobre los valles de los ríos Chillón, Rímac y Lurín.. Según el censo de 2017, es el departamento con mayor población con 8 millones 574 mil 974 habitantes.

Cuenta con una superficie de 2638 km² y 43 distritos (Lima, Ancón, Ate, Barranco, Breña, Carabayllo, Chaclacayo, La Victoria, San Borja, entre otros) con una extensión aproximada de 1500 cuadras.

### Imagen estática de la ciudad o porción de ciudad elegida
A continuación se mostrará de forma gráfica la porción de las calles consideradas de la ciudad de Lima correspondiente al año 2022.

![](https://i.ibb.co/87M8rc1/map2.png)
> *Fuente: Elaboración propia a partir de gráficos obtenidos de Google Maps ([Ciudad de Lima Google Maps](https://www.google.com/maps/@-12.0545928,-76.955946,12.1z/data=!5m1!1e2 "Ver Mapa de la porción de ciudad elegida")).*

---

## **Descripción del conjunto de datos**
En esta sección se mostrarán el modelo de datos considerados para la elaboración del mapa de la ciudad de Lima así como para la obtención de las rutas óptimas en estima de los criterios de distancia y tráfico vehicular.

### Datos consignados por calle
Los datos consignados que representarán las calles de Lima se encuentran en el archivo Lima Calles (Lima-calles.csv). Los cuales cuentan con tres campos importantes que nos permitirán identificar cada una de ellas, a continuación se mostrarán los campos considerados con sus respectivas descripciones a manera de tabla. 

| Nombre de los campos | Descripciones |
|-----------|---------------|
| ID_Calle | Representa al identificador de la calle, este no se repite. Es decir, no puede haber otra calle con el mismo identificador.|
|Nombre_Calle | Nombre de la calle real de la ciudad de Lima al año 2022. |
| Num_Intercepciones | Es el número de intercepciones con las que cuenta la calle en todo su recorrido|
> *Fuente: Elaboración Propia*

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

## **Grafo de la ciudad**
Para la elaboración del grafo que representa la ciudad de Lima en el año 2022, se realizaron las siguientes pautas, esto con el objetivo de construir los dataset en un formato determinado de tal forma que nos permitan formar el grafo que representará visualmente la ciudad de lima y asimismo encontrar rutas óptimas de transporte vehicular.

+ Para crear el grafo que representará a la ciudad de Lima en primer lugar se creó una lista de adyacencia a partir de las coordenadas de inicio y fin de cada una de las calles de la ciudad de Lima.
+ Cada calle o avenida tiene un punto de inicio y un punto final, aprovechamos esto de tal manera que, si trazamos una recta desde el punto de inicio hacia el punto final de una calle, obtendremos una recta.
![](https://i.ibb.co/pKQ8yDX/calle-recta.jpg)
> ***Nota:** Representación de una calle como una recta*

+ Sin embargo, este procedimiento tiende a no ser exacto ya que las calles no son sólo rectas, sino que pueden haber calles en forma circulas entre otras. Para solucionar este problema, dividiremos una calle en varios segmentos que los llamaremos intercepciones de tal forma que podamos tener mayor precisión sobre la forma de las calles.
![](https://i.ibb.co/nnsML3n/calle-con-intercepciones.jpg)
> ***Nota:** Se opta por generar intercepciones en calles ya que nos permite mayor precisión en cuanto a la forma de las calles de Lima.*

+ En cuanto a las relaciones entre las calles, estas se obtendrán cuando al menos dos calles se intersectan ya que de esta manera podemos decir que entre estas dos calles existe al menos una esquina.
![](https://i.ibb.co/dbct04M/calle-interseca.jpg)
> ***Nota:** Calle Jr.Paruro y Jr. Leticia se intersecan.*

+ La lista de adyacencia se creará a partir de las relaciones entre calles, si una calle A se interseca con una calle B, entonces una se agregará a la otra en la lista de adyacencia.

+ Finalmente con esta lista de adyacencia podemos crear el grafo a través de los nodos y aristas que son representados por las intersecciones y calles respectivamente. 
+ El grafo se verá como se muestra a continuación:
![](https://i.ibb.co/C9h4h6G/mapa.png)
>Interpretación del mapa de la ciudad (grafo)

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

### Implementación del algoritmo Dijkstra
El algoritmo principal Dijkstra se implementó de la siguiente manera a nivel de código:
![](https://i.ibb.co/Mkdpdvv/Dijkstra.png)
> Algoritmo Dijkstra

En el se ingresa una lista de adyacencia de nodos y el nodo inicial. El resultado de aplicar el algoritmo es una lista de nodos recorridos. A continuación veremos las variaciones de este algoritmo con los requerimientos establecidos en el trabajo:

#### Implementación del cálculo de la ruta más corta
Como se mencionó anteriormente en forma teoríca, para la implementación del algoritmo Dijkstra se tomó en cuenta el factor de tráfico horario que cambia los pesos en las aristas del mapa. Con esta consideración se desarrollo la implementación del algoritmo.

Primero, se recoge la hora que marca el reloj del sistema para calcular el factor de tráfico necesario:
![](https://i.ibb.co/8KhtMPK/actualizar-hora.png)
> Algoritmo actualizar hora

Con este factor se aplica el nuevo peso a todos los aristas de las intersecciones:
![](https://i.ibb.co/hcK8BPc/get-Trafico.png)
> Algoritmo obtener tráfico

Con los nuevos pesos y los datos de entrada ingresados por el usuario, se procede a hacer uso del Dijkstra para calculas la ruta principal origen-destino.
![](https://i.ibb.co/bBmMjTx/camino-Menor.jpg)
> Algoritmo camino menor con los nuevos pesos

Los resultados del calculo se muestran en la consola como una serie de nodos recorridos, para el ejemplo: Nodo 7 al 14, el resultado es el siguiente:
![](https://i.ibb.co/3pDQwWL/lista.jpg)
> Resultado de cálculo del algoritmo

#### Implementación del cálculo de rutas alternativas
Para el cálculo de las rutas alternativas se tomaron como criterios, las rutas sin considerar el tráfico y las rutas por criterio de distancia.

#### Ruta más corta sin considerar el tráfico
Para realizar la implementación del cálculo de esta ruta alternativa no se usó la función getFactorTráfico sino que más bien se usó el factor tiempo para el cálculo de esta ruta. 

![](https://i.ibb.co/8gd5yqZ/tiempo.png)
> Construcción de la lista de adyacencia con criterio de tiempo

## Interfaz gráfica
Para realizar la implementación de la interfaz gráfica del sistema se utilizó la biblioteca tkinder, con ella declaramos una variable screen al que se le fue asignado las dimensiones, colores y titulos requeridos. Además, se agregó la sección “Ruta de viaje” en la que se muestran los IDs de las calles por las que se transita para llegar al punto que indique en los inputs de entrada. 
![](https://i.ibb.co/W014197/form-app.jpg)
> Interfaz gráfica de Tu ruta (primera pantalla de carga)

Luego de ingresar los datos que se piden en el primer formulario, la aplicación carga el archivo web index.html en el que se visualiza el mapa completo requerido y se marca con una línea azul el recorrido necesario para llegar al destino solicitado. Por ejemplo, el resultado de partir del punto 18 al punto 724 se visualiza a continuación:
![](https://i.ibb.co/Js8NHgN/mapa-18-74.jpg)
> Ruta desde el punto 18 al punto 724 (Plaza 2 de Mayo a Morococha)

El resultado en la interfaz gráfica se muestra a continuación:
![](https://i.ibb.co/pr57GH0/form-18-x.jpg)
> Resultado en interfaz gráfica de Tu ruta (punto 18 al 724)

## **Conclusiones**

## **Referencias**

+ Presidencia del Consejo de Ministros. (2021). Lima Metropolitana: Información territorial de la provincia de Lima. [https://cdn.www.gob.pe/uploads/document/file/1903877/Lima%20Metropolitana_Informaci%C3%B3n%20Territorial%20Completo.pdf](https://cdn.www.gob.pe/uploads/document/file/1903877/Lima%20Metropolitana_Informaci%C3%B3n%20Territorial%20Completo.pdf "Visitar Lima Metropolitana: Información territorial de la provincia de Lima.") [Consulta: 16 de junio de 2022]
+ Salas, A.H. (2008, octubre). Acerca del Algoritmo de Dijkstra. https://arxiv.org/pdf/0810.0075.pdf [Consulta: 17 de junio de 2022]