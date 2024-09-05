import tkinter as tk
from tkinter import ttk
# import ttkbootstrap as ttk


root = tk.Tk()
root.title("Tkinter variables")
root.minsize(300, 150)

txt = tk.StringVar(value='test')

label = ttk.Label(root, textvariable=txt)
label.pack()

entry = ttk.Entry(root, textvariable=txt)
entry.pack()

btn = ttk.Button(root, text='button')
btn.pack()


root.mainloop()
