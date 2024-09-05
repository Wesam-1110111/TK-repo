import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title('Tabs')
root.geometry('600x400')

# the notebook
notebook = ttk.Notebook(root)

# the tab 1
tab1 = ttk.Frame(notebook)
# frame = ttk.Frame(tab1)
# frame.pack()
label = ttk.Label(tab1, text='Log in')
label.pack()

# the tab 2
tab2 = ttk.Frame(notebook)


notebook.add(tab1, text='Log in')
notebook.add(tab2, text='Sign in')

notebook.pack()

root.mainloop()
