def reconstruir_camino(padre, origen, destino):
    """Dado un diccionario vertice -> padre (armado por Dijkstra, BFS, etc.),
    devuelve la lista de vertices desde origen hasta destino. Si destino
    no es alcanzable desde origen segun el diccionario, devuelve None."""
    camino = []
    actual = destino
    while actual is not None:
        camino.append(actual)
        if actual == origen:
            break
        actual = padre.get(actual)
    else:
        return None

    camino.reverse()
    if camino[0] != origen:
        return None
    return camino