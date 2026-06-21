from TDA_grafo.grafo import Grafo


def arbol_tendido_minimo(grafo):
    """Arbol de tendido minimo de un grafo no dirigido y conexo (Kruskal
    con Union-Find). Devuelve (arbol, peso_total), donde arbol es un Grafo
    nuevo (no modifica el original)."""
    padre = {v: v for v in grafo.obtener_vertices()}

    def encontrar(v):
        raiz = v
        while padre[raiz] != raiz:
            raiz = padre[raiz]
        while padre[v] != raiz:
            padre[v], v = raiz, padre[v]
        return raiz

    def unir(v, w):
        rv, rw = encontrar(v), encontrar(w)
        if rv == rw:
            return False
        padre[rv] = rw
        return True

    arbol = Grafo(dirigido=False)
    for v in grafo.obtener_vertices():
        arbol.agregar_vertice(v)

    aristas_ordenadas = sorted(grafo.obtener_aristas(), key=lambda arista: arista[2])

    peso_total = 0
    for v, w, peso in aristas_ordenadas:
        if unir(v, w):
            arbol.agregar_arista(v, w, peso)
            peso_total += peso

    return arbol, peso_total