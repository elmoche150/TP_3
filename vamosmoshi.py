#!/usr/bin/python3
import sys

from archivos.parser_pajek import leer_pajek, escribir_pajek
from archivos.parser_recomendaciones import leer_recomendaciones
from archivos.kml import exportar_kml
from algoritmos.dijskstra import camino_minimo
from algoritmos.topologico import orden_topologico
from algoritmos.euler import circuito_euleriano
from algoritmos.mst import arbol_tendido_minimo

NO_SE_ENCONTRO_RECORRIDO = "No se encontro recorrido"


def comando_ir(grafo, coordenadas, parametros):
    if len(parametros) != 3:
        print(NO_SE_ENCONTRO_RECORRIDO)
        return
    desde, hasta, archivo = (p.strip() for p in parametros)

    camino, peso = camino_minimo(grafo, desde, hasta)
    if camino is None:
        print(NO_SE_ENCONTRO_RECORRIDO)
        return

    print(' -> '.join(camino))
    print(f"Tiempo total: {peso}")
    exportar_kml(archivo, camino, coordenadas, f"Camino desde {desde} hacia {hasta}")


def comando_itinerario(grafo, parametros):
    if len(parametros) != 1:
        print(NO_SE_ENCONTRO_RECORRIDO)
        return
    archivo_recomendaciones = parametros[0].strip()

    try:
        grafo_precedencias = leer_recomendaciones(archivo_recomendaciones, grafo.obtener_vertices())
    except (FileNotFoundError, OSError):
        print(NO_SE_ENCONTRO_RECORRIDO)
        return

    orden = orden_topologico(grafo_precedencias)
    if orden is None:
        print(NO_SE_ENCONTRO_RECORRIDO)
        return

    print(' -> '.join(orden))


def comando_viaje(grafo, coordenadas, parametros):
    if len(parametros) != 2:
        print(NO_SE_ENCONTRO_RECORRIDO)
        return
    origen, archivo = (p.strip() for p in parametros)

    if not grafo.existe_vertice(origen):
        print(NO_SE_ENCONTRO_RECORRIDO)
        return

    circuito, peso = circuito_euleriano(grafo, origen)
    if circuito is None:
        print(NO_SE_ENCONTRO_RECORRIDO)
        return

    print(' -> '.join(circuito))
    print(f"Tiempo total: {peso}")
    exportar_kml(archivo, circuito, coordenadas, f"Viaje desde {origen}")


def comando_reducir_caminos(grafo, coordenadas, parametros):
    if len(parametros) != 1:
        print(NO_SE_ENCONTRO_RECORRIDO)
        return
    archivo_destino = parametros[0].strip()

    arbol, peso_total = arbol_tendido_minimo(grafo)
    escribir_pajek(archivo_destino, arbol, coordenadas)
    print(f"Peso total: {peso_total}")


def procesar_comando(linea, grafo, coordenadas):
    linea = linea.strip()
    if not linea:
        return

    espacio = linea.find(' ')
    if espacio == -1:
        comando, resto = linea, ''
    else:
        comando, resto = linea[:espacio], linea[espacio + 1:]

    parametros = resto.split(',') if resto else []

    if comando == 'ir':
        comando_ir(grafo, coordenadas, parametros)
    elif comando == 'itinerario':
        comando_itinerario(grafo, parametros)
    elif comando == 'viaje':
        comando_viaje(grafo, coordenadas, parametros)
    elif comando == 'reducir_caminos':
        comando_reducir_caminos(grafo, coordenadas, parametros)
    else:
        print(f"Comando desconocido: {comando}")


def main():
    if len(sys.argv) != 2:
        print("Uso: ./vamosmoshi <archivo.pj>", file=sys.stderr)
        sys.exit(1)

    grafo, coordenadas = leer_pajek(sys.argv[1])

    for linea in sys.stdin:
        procesar_comando(linea, grafo, coordenadas)


if __name__ == '__main__':
    main()