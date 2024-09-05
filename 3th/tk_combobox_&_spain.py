import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.title('Combobox')
window.geometry('600x400')

values = ['Pizza', 'Burger', 'Death']
selected = tk.StringVar(value='Pizza')

combobox = ttk.Combobox(window, textvariable=selected, values=values)
combobox.pack()

label = ttk.Label(window, text=f'HI')
label.pack()

combobox.bind('<<ComboboxSelected>>', lambda event: label.config(text=f'Selected item: {selected.get()}'))

# Spinbox

spin = ttk.Spinbox(window, from_=1, to=10, increment=0.5)
spin.pack()

spin_var = tk.StringVar()

spin2 = ttk.Spinbox(window, values=['A', 'B', 'C', 'D', 'E'], textvariable=spin_var)
spin2.pack()

spin2.bind('<<Decrement>>', lambda event: print(spin_var.get()))

window.mainloop()
