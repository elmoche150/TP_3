class Grafo:

    def __init__(self, dirigido=False):
        self.dirigido = dirigido
        self.ady = {}


    def agregar_vertice(self, v):
        if v not in self.ady:
            self.ady[v] = {}
    
    def agregar_arista(self, v, w, peso=1):
        self.agregar_vertice(v)
        self.agregar_vertice(w)

        self.ady[v][w] = peso

        if not self.dirigido:
            self.ady[w][v] = peso
    
    def borrar_arista(self, v, w):
        if v in self.ady and w in self.ady[v]:
            del self.ady[v][w]

        if not self.dirigido:
            if w in self.ady and v in self.ady[w]:
                del self.ady[w][v]
   
    def borrar_vertice(self, v):
        if v not in self.ady:
            return
        for w in self.ady:
            if v in self.ady[w]:
                del self.ady[w][v]
        del self.ady[v]
    
    def estan_unidos(self, v, w):
        return v in self.ady and w in self.ady[v]
    
    def peso_arista(self, v, w):
        return self.ady[v][w]
    
    def existe_vertice(self, v):
        return v in self.ady
    
    def obtener_vertices(self):
        return self.ady.keys()

    def adyacentes(self, v):
        return self.ady[v].keys()
    
    def cantidad_vertices(self):
        return len(self.ady)
    
    def obtener_grado(self, v):
        if v not in self.ady:
            raise KeyError("El vértice no existe")
        return len(self.ady[v])