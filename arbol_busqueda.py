
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ABB:
    def __init__(self, tipo):
        self.raiz = None
        self.tipo = tipo
        self.tamanio = 0

    def insertar(self, valor):
        if not self.raiz:
            self.raiz = Nodo(valor)
        else:
            self._insertar_rec(self.raiz, valor)
        self.tamanio += 1

    def _insertar_rec(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda:
                self._insertar_rec(nodo.izquierda, valor)
            else:
                nodo.izquierda = Nodo(valor)
        else:
            if nodo.derecha:
                self._insertar_rec(nodo.derecha, valor)
            else:
                nodo.derecha = Nodo(valor)

    def buscar(self, valor):
        return self._buscar(self.raiz, valor)

    def _buscar(self, nodo, valor):
        if not nodo:
            return False
        if nodo.valor == valor:
            return True
        if valor < nodo.valor:
            return self._buscar(nodo.izquierda, valor)
        else:
            return self._buscar(nodo.derecha, valor)

    def eliminar(self, valor):
        self.raiz, eliminado = self._eliminar(self.raiz, valor)
        if eliminado:
            self.tamanio -= 1
        return eliminado

    def _eliminar(self, nodo, valor):
        if not nodo:
            return nodo, False
        if valor < nodo.valor:
            nodo.izquierda, eliminado = self._eliminar(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha, eliminado = self._eliminar(nodo.derecha, valor)
        else:
            if not nodo.izquierda:
                return nodo.derecha, True
            elif not nodo.derecha:
                return nodo.izquierda, True
            temp = self._min_value_node(nodo.derecha)
            nodo.valor = temp.valor
            nodo.derecha, _ = self._eliminar(nodo.derecha, temp.valor)
            return nodo, True
        return nodo, eliminado

    def _min_value_node(self, nodo):
        actual = nodo
        while actual.izquierda:
            actual = actual.izquierda
        return actual

    def get_info(self):
        return f"Tipo de dato: {self.tipo}\nTamaño: {self.tamanio}\nAltura: {self.altura(self.raiz)}\nRaíz: {self.raiz.valor if self.raiz else 'Ninguna'}"

    def altura(self, nodo):
        if not nodo:
            return 0
        return 1 + max(self.altura(nodo.izquierda), self.altura(nodo.derecha))

    def get_visual_info(self):
        dot = "digraph G {\n"
        dot += "  node [shape=record];\n"
        dot += self._generar_dot(self.raiz, "nodo0")
        dot += "}"
        return dot


    def _generar_dot(self, nodo, nombre):
        if nodo is None:
            return ""
        
        dot = f'  {nombre} [label="{nodo.valor} | {id(nodo)}"];\n'

        if nodo.izquierda:
            hijo_izq = f"{nombre}i"
            dot += f"  {nombre} -> {hijo_izq};\n"
            dot += self._generar_dot(nodo.izquierda, hijo_izq)

        if nodo.derecha:
            hijo_der = f"{nombre}d"
            dot += f"  {nombre} -> {hijo_der};\n"
            dot += self._generar_dot(nodo.derecha, hijo_der)

        return dot
