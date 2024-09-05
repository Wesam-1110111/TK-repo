import tkinter as tk
from tkinter import ttk
from random import randint,choice



root = tk.Tk()
root.title('Scroll Bar')
root.geometry('400x300')


canvas = tk.Canvas(root, bg='#FFFFFF', scrollregion=(0,0,2000,5000))
canvas.pack(expand=True, fill='both')

canvas.create_line(0,0,2000,5000, fill='#000000', width=5)
for i in range(100):
	l = randint(0, 2000)
	t = randint(0, 5000)
	r = l + randint(0, 500)
	b = t + randint(0, 500)
	color = choice(('#FF4747', '#47FF47', '#4747FF', '#F407F4', '#d401a2'))
	canvas.create_rectangle(l,t,r,b, fill=color)

# ^
# | scrollbar
# V
scrollbar = ttk.Scrollbar(root, command= canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')

canvas.bind('<MouseWheel>', lambda event: canvas.yview_scroll(-int(event.delta / 60), 'units'))


# <---> scrollbar
h_scrollbar = ttk.Scrollbar(root, orient='horizontal', command=canvas.xview)
h_scrollbar.place(relx=0, rely=1, relwidth=1, anchor='sw')
canvas.configure(xscrollcommand=h_scrollbar.set)
canvas.bind('<Control-MouseWheel>', lambda event: canvas.xview_scroll(-int(event.delta / 60), 'units'))

root.mainloop()