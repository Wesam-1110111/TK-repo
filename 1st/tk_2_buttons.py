from tkinter import *

window = Tk()


def click():
    Label(window, text="The button was clicked!").pack()


Button(window, text="Click me", command=click).pack()

window.mainloop()
