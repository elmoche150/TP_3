from util.heap import Heap
from algoritmos.reconstruccion import reconstruir_camino

INFINITO = float('inf')


def camino_minimo(grafo, origen, destino):
    """Camino minimo entre origen y destino (Dijkstra), pensado para pesos
    no negativos. Devuelve (camino, distancia_total). Si origen o destino
    no existen, o no hay forma de llegar de uno a otro, devuelve (None, None)."""
    if not grafo.existe_vertice(origen) or not grafo.existe_vertice(destino):
        return None, None

    dist = {v: INFINITO for v in grafo.obtener_vertices()}
    padre = {v: None for v in grafo.obtener_vertices()}
    dist[origen] = 0

    heap = Heap()
    heap.encolar(0, origen)
    visitados = set()

    while not heap.esta_vacio():
        d, v = heap.desencolar()
        if v in visitados:
            continue
        visitados.add(v)

        if v == destino:
            break

        for w in grafo.adyacentes(v):
            if w in visitados:
                continue
            nueva_dist = d + grafo.peso_arista(v, w)
            if nueva_dist < dist[w]:
                dist[w] = nueva_dist
                padre[w] = v
                heap.encolar(nueva_dist, w)

    if dist[destino] == INFINITO:
        return None, None

    camino = reconstruir_camino(padre, origen, destino)
    return camino, dist[destino]