

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Cola:
    def __init__(self, tipo):
        self.frente = None
        self.final = None
        self.tamanio = 0
        self.tipo = tipo

    def insertar(self, valor):
        nuevo = Nodo(valor)
        if self.final:
            self.final.siguiente = nuevo
        self.final = nuevo
        if not self.frente:
            self.frente = nuevo
        self.tamanio += 1

    def eliminar(self):
        if not self.frente:
            return None
        valor = self.frente.valor
        self.frente = self.frente.siguiente
        if not self.frente:
            self.final = None
        self.tamanio -= 1
        return valor

    def buscar(self, valor):
        actual = self.frente
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False

    def get_info(self):
        info = f"Tipo de dato: {self.tipo}\nTamaño: {self.tamanio}\n"
        actual = self.frente
        i = 0
        while actual:
            info += f"[{i}] Valor: {actual.valor}, Dirección: {id(actual)}\n"
            actual = actual.siguiente
            i += 1
        return info

    def get_visual_info(self):
        dot = "digraph G {\n  rankdir=LR;\n  node [shape=record];\n"
        actual = self.frente
        i = 0
        while actual:
            dot += f"  nodo{i} [label=\"{actual.valor} | {id(actual)}\"]\n"
            if actual.siguiente:
                dot += f"  nodo{i} -> nodo{i+1}\n"
            actual = actual.siguiente
            i += 1
        dot += "}"
        return dot
