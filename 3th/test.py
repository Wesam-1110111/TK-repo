import tkinter as tk
from random import randint

def rand_n():
	return randint(0, 10)


print(f'this is a random number from 0 - 10: {rand_n()}')


# setups
root = tk.Tk()
root.title('Window')
root.geometry('400x300+700+50')

randvar = tk.IntVar(value=rand_n())

tk.Label(root, text='some text', textvariable=randvar).pack()


# run
root.mainloop()