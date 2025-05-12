class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Pila:
    def __init__(self, tipo):
        self.tope = None
        self.tamanio = 0
        self.tipo = tipo

    def insertar(self, valor):
        nuevo = Nodo(valor)
        nuevo.siguiente = self.tope
        self.tope = nuevo
        self.tamanio += 1

    def eliminar(self):
        if self.tope is None:
            return None
        valor = self.tope.valor
        self.tope = self.tope.siguiente
        self.tamanio -= 1
        return valor

    def buscar(self, valor):
        actual = self.tope
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False

    def get_info(self):
        info = f"Tipo de dato: {self.tipo}\nTamaño: {self.tamanio}\n"

        actual = self.tope
        i = 0
        while actual:
            info += f"[{i}] Valor: {actual.valor}, Dirección: {id(actual)}\n"
            actual = actual.siguiente
            i += 1
        return info
    
    def get_visual_info(self):
        dot = "digraph G {\n"
        dot += "  rankdir=TB;\n"
        dot += "  node [shape=record];\n"
        actual = self.tope
        i = 0
        while actual:
            dot += f'  nodo{i} [label="{actual.valor} | {id(actual)}"];\n'
            if actual.siguiente:
                dot += f"  nodo{i} -> nodo{i+1};\n"
            actual = actual.siguiente
            i += 1
        dot += "}"
        return dot

