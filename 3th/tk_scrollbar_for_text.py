import tkinter as tk
from tkinter import ttk



# setups
root = tk.Tk()
root.title('Scrollbar 2')
root.geometry('400x300')

# widgets
text = tk.Text(root)
for i in range(100):
	# text.config(value=f'{i}\n')
	text.insert(f'{i}.0', f'text: {i}\n')
text.pack(expand=True, fill='both')

scrollbar = ttk.Scrollbar(root, command=text.yview)
text.configure(yscrollcommand=scrollbar.set)
scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')

# run
root.mainloop()