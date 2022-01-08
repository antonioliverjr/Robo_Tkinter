from tkinter import * 
from tkinter import Tk, ttk
from config import Color


class GuiApp():
    def __init__(self):
        self.main = Tk()
        self.frame = ttk
        self.mainframe = self.frame.Frame(self.main, padding="150 100", borderwidth=2
        , relief=SOLID)
        self.initialize_gui()

    def initialize_gui(self):
        #self.main.geometry("500x500")
        self.main.title("Robo Tkinter")
        self.mainframe.grid(column=0, row=1, sticky=(N, W, E, S))
        self.frame.Label(self.mainframe, text="Teste de label"
        , background="black", foreground="white").grid(column=5, row=1, sticky=(W, E))
        self.frame.Button(self.mainframe, text="Clique Aqui").grid(column=5, row=3, sticky=S)
        
        self.l = self.frame.Label(self.mainframe, text="Starting...")
        self.l.grid()
        self.l.bind('<Enter>', lambda e: self.l.configure(text='Moved mouse inside'))
        self.l.bind('<Leave>', lambda e: self.l.configure(text='Moved mouse outside'))
        self.l.bind('<ButtonPress-1>', lambda e: self.l.configure(text='Clicked left mouse button'))
        self.l.bind('<3>', lambda e: self.l.configure(text='Clicked right mouse button'))
        self.l.bind('<Double-1>', lambda e: self.l.configure(text='Double clicked'))
        self.l.bind('<B3-Motion>', lambda e: self.l.configure(text='right button drag to %d,%d' % (e.x, e.y)))
