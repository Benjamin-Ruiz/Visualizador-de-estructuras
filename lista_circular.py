
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaCircular:
    def __init__(self, tipo):
        self.cabeza = None
        self.tamanio = 0
        self.tipo = tipo

    def insertar_inicio(self, valor):
        nuevo = Nodo(valor)
        if not self.cabeza:
            nuevo.siguiente = nuevo
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente
            nuevo.siguiente = self.cabeza
            actual.siguiente = nuevo
            self.cabeza = nuevo
        self.tamanio += 1

    def insertar_final(self, valor):
        nuevo = Nodo(valor)
        if not self.cabeza:
            nuevo.siguiente = nuevo
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente
            actual.siguiente = nuevo
            nuevo.siguiente = self.cabeza
        self.tamanio += 1

    def eliminar_inicio(self):
        if not self.cabeza:
            return None
        valor = self.cabeza.valor
        if self.cabeza.siguiente == self.cabeza:
            self.cabeza = None
        else:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente
            actual.siguiente = self.cabeza.siguiente
            self.cabeza = self.cabeza.siguiente
        self.tamanio -= 1
        return valor

    def eliminar_final(self):
        if not self.cabeza:
            return None
        actual = self.cabeza
        anterior = None
        while actual.siguiente != self.cabeza:
            anterior = actual
            actual = actual.siguiente
        valor = actual.valor
        if anterior is None:
            self.cabeza = None
        else:
            anterior.siguiente = self.cabeza
        self.tamanio -= 1
        return valor

    def buscar(self, valor):
        if not self.cabeza:
            return False
        actual = self.cabeza
        while True:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        return False

    def rotar_izquierda(self):
        if self.cabeza:
            self.cabeza = self.cabeza.siguiente

    def rotar_derecha(self):
        if not self.cabeza or self.cabeza.siguiente == self.cabeza:
            return
        actual = self.cabeza
        while actual.siguiente != self.cabeza:
            actual = actual.siguiente
        self.cabeza = actual

    def get_info(self):
        info = f"Tipo de dato: {self.tipo}\nTamaño: {self.tamanio}\n"
        if not self.cabeza:
            return info
        actual = self.cabeza
        i = 0
        while True:
            info += f"[{i}] Valor: {actual.valor}, Dirección: {id(actual)}\n"
            actual = actual.siguiente
            i += 1
            if actual == self.cabeza:
                break
        return info

    def get_visual_info(self):
        if not self.cabeza:
            return "digraph G {\n}"
        dot = "digraph G {\n  rankdir=LR;\n  node [shape=record];\n"
        actual = self.cabeza
        i = 0
        nodos = []
        while True:
            nodos.append((i, actual))
            actual = actual.siguiente
            i += 1
            if actual == self.cabeza:
                break
        for idx, nodo in nodos:
            dot += f"  nodo{idx} [label=\"{nodo.valor} | {id(nodo)}\"]\n"
        for idx in range(len(nodos)):
            siguiente = (idx + 1) % len(nodos)
            dot += f"  nodo{idx} -> nodo{siguiente}\n"
        dot += "}"
        return dot
