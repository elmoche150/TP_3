from TDA_grafo.grafo import Grafo
from algoritmos.bfs import bfs


def circuito_euleriano(grafo, origen):
    """Circuito que recorre cada arista de grafo exactamente una vez,
    empezando y terminando en origen (algoritmo de Hierholzer). Devuelve
    (circuito, peso_total). Si no existe tal circuito, devuelve (None, None)."""
    if not grafo.existe_vertice(origen):
        return None, None

    con_aristas = [v for v in grafo.obtener_vertices() if grafo.grado(v) > 0]

    if not con_aristas:
        return [origen], 0

    if grafo.grado(origen) == 0:
        return None, None  

    alcanzables = bfs(grafo, origen)
    if not all(v in alcanzables for v in con_aristas):
        return None, None  

    if any(grafo.grado(v) % 2 != 0 for v in con_aristas):
        return None, None

    copia = _copiar_grafo(grafo)
    cantidad_aristas = len(grafo.obtener_aristas())
    peso_total = sum(peso for _, _, peso in grafo.obtener_aristas())

    pila = [origen]
    circuito = []
    while pila:
        v = pila[-1]
        ady = copia.adyacentes(v)
        if ady:
            w = ady[0]
            copia.borrar_arista(v, w)
            pila.append(w)
        else:
            circuito.append(pila.pop())

    circuito.reverse()

    if len(circuito) != cantidad_aristas + 1:
        return None, None

    return circuito, peso_total


def _copiar_grafo(grafo):
    copia = Grafo(dirigido=grafo.dirigido)
    for v in grafo.obtener_vertices():
        copia.agregar_vertice(v)
    for v, w, peso in grafo.obtener_aristas():
        copia.agregar_arista(v, w, peso)
    return copia