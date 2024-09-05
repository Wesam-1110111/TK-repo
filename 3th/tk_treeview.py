import tkinter as tk
from tkinter import ttk
from random import choice


root = tk.Tk()
root.title('Tree view')
root.geometry('600x450')

# data
first_names = ['Bob', 'Maria', 'Alex', 'Yassmen', 'Wesam', 'Ahmed', 'Salem']
last_names = ['Smith', 'Brown', 'Wilson', 'Ali', 'Shokry', 'Test', 'Mohammed']

# tree view
table = ttk.Treeview(root, columns=('first', 'last', 'email'), show='headings')
table.heading('first', text='First name')
table.heading('last', text='Last name')
table.heading('email', text='Email')


for i in range(100):
    first = choice(first_names)
    last = choice(last_names)
    email = f'{first}{last}@gmail.com'
    data = (first, last, email)
    table.insert(parent='', index=0, values=data)
    # table.insert(parent='', index=i, text=last)


table.pack(fill='both', expand=True)

table.insert('', index=tk.END, values=('xxxx', 'yyyy', 'zzzz'))


def print_item(_):
    print(table.selection())
    for item in table.selection():
        print(table.item(item)['values'])


def delete_item(_):
    table.delete(table.selection())


table.bind('<<TreeviewSelect>>', print_item)
table.bind('<Delete>', delete_item)

root.mainloop()
