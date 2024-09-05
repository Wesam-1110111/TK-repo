import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext


root = tk.Tk()
root.title('Sliders')
root.geometry('600x400')

slider_var = tk.DoubleVar(value=20)

slider = ttk.Scale(
    root,
    length=250,
    orient='vertical',
    from_=0,
    to=50,
    variable=slider_var,
    command=lambda value: print(value)
)

progress = ttk.Progressbar(
    root,
    length=200,
    variable=slider_var,
    maximum=50
)
# progress.start(100)
slider.pack()
progress.pack()

scroll = scrolledtext.ScrolledText(root)
scroll.pack()

root.mainloop()
