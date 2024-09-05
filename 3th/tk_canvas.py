import tkinter as tk


root = tk.Tk()
root.title('Canvas')
root.geometry('600x400')

# Canvas

canvas = tk.Canvas(root, bg='white', width=1600, height=1400)
canvas.pack()


# canvas.bind('<Motion>', lambda event: canvas.create_line((0, 0, event.x, event.y)))


canvas.create_line((300, 0, 300, 400))
canvas.create_line((0, 200, 600, 200))

canvas.create_rectangle((150, 100, 450, 300))
canvas.create_oval((150, 100, 450, 300))
canvas.create_oval((200, 150, 400, 250))

canvas.create_polygon((300, 200, 200, 100, 400, 100))
canvas.create_polygon((300, 200, 200, 300, 400, 300))
root.bind('<KeyPress-c>', lambda event: canvas.delete('all'))


def draw(event):
    x = event.x
    y = event.y
    canvas.create_oval((x - size / 2, y - size / 2, x + size / 2, y + size / 2), fill='black')


size = 4


def draw_size(event):
    global size
    if event.delta > 0:
        size += 4
    else:
        size -= 4
    size = max(0, min(size, 50))


canvas.bind('<Motion>', draw)
canvas.bind('<MouseWheel>', draw_size)

# canvas.clipboard_clear()
# canvas.clipboard_clear()


root.mainloop()
