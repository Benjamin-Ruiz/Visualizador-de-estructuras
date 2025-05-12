
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaSimple:
    def __init__(self, tipo):
        self.cabeza = None
        self.tamanio = 0
        self.tipo = tipo

    def insertar_inicio(self, valor):
        nuevo = Nodo(valor)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        self.tamanio += 1

    def insertar_final(self, valor):
        nuevo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self.tamanio += 1

    def eliminar_inicio(self):
        if not self.cabeza:
            return None
        valor = self.cabeza.valor
        self.cabeza = self.cabeza.siguiente
        self.tamanio -= 1
        return valor

    def eliminar_final(self):
        if not self.cabeza:
            return None
        if not self.cabeza.siguiente:
            valor = self.cabeza.valor
            self.cabeza = None
        else:
            actual = self.cabeza
            while actual.siguiente.siguiente:
                actual = actual.siguiente
            valor = actual.siguiente.valor
            actual.siguiente = None
        self.tamanio -= 1
        return valor

    def buscar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False

    def get_info(self):
        info = f"Tipo de dato: {self.tipo}\nTamaño: {self.tamanio}\n"
        actual = self.cabeza
        i = 0
        while actual:
            info += f"[{i}] Valor: {actual.valor}, Dirección: {id(actual)}\n"
            actual = actual.siguiente
            i += 1
        return info

    def get_visual_info(self):
        dot = "digraph G {\n  rankdir=LR;\n  node [shape=record];\n"
        actual = self.cabeza
        i = 0
        while actual:
            dot += f"  nodo{i} [label=\"{actual.valor} | {id(actual)}\"]\n"
            if actual.siguiente:
                dot += f"  nodo{i} -> nodo{i+1}\n"
            actual = actual.siguiente
            i += 1
        dot += "}"
        return dot
