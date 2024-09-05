import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title('Layout')
root.geometry('400x600+1500+50')


label1 = ttk.Label(root, text='a Label 1', background='#FF8998')
label2 = ttk.Label(root, text='It is just a label 2', background='#4898FF')
label3 = ttk.Label(root, text='Just a Label 3', background='#239923')
button = ttk.Button(root, text='Button')

# pack
label1.pack(expand=True, fill='both', side='top', padx=10, pady=10)
label2.pack(expand=True, side='left', fill='both')
label3.pack(expand=True, fill='both', side='top')
button.pack(expand=True, fill='both', side='top')

# run
root.mainloop()
