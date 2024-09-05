import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title('Grid')
root.geometry('600x400+700+50')
root.attributes('-topmost', True)

# some widgets

label1 = ttk.Label(root, text='Label 1', background='#FF7777')
label2 = ttk.Label(root, text='Label 2', background='#7777FF')
label3 = ttk.Label(root, text='Label 3', background='#449044')
label4 = ttk.Label(root, text='Label 4', background='#FFFF89')

btn1 = ttk.Button(root, text='button 1')
btn2 = ttk.Button(root, text='button 2')

entry = ttk.Entry(root)

# define a grid
root.columnconfigure(0, weight=1, uniform='a')
root.columnconfigure(1, weight=1, uniform='a')
root.columnconfigure(2, weight=1, uniform='a')
root.columnconfigure(3, weight=2, uniform='a')

root.rowconfigure(0, weight=1, uniform='a')
root.rowconfigure(1, weight=1, uniform='a')
root.rowconfigure(2, weight=1, uniform='a')
root.rowconfigure(3, weight=3, uniform='a')

# place a widget
label1.grid(row=0, column=0, sticky='nsew')
label2.grid(row=1, column=1, rowspan=3, sticky='nsew')
label3.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky='nsew')
label4.grid(row=3, column=3, sticky='se')

btn1.grid(row=0, column=3, sticky='nsew')
btn2.grid(row=2, column=2, sticky='nsew', padx=5, pady=5)

entry.grid(row=3, column=3)

# run
root.mainloop()
