import tkinter as tk
from tkinter import ttk


class App(tk.Tk):

	def __init__(self, title: str = 'App', size: (int, int) = (300, 300)):
		
		super().__init__()
		
		# window setups
		self.title(title)
		self.geometry(f'{size[0]}x{size[1]}+800+50')
		self.minsize(size[0], size[1])

		# widgets
		first = Unit(self, 'label', 'button')
		sec2 = Unit(self, 'test', 'click')
		th3 = Unit(self, 'hello', 'test')
		th4 = Unit(self, 'bye', 'Go')
		th5 = Unit(self, 'last one', 'exit')


		# run
		self.mainloop()


class Unit(ttk.Frame):

	def __init__(self, master, label_text, button_text):

		super().__init__(master)

		# rows and columns
		self.columnconfigure((0, 1, 2), weight=1, uniform='a')
		self.rowconfigure(0, weight=1, uniform='a')

		# create widgets
		ttk.Label(self, text=label_text).grid(row=0, column=0, sticky='nsew')
		ttk.Button(self, text=button_text).grid(row=0, column=1, sticky='nsew')
		self.create_some_widgets().grid(row=0, column=2, sticky='nsew', padx=5)
		self.pack(padx=10, pady=10, expand=True, fill='both')


	def create_some_widgets(self):
		frame = ttk.Frame(self)

		ttk.Entry(frame).pack(expand=True, fill='both')
		ttk.Button(frame, text='button').pack(expand=True, fill='both')

		return frame


if __name__ == '__main__':
	root = App('Tk with Classes and Functions', (400, 600))
	# frame_k = create_some_widgets(root)
	# frame_k.pack(side='left', expand=True, fill='both')
