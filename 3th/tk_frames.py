import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title('Frames')
root.geometry('600x400')

frame = ttk.Frame(root, borderwidth=1, width=200, height=160, relief=tk.GROOVE)
frame.pack_propagate(False)
frame.pack()

btn = ttk.Button(frame, text='a button')
btn.pack()


root.mainloop()
