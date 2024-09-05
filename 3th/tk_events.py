import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk


def event_root(event):
    root.quit()


root = ttk.Window(themename='darkly')
root.title('Tkinter events')
root.geometry('600x500')
root.minsize(300, 200)


text = tk.Text(root)
text.pack()

entry = ttk.Entry(root)
entry.pack()

button = ttk.Button(root, text='button')
button.pack()

label = ttk.Label(root, text='Press q to quit')
label.pack()

com_var = tk.StringVar(value='Libya')


# events

# text.bind('<Motion>', lambda event: print(f'x: {event.x}, y: {event.y}'))

root.bind('<KeyPress-q>', event_root)
text.bind('<Shift-MouseWheel>', lambda event: print(f'MouseWheel'))


root.mainloop()
