import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title('Layout')
root.geometry('600x400')

label1 = ttk.Label(root, text='Label 1', background='#FF8998')
label2 = ttk.Label(root, text='Label 2', background='#4898FF')

# pack
# label1.pack(side='top', expand=True, fill='both')
# label2.pack(side='bottom', expand=True, fill='both')

# grid
# root.rowconfigure(0, weight=1)
# root.rowconfigure(1, weight=1)
# root.rowconfigure(2, weight=2)
# root.columnconfigure(0, weight=1)
# root.columnconfigure(1, weight=2)
# root.columnconfigure(2, weight=1)
# label1.grid(row=0, column=1, columnspan=2 , sticky='nsew')
# label2.grid(row=1, column=1, rowspan=2, sticky='nsew')

# place
label1.place(x=300, y=200, width=350, height=100, anchor='se')
label2.place(relx=0.55, rely=0.55, relwidth=50, anchor='nw')

# run
root.mainloop()
