import tkinter as tk
from tkinter import ttk

"""

	in this project i used in first time, 
	sublime text with Python, and it's 
	so light and doesn't use a big of RAM,
	and CPU, it's just perfect.

	-->Typo: in line 9 "perfect"


"""



class App(tk.Tk):
	
  def __init__(self, title: str = 'tk', size: (int, int) = (300, 300)):
		super().__init__()

		# window setups
		self.title(title)
		self.geometry(f'{size[0]}x{size[1]}+750+50')
		self.minsize(size[0], size[1])
		self.attributes('-topmost', True)

		# menu frame
		self.menu = Menu(self)

		# main frame
		self.main = Main(self)

		# run
		self.mainloop()


"""

	Main class

"""

class Main(ttk.Frame):

	def __init__(self, pa):
		super().__init__(pa)
		self.place(relx=0.3, rely=0, relwidth=0.7, relheight=1)
		

		self.left_frame = SubFrame(self, '#4747FF', l_text='Left label', b_text='Left Button')
		self.right_frame = SubFrame(self , '#FF4747', l_text='Right label', b_text='Right Button')
		# SubFrame(self , '#FF4747', l_text='Right label', b_text='Right Button')
		




# submain frames

class SubFrame(ttk.Frame):

	def __init__(self, pa, color, l_text, b_text):
		super().__init__(pa)


		ttk.Label(self, text=l_text, background=color).pack(expand=True, fill='both', pady=10)
		ttk.Button(self, text=b_text).pack(expand=True, fill='both', pady=10)

		self.pack(side='left', expand=True, fill='both', pady=15, padx=15)
	


"""

   Menu class
     it's just a frame,
     on the left of the window,
     and there some buttons and other widgets in it.

"""

class Menu(ttk.Frame):

	def __init__(self, pa):

		super().__init__(pa)
		self.place(x=0, y=0, relwidth=0.3, relheight=1)
		self.create_widgets()


	def rows_and_columns(self):
		self.columnconfigure((0, 1, 2), weight=1, uniform='a')
		self.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform='a')


	def create_widgets(self):
		self.rows_and_columns()
		self.btns = [
			ttk.Button(self, text='Button 1'),
			ttk.Button(self, text='Button 2'),
			ttk.Button(self, text='Button 3')
		]

		self.slider = [
			ttk.Scale(self, to=10, orient='vertical'),
			ttk.Scale(self, to=10, orient='vertical')
		]

		self.frame = ttk.Frame(self)

		checkbox_var = tk.StringVar()

		# check1 = ttk.Checkbutton(frame, text='Yes', onvalue='ON', offvalue='OFF', variable=checkbox_var)
		# check2 = ttk.Checkbutton(frame, text='No', onvalue='OFF', offvalue='ON', variable=checkbox_var)

		
		self.checkbox = [
			ttk.Checkbutton(self.frame, text='Yes', onvalue='ON', offvalue='OFF', variable=checkbox_var),
			ttk.Checkbutton(self.frame, text='No', onvalue='OFF', offvalue='ON', variable=checkbox_var)
		]
		
		self.entry = ttk.Entry(self)

		self.widget_layout()


	#///

	def widget_layout(self):


		# display the fucking widgets
		self.btns[0].grid(row=0, column=0, columnspan=2, sticky='nsew')
		self.btns[1].grid(row=0, column=2, sticky='nsew')
		self.btns[2].grid(row=1, column=0, columnspan=3, sticky='nsew')

		self.slider[0].grid(row=2, column=0, rowspan=2, sticky='nsew', pady=10)
		self.slider[1].grid(row=2, column=2, rowspan=2, sticky='nsew', pady=10)

		self.frame.grid(row=4, column=0, columnspan=3, sticky='ew')

		self.checkbox[0].pack(side='left', expand=True)
		self.checkbox[1].pack(side='left', expand=True)
		# check1.pack(side='left', expand=True)
		# check2.pack(side='left', expand=True)

		self.entry.place(relx=0.5, rely=0.95, relwidth=0.9, anchor='center')






"""

	the main

"""

if __name__ == '__main__':
	root = App(title='Tk with Classes', size=(600, 600))

