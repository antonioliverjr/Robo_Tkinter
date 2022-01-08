from tkinter import *


class GuiApp:
    
    def __init__(self) -> None:
        self.janela = Tk()
        self._title = ''

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, titulo:str):
        if not isinstance(titulo, (str)):
            raise ValueError("Informe uma string!")
        self._title = titulo

    def iniciar(self, titulo:str):
        self.title = titulo
        self.janela.title(self._title)
        return self.janela.mainloop()