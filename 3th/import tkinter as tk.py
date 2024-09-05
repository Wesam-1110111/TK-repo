import tkinter as tk
from tkinter import ttk


class App(tk.Tk):

	def __init__(self, title, size = (300, 300)):
		# window setups
		super().__init__()
		self.title(title)
		self.geometry(f'{size[0]}x{size[1]}+700+50')
		self.minsize(size[0], size[1])
		self.attributes('-topmost', True)
		self.bind('<c>', lambda event: self.quit())

		# frame
		self.frame = ttk.Frame(self)

		self.frame.pack(expand=True, fill='both')
		
		self.small_widgets()
		# self.after(5000, self.meduim_widgets())
		s = SizeNot(self, {600: self.meduim_widgets, 300: self.small_widgets, 1200: self.large_widgets})
		# s.check_width()
		# run
		self.mainloop()

	def small_widgets(self):
		
		self.frame.pack_forget()
		self.frame = ttk.Frame(self)

		ttk.Label(self.frame, text='Label 1', background='#4747FF').pack(expand=True, fill='both', pady=10, padx=10)
		ttk.Label(self.frame, text='Label 2', background='#FF4747').pack(expand=True, fill='both', pady=10, padx=10)
		ttk.Label(self.frame, text='Label 3', background='#47FF47').pack(expand=True, fill='both', pady=10, padx=10)
		ttk.Label(self.frame, text='Label 4', background='#FFFF47').pack(expand=True, fill='both', pady=10, padx=10)
		
		self.frame.pack(expand=True, fill='both')


	def meduim_widgets(self):
		
		self.frame.pack_forget()
		self.frame = ttk.Frame(self)
		self.frame.rowconfigure((0, 1), weight = 1, uniform='a')
		self.frame.columnconfigure((0, 1), weight = 1, uniform='a')
		self.frame.pack(expand=True, fill='both')

		ttk.Label(self.frame, text='Label 1', background='#4747FF').grid(row=0, column=0, sticky='nwes', pady=10, padx=10)
		ttk.Label(self.frame, text='Label 2', background='#FF4747').grid(row=0, column=1, sticky='nwes', pady=10, padx=10)
		ttk.Label(self.frame, text='Label 3', background='#47FF47').grid(row=1, column=0, sticky='nwes', pady=10, padx=10)
		ttk.Label(self.frame, text='Label 4', background='#FFFF47').grid(row=1, column=1, sticky='nwes', pady=10, padx=10)


	
	def large_widgets(self):
		print('LAAARRRGGGGEEE')
		self.frame.pack_forget()
		self.frame = ttk.Frame(self)
		self.frame.rowconfigure(0, weight=1, uniform='a')
		self.frame.columnconfigure((0, 1, 2, 3), weight=1, uniform='a')
		self.frame.pack(expand=True, fill='both')

		ttk.Label(self.frame, text='Label 1', background='#4747FF').grid(row=0, column=0, sticky='nwes', padx=10)
		ttk.Label(self.frame, text='Label 2', background='#47FF47').grid(row=0, column=1, sticky='nwes', padx=10)
		ttk.Label(self.frame, text='Label 3', background='#FF4747').grid(row=0, column=2, sticky='nwes', padx=10)
		ttk.Label(self.frame, text='Label 4', background='#FFFF47').grid(row=0, column=3, sticky='nwes', padx=10)


class SizeNot:
	def __init__(self, window, size):
		self.window = window
		self.size = {key: value for key, value in sorted(size.items())}
		self.current_min_size = None
		self.window.bind('<Configure>', self.check_size)

		self.window.update()

		min_height = self.window.winfo_height()
		min_width = list(self.size)[0]
		


	def check_size(self, event):
		if event.widget == self.window:
			window_width = event.width
			checked_size = None

			for min_size in self.size:
				delta = window_width - min_size
				if delta >= 0:
					checked_size = min_size
			if checked_size != self.current_min_size:
				self.current_min_size = checked_size
				self.size[self.current_min_size]()

		# print(event)
		# if event.width < 600:
		# 	self.size[300]()
		# elif 1200 > event.width >= 600:
		# 	self.size[600]()
		# else:
		# 	self.size[1200]() 




# **********
if __name__ == '__main__':
	App(title='Responsive layouts', size=(400, 300))
