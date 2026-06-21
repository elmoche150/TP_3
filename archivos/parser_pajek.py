from TDA_grafo.grafo import Grafo


def leer_pajek(ruta):
    """Lee un archivo en formato Pajek. Devuelve (grafo, coordenadas), donde
    coordenadas es un diccionario ciudad -> (lat, lon)."""
    with open(ruta, encoding='utf-8') as f:
        lineas = [linea.strip() for linea in f if linea.strip()]

    grafo = Grafo(dirigido=False)
    coordenadas = {}

    indice = 0
    cantidad_vertices = int(lineas[indice])
    indice += 1
    for _ in range(cantidad_vertices):
        nombre, lat, lon = lineas[indice].rsplit(',', 2)
        grafo.agregar_vertice(nombre)
        coordenadas[nombre] = (float(lat), float(lon))
        indice += 1

    cantidad_aristas = int(lineas[indice])
    indice += 1
    for _ in range(cantidad_aristas):
        origen, destino, peso = lineas[indice].rsplit(',', 2)
        grafo.agregar_arista(origen, destino, int(peso))
        indice += 1

    return grafo, coordenadas


def escribir_pajek(ruta, grafo, coordenadas):
    """Escribe grafo (junto con sus coordenadas) en formato Pajek."""
    vertices = grafo.obtener_vertices()
    aristas = grafo.obtener_aristas()

    with open(ruta, 'w', encoding='utf-8') as f:
        f.write(f"{len(vertices)}\n")
        for v in vertices:
            lat, lon = coordenadas[v]
            f.write(f"{v},{lat},{lon}\n")

        f.write(f"{len(aristas)}\n")
        for v, w, peso in aristas:
            f.write(f"{v},{w},{peso}\n")