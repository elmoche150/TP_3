from TDA_grafo.grafo import Grafo


def leer_recomendaciones(ruta, todas_las_ciudades):
    """Lee el archivo de recomendaciones (cada linea "ciudad_1,ciudad_2"
    indica que ciudad_1 debe visitarse antes que ciudad_2) y arma un grafo
    dirigido de precedencias. Se agregan como vertices todas las ciudades
    del mapa original, tengan o no restricciones asociadas."""
    grafo = Grafo(dirigido=True)
    for ciudad in todas_las_ciudades:
        grafo.agregar_vertice(ciudad)

    with open(ruta, encoding='utf-8') as f:
        for linea in f:
            linea = linea.strip()
            if not linea:
                continue
            antes, despues = linea.rsplit(',', 1)
            grafo.agregar_vertice(antes)
            grafo.agregar_vertice(despues)
            grafo.agregar_arista(antes, despues)

    return grafo