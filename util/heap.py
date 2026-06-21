class Heap:
    """Heap binario de minimos, implementado sobre un arreglo.
    Cada elemento se encola junto a una prioridad; desencolar siempre
    devuelve el elemento de menor prioridad."""

    def __init__(self):
        self.datos = []

    def esta_vacio(self):
        return len(self.datos) == 0

    def cantidad(self):
        return len(self.datos)

    def encolar(self, prioridad, elemento):
        self.datos.append((prioridad, elemento))
        self._sift_up(len(self.datos) - 1)

    def desencolar(self):
        if self.esta_vacio():
            raise IndexError("Heap vacio")
        self._swap(0, len(self.datos) - 1)
        prioridad, elemento = self.datos.pop()
        if not self.esta_vacio():
            self._sift_down(0)
        return prioridad, elemento

    def _upheap(self, i):
        while i > 0:
            padre = (i - 1) // 2
            if self.datos[i][0] < self.datos[padre][0]:
                self._swap(i, padre)
                i = padre
            else:
                break

    def _downheap(self, i):
        n = len(self.datos)
        while True:
            izq = 2 * i + 1
            der = 2 * i + 2
            menor = i
            if izq < n and self.datos[izq][0] < self.datos[menor][0]:
                menor = izq
            if der < n and self.datos[der][0] < self.datos[menor][0]:
                menor = der
            if menor == i:
                break
            self._swap(i, menor)
            i = menor

    def _swap(self, i, j):
        self.datos[i], self.datos[j] = self.datos[j], self.datos[i]