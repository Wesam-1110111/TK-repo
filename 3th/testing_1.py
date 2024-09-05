import tkinter as tk
from tkinter import ttk


USER = 'admin'
times = 3


def reset():
    global times
    times = 3
    entry['state'] = 'enabled'
    btn['state'] = 'enabled'
    mass['text'] = ''
    reset_btn.forget()


def check():
    global times

    if times == 0 and entry.get() != USER:
        entry['state'] = 'disabled'
        btn['state'] = 'disabled'
        reset_btn.pack()

    if entry.get() == USER:
        # mass.config(text='Welcome back')
        mass['text'] = 'Wesam is here!'
    else:
        mass.config(text=f'user name is not correct\nyou have ({times}) other tries')
        times -= 1
    mass.pack()


if __name__ == '__main__':

    root = tk.Tk()
    root.title('testing setting and getting')
    # root.geometry('500x300')
    root.minsize(300, 150)

    frame = ttk.Frame(root)
    frame.pack(pady=15)

    label = ttk.Label(frame, text='User:')
    label.pack(side='left')

    entry = ttk.Entry(frame)
    entry.pack(side='left', padx=10)

    btn = ttk.Button(root, text='Log in', command=check)
    btn.pack()

    reset_btn = ttk.Button(root, text='Reset', command=reset)

    mass = (ttk.Label(root, text=''))

    root.mainloop()
