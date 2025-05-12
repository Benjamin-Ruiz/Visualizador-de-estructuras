
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.anterior = None
        self.siguiente = None

class ListaDoble:
    def __init__(self, tipo):
        self.cabeza = None
        self.tamanio = 0
        self.tipo = tipo

    def insertar_inicio(self, valor):
        nuevo = Nodo(valor)
        if self.cabeza:
            self.cabeza.anterior = nuevo
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
            nuevo.anterior = actual
        self.tamanio += 1

    def insertar_posicion(self, valor, posicion):
        if posicion <= 0:
            self.insertar_inicio(valor)
        elif posicion >= self.tamanio:
            self.insertar_final(valor)
        else:
            nuevo = Nodo(valor)
            actual = self.cabeza
            for _ in range(posicion):
                actual = actual.siguiente
            anterior = actual.anterior
            nuevo.anterior = anterior
            nuevo.siguiente = actual
            anterior.siguiente = nuevo
            actual.anterior = nuevo
            self.tamanio += 1

    def eliminar_inicio(self):
        if not self.cabeza:
            return None
        valor = self.cabeza.valor
        self.cabeza = self.cabeza.siguiente
        if self.cabeza:
            self.cabeza.anterior = None
        self.tamanio -= 1
        return valor

    def eliminar_final(self):
        if not self.cabeza:
            return None
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        valor = actual.valor
        if actual.anterior:
            actual.anterior.siguiente = None
        else:
            self.cabeza = None
        self.tamanio -= 1
        return valor

    def eliminar_posicion(self, posicion):
        if posicion < 0 or posicion >= self.tamanio:
            return None
        if posicion == 0:
            return self.eliminar_inicio()
        actual = self.cabeza
        for _ in range(posicion):
            actual = actual.siguiente
        if actual.anterior:
            actual.anterior.siguiente = actual.siguiente
        if actual.siguiente:
            actual.siguiente.anterior = actual.anterior
        self.tamanio -= 1
        return actual.valor

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

        dot = "digraph G {\n"
        dot += "  rankdir=LR;\n"
        dot += "  node [shape=record, style=filled, fillcolor=lightgray];\n"
        actual = self.cabeza
        i = 0
        while actual:
            dot += f'  nodo{i} [label="{actual.valor} | {id(actual)}"];\n'
            if actual.siguiente:
                dot += f'  nodo{i} -> nodo{i+1} [arrowhead=normal];\n'
                dot += f'  nodo{i+1} -> nodo{i} [arrowhead=vee, constraint=false];\n'
            actual = actual.siguiente
            i += 1
        dot += "}"
        return dot

