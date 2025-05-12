import os
import tempfile
import graphviz
import webbrowser

class Visualizador:
    def mostrar(self, dot_source):
        temp_dir = tempfile.gettempdir()
        file_path = os.path.join(temp_dir, "estructura_renderizada")
        dot = graphviz.Source(dot_source)
        dot.render(file_path, format="png", cleanup=True)  # <- Esto es lo que faltaba
        webbrowser.open(f"{file_path}.png")

