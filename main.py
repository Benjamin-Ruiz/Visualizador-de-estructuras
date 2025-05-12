
import tkinter as tk
from tkinter import ttk, messagebox
from estructuras.pila import Pila
from estructuras.cola import Cola
from estructuras.lista_simple import ListaSimple
from estructuras.lista_circular import ListaCircular
from estructuras.lista_doble import ListaDoble
from estructuras.arbol_binario import ArbolBinario
from estructuras.arbol_busqueda import ABB
from visual.visualizador import Visualizador

class AppEstructuras:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualizador de Estructuras de Datos")
        self.root.geometry("900x650")

        self.estructura = None
        self.tipo_dato = tk.StringVar(value="int")
        self.visualizador = Visualizador()

        self._crear_widgets()

    def _crear_widgets(self):
        frame_top = tk.Frame(self.root)
        frame_top.pack(pady=10)

        tk.Label(frame_top, text="Estructura:").pack(side=tk.LEFT, padx=5)
        self.combo_estructura = ttk.Combobox(frame_top, values=[
            "Pila", "Cola", "ListaSimple", "ListaCircular", "ListaDoble", "ArbolBinario", "ABB"
        ], state="readonly")
        self.combo_estructura.current(0)
        self.combo_estructura.pack(side=tk.LEFT)

        tk.Label(frame_top, text="Tipo de Dato:").pack(side=tk.LEFT, padx=5)
        self.combo_tipo = ttk.Combobox(frame_top, values=["int", "float", "bool", "str"], state="readonly")
        self.combo_tipo.current(0)
        self.combo_tipo.pack(side=tk.LEFT)

        tk.Button(frame_top, text="Crear", command=self.crear_estructura).pack(side=tk.LEFT, padx=10)

        self.frame_ops = tk.Frame(self.root)
        self.frame_ops.pack(pady=10)

        self.entry_valor = tk.Entry(self.frame_ops)
        self.entry_valor.pack(side=tk.LEFT)

        self.boton_insertar = tk.Button(self.frame_ops, text="Insertar", command=self.insertar)
        self.boton_insertar.pack(side=tk.LEFT, padx=5)

        self.boton_eliminar = tk.Button(self.frame_ops, text="Eliminar", command=self.eliminar)
        self.boton_eliminar.pack(side=tk.LEFT, padx=5)

        self.boton_buscar = tk.Button(self.frame_ops, text="Buscar", command=self.buscar)
        self.boton_buscar.pack(side=tk.LEFT, padx=5)

        self.boton_rotar_izq = tk.Button(self.frame_ops, text="Rotar ⬅", command=self.rotar_izq)
        self.boton_rotar_der = tk.Button(self.frame_ops, text="Rotar ➡", command=self.rotar_der)
        self.boton_rotar_izq.pack(side=tk.LEFT, padx=5)
        self.boton_rotar_der.pack(side=tk.LEFT, padx=5)

        self.text_info = tk.Text(self.root, height=10, state="normal")
        self.text_info.pack(fill=tk.X, padx=10)

        tk.Button(self.root, text="Visualizar", command=self.visualizar).pack(pady=10)

    def crear_estructura(self):
        tipo = self.combo_tipo.get()
        nombre = self.combo_estructura.get()
        if nombre == "Pila":
            self.estructura = Pila(tipo)
        elif nombre == "Cola":
            self.estructura = Cola(tipo)
        elif nombre == "ListaSimple":
            self.estructura = ListaSimple(tipo)
        elif nombre == "ListaCircular":
            self.estructura = ListaCircular(tipo)
        elif nombre == "ListaDoble":
            self.estructura = ListaDoble(tipo)
        elif nombre == "ArbolBinario":
            self.estructura = ArbolBinario(tipo)
        elif nombre == "ABB":
            self.estructura = ABB(tipo)

        self.actualizar_info()

    def insertar(self):
        valor = self._obtener_valor()
        if valor is not None:
            if hasattr(self.estructura, 'insertar'):
                self.estructura.insertar(valor)
            elif hasattr(self.estructura, 'insertar_inicio'):
                self.estructura.insertar_final(valor)
            self.actualizar_info()

    def eliminar(self):
        if hasattr(self.estructura, 'eliminar'):
            resultado = self.estructura.eliminar()
        elif hasattr(self.estructura, 'eliminar_inicio'):
            resultado = self.estructura.eliminar_inicio()
        else:
            resultado = "No se puede eliminar"
        messagebox.showinfo("Eliminar", f"Resultado: {resultado}")
        self.actualizar_info()

    def buscar(self):
        valor = self._obtener_valor()
        if valor is not None:
            resultado = self.estructura.buscar(valor)
            messagebox.showinfo("Buscar", f"Resultado: {resultado}")

    def rotar_izq(self):
        if hasattr(self.estructura, 'rotar_izquierda'):
            self.estructura.rotar_izquierda()
            self.actualizar_info()

    def rotar_der(self):
        if hasattr(self.estructura, 'rotar_derecha'):
            self.estructura.rotar_derecha()
            self.actualizar_info()

    def visualizar(self):
        if self.estructura:
            dot = self.estructura.get_visual_info()
            self.visualizador.mostrar(dot)
            print(dot)


    def actualizar_info(self):
        self.text_info.config(state="normal")
        self.text_info.delete("1.0", tk.END)
        self.text_info.insert(tk.END, self.estructura.get_info())
        self.text_info.config(state="disabled")

    def _obtener_valor(self):
        valor_str = self.entry_valor.get()
        if not self.estructura:
            messagebox.showerror("Error", "Primero creá una estructura.")
            return None

        tipo = getattr(self.estructura, 'tipo', 'str')
        try:
            if tipo == "int":
                return int(valor_str)
            elif tipo == "float":
                return float(valor_str)
            elif tipo == "bool":
                return valor_str.lower() == "true"
            elif tipo == "str":
                return valor_str
        except ValueError:
            messagebox.showerror("Error", "Valor inválido para el tipo seleccionado")
            return None


if __name__ == "__main__":
    root = tk.Tk()
    app = AppEstructuras(root)
    root.mainloop()
