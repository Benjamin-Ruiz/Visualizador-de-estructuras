
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self, tipo):
        self.raiz = None
        self.tipo = tipo
        self.tamanio = 0

    def insertar(self, valor):
        nuevo = Nodo(valor)

        if self.raiz is None:
            self.raiz = nuevo
            return

        cola = [self.raiz]
        while cola:
            actual = cola.pop(0)
            if actual.izquierda is None:
                actual.izquierda = nuevo
                return
            elif actual.derecha is None:
                actual.derecha = nuevo
                return
            else:
                cola.append(actual.izquierda)
                cola.append(actual.derecha)



    def buscar(self, valor):
        return self._buscar(self.raiz, valor)

    def _buscar(self, nodo, valor):
        if not nodo:
            return False
        if nodo.valor == valor:
            return True
        return self._buscar(nodo.izquierda, valor) or self._buscar(nodo.derecha, valor)

    def eliminar(self, valor):
        self.raiz, eliminado = self._eliminar(self.raiz, valor)
        if eliminado:
            self.tamanio -= 1
        return eliminado

    def _eliminar(self, nodo, valor):
        if not nodo:
            return nodo, False
        if nodo.valor == valor:
            if not nodo.izquierda and not nodo.derecha:
                return None, True
            if not nodo.izquierda:
                return nodo.derecha, True
            if not nodo.derecha:
                return nodo.izquierda, True
       
            sucesor = self._min_value_node(nodo.derecha)
            nodo.valor = sucesor.valor
            nodo.derecha, _ = self._eliminar(nodo.derecha, sucesor.valor)
            return nodo, True
        elif valor < nodo.valor:
            nodo.izquierda, eliminado = self._eliminar(nodo.izquierda, valor)
        else:
            nodo.derecha, eliminado = self._eliminar(nodo.derecha, valor)
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

