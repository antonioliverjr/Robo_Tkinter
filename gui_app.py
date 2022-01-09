from tkinter import * 
from tkinter import Tk, ttk
from config import Color


class GuiApp():
    def __init__(self):
        self.main = Tk()
        self.main['bg'] = Color.BACKGROUND_BG.value
        self.main.geometry("550x330+200+200")
        self.main.resizable(False, False)
        self.main.iconbitmap(default="etl.ico")
        self.main.title("Robo Tkinter")
        self.mainframe = ttk.Frame(self.main, padding="3 3 12 12", borderwidth=2
        , relief=SOLID)
        self.style = ttk.Style()
        self.style.theme_use('alt')
        self.style.configure('TButton', background=Color.FONTE_TEXT.value, foreground=Color.BACKGROUND_IT.value)
        self.style.map('TButton', foreground=[('active', Color.FONTE_TEXT.value)])

        ''' Objetos da janela '''
        self.titulo = ttk.Label(self.main, text="Importação de Produtos Adventure x Commerce",
        background=Color.BACKGROUND_IT.value, foreground=Color.FONTE_TEXT.value, padding=5,
        font="Times 16 bold", width=46, anchor=CENTER)
        self.console = Listbox(self.main, background="white",
         foreground=Color.FONTE_TEXT.value, font="Arial 12 italic", width=50)
        self.barray = ttk.Scrollbar(self.main, orient=VERTICAL, command=self.console.yview)
        self.console.configure(yscrollcommand=self.barray.set)
        self.iniciar = ttk.Button(self.main, text="Iniciar")
        self.__total_registros_label = ttk.Label(self.main, text="Total de Registros:", foreground=Color.FONTE_TEXT.value, 
        background=Color.BACKGROUND_BG.value, anchor=CENTER)
        self.total_registros = ttk.Label(self.main, background=Color.BACKGROUND_IT.value, anchor=CENTER)
        self.__data_importacao_label = ttk.Label(self.main, text="Data Ultima Importação:", foreground=Color.FONTE_TEXT.value, 
        background=Color.BACKGROUND_BG.value, anchor=CENTER)
        self.data_importacao = ttk.Label(self.main, background=Color.BACKGROUND_IT.value, anchor=CENTER)
        
        ''' Distruição dos objetos na janela '''
        self.titulo.grid(row=0, columnspan=6, sticky=(N, S, W, E), padx=10, pady=10)
        self.console.grid(row=1, columnspan=5, sticky=(N,W), padx=10, pady=10)
        self.barray.grid(row=1, column=5, pady=10, sticky=(N,S,W))
        self.__total_registros_label.grid(row=2, column=0, ipadx=2, ipady=2, pady=3)
        self.total_registros.grid(row=2, column=1, ipadx=3, ipady=3, pady=3)
        self.__data_importacao_label.grid(row=2, column=2, ipadx=2, ipady=2, pady=3)
        self.data_importacao.grid(row=2, column=3, ipadx=3, ipady=3, pady=3)
        self.iniciar.grid(row=2, column=4, columnspan=2, padx=3, pady=3, ipadx=3,sticky=(N, S, W, E))



