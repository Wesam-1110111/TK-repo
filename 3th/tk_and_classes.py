import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self, title='tk', size=(300, 150)):

        # main setups
        super().__init__()
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0], size[1])

        # widgets
        Menu(self)

        # run
        self.mainloop()


class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)



#
if __name__ == '__main__':
    App('Class based app', (1000, 600))
    # Menu(App)
