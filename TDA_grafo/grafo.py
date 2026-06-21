class Grafo:

    def __init__(self, dirigido=False):
        self.dirigido = dirigido
        self.ady = {}


    def agregar_vertice(self, v):
        if v not in self.ady:
            self.ady[v] = {}
    
    def borrar_vertice(self, v, w):
        if not self.dirigido:
            del self.ady[w][v]
    
    def estan_unidos(self, v, w):
        return w in self.ady[v]
    
    def peso_arista(self, v, w):
        return self.ady[v][w]
    
    def existe_vertice(self, v):
        return v in self.ady
    
    def obtener_vertices(self):
        return self.ady.keys()

    def adyacentes(self, v):
        return self.ady[v].keys()