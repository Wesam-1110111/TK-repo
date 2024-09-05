import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title('Stacking order')
root.geometry('400x400+800+50')
root.attributes('-topmost', True)

# widgets
label1 = ttk.Label(root, text='Label 1', background='#44FF44')
label2 = ttk.Label(root, text='Label 2', background='#FF4444')
label3 = ttk.Label(root, text='Label 3', background='#4444FF')


button1 = ttk.Button(root, text='raise label 1', command=lambda: label1.lift())
button2 = ttk.Button(root, text='raise label 2', command=lambda: label2.tkraise())
button3 = ttk.Button(root, text='raise label 3', command=lambda: label3.tkraise())


# layout
label1.place(relx=0.2, rely=0.3, width=200, height=150)
label2.place(relx=0.38, rely=0.25, width=140, height=100)
label3.place(relx=0.32, rely=0.42, width=180, height=120)


button1.place(relx=0.8, rely=1, anchor='se')
button2.place(relx=1, rely=1, anchor='se')
button3.place(relx=0.6, rely=1, anchor='se')


# run
root.mainloop()
