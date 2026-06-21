def bfs(grafo, origen):
    """Recorrido BFS desde origen. Devuelve el conjunto de vertices
    alcanzables (incluyendo al propio origen)."""
    visitados = {origen}
    cola = [origen]
    inicio = 0
    while inicio < len(cola):
        v = cola[inicio]
        inicio += 1
        for w in grafo.adyacentes(v):
            if w not in visitados:
                visitados.add(w)
                cola.append(w)
    return visitados
