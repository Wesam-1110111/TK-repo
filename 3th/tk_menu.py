import tkinter as tk
from tkinter import ttk


def create_window():

    # root
    root = tk.Tk()
    root.title('Menus')
    root.geometry('600x400')

    # menu
    home_menu = tk.Menu(root)

    # sub menus
    file_menu = tk.Menu(home_menu, tearoff=False)
    home_menu.add_cascade(label='File', menu=file_menu)

    # add options
    file_menu.add_command(label='New', command=lambda: print('new file'))
    file_menu.add_command(label='Open', command=lambda: print('Open file'))
    file_menu.add_separator()

    # more menu
    more_menu = tk.Menu(file_menu, tearoff=False)
    file_menu.add_cascade(label='More', menu=more_menu)
    more_menu.add_command(label='Hi', command=lambda: print('hi'))
    more_menu.add_command(label='Bye', command=lambda: print('bye'))

    # help menu
    help_menu = tk.Menu(home_menu, tearoff=False)
    help_menu.add_command(label='Help me', command=lambda: print('help me'))
    help_menu.add_checkbutton(label='Show')

    home_menu.add_cascade(label='Help', menu=help_menu)

    # button menu
    btn = ttk.Menubutton(root, text='Menu')
    btn.pack()

    # other menu
    last_menu = tk.Menu(btn, tearoff=False)
    last_menu.add_command(label='Some command', command=lambda: print('some'))
    last_menu.add_command(label='Other command', command=lambda: print('other'))

    btn.configure(menu=last_menu)

    # display menu
    root.configure(menu=home_menu)

    # run
    root.mainloop()


if __name__ == '__main__':
    create_window()
