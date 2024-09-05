import tkinter as tk
from tkinter import ttk


# create a window
root = tk.Tk()
root.title('Place')
root.geometry('400x600+900+50')
root.attributes('-topmost', True)

# create widgets
label1 = ttk.Label(root, text='Label 1', background='#FF7777')
label2 = ttk.Label(root, text='Label 2', background='#7777FF')
label3 = ttk.Label(root, text='Label 3', background='#77FF77')
btn = ttk.Button(root, text='Button 1')

# layout
label1.place(x=300, y=100, width=100, height=200)
label2.place(relx=0.2, rely=0.1, relwidth=0.4, relheight=0.5)
label3.place(x=80, y=60, width=160, height=300)
btn.place(relx=1.0, rely=1.0, anchor='se')

# create frame
frame = ttk.Frame(root)
frame_label = ttk.Label(frame, text='Frame label', background='#FFFF77')
frame_button = ttk.Button(frame, text='Button')

# frame layout
frame.place(relx=0, rely=0, relwidth=0.3, relheight=1)
frame_label.place(relx=0, rely=0, relwidth=1, relheight=0.5)
frame_button.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)

# an exercise
exe_label = ttk.Label(root, text='EXE Label', background='#A8190B')
exe_label.place(relx=0.5, rely=0.5, anchor='center', height=200, relwidth=0.5)

# run
root.mainloop()
