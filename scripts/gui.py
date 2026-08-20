import FreeSimpleGUI as sg
from input_parser import Parser

class GUI:
	def __init__(self):
		self.window = self.create_window()
  
	def create_window(self):
		layout = [[sg.Text('Test')]]
		return sg.Window('Test', layout=layout, size=(800, 600))

	def run_game(self, parser, window):
		while True:
			event, values = window.read()

			if event == sg.WIN_CLOSED:
				break
		window.close()