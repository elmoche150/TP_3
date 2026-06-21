def exportar_kml(ruta, camino, coordenadas, titulo):
    """Exporta un archivo KML con un Placemark de tipo Point por cada
    ciudad distinta que aparece en camino, y un Placemark de tipo
    LineString por cada tramo consecutivo del recorrido."""
    ciudades_unicas = []
    vistas = set()
    for ciudad in camino:
        if ciudad not in vistas:
            vistas.add(ciudad)
            ciudades_unicas.append(ciudad)

    with open(ruta, 'w', encoding='utf-8') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<kml xmlns="http://earth.google.com/kml/2.1">\n')
        f.write('\t<Document>\n')
        f.write(f'\t\t<name>{titulo}</name>\n\n')

        for ciudad in ciudades_unicas:
            lat, lon = coordenadas[ciudad]
            f.write('\t\t<Placemark>\n')
            f.write(f'\t\t\t<name>{ciudad}</name>\n')
            f.write('\t\t\t<Point>\n')
            f.write(f'\t\t\t\t<coordinates>{lat}, {lon}</coordinates>\n')
            f.write('\t\t\t</Point>\n')
            f.write('\t\t</Placemark>\n')

        f.write('\n')

        for i in range(len(camino) - 1):
            origen, destino = camino[i], camino[i + 1]
            lat1, lon1 = coordenadas[origen]
            lat2, lon2 = coordenadas[destino]
            f.write('\t\t<Placemark>\n')
            f.write('\t\t\t<LineString>\n')
            f.write(f'\t\t\t\t<coordinates>{lat1}, {lon1} {lat2}, {lon2}</coordinates>\n')
            f.write('\t\t\t</LineString>\n')
            f.write('\t\t</Placemark>\n')

        f.write('\t</Document>\n')
        f.write('</kml>\n')