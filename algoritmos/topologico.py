def orden_topologico(grafo):
    """Orden topologico de un grafo dirigido (algoritmo de Kahn). Las
    ciudades sin restricciones de precedencia (grado de entrada 0 desde
    el arranque) tambien quedan incluidas en el resultado. Si el grafo
    tiene un ciclo, devuelve None (no se puede cumplir con lo pedido)."""
    grado_entrada = {v: 0 for v in grafo.obtener_vertices()}
    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):
            grado_entrada[w] += 1

    cola = [v for v in grafo.obtener_vertices() if grado_entrada[v] == 0]
    orden = []

    inicio = 0
    while inicio < len(cola):
        v = cola[inicio]
        inicio += 1
        orden.append(v)
        for w in grafo.adyacentes(v):
            grado_entrada[w] -= 1
            if grado_entrada[w] == 0:
                cola.append(w)

    if len(orden) != grafo.cantidad_vertices():
        return None  # quedaron vertices con grado de entrada > 0 -> habia un ciclo

    return orden