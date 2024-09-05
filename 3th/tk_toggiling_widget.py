import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title('Hide widgets')
root.geometry('600x400+700+50')
root.attributes('-topmost', True)


# ***
def hide_display():
    global label_visible

    if label_visible:
        label.pack_forget()
        label_visible = False
    else:
        label.pack(expand=True)
        label_visible = True


# create some widgets
label = ttk.Label(root, text='Label')
button = ttk.Button(root, text='Toggle label', command=hide_display)

label_visible = True

# layout with place

# label.place(relx=0.5, rely=0.5, anchor='center')
# button.place(relx=0.5, rely=0.968, anchor='center')

# layout with pack
label.pack(expand=True)
button.pack(side='bottom')

# run
root.mainloop()
