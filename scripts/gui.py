import FreeSimpleGUI as sg
from input_parser import Parser

class GUI:
	def __init__(self):
		self.log = ''
		self.window = self.create_window()
  
	def create_window(self):
		layout = [
     						[sg.Push(), sg.Graph(canvas_size=(512, 256), graph_bottom_left=(0,0), graph_top_right=(512, 256), key='-DISPLAY-'), sg.Push()],
            			[sg.Text('', background_color='#222222', size=(100, 10), key='-OUTPUT-')],
               		[sg.Input(key='-IN-', size=(100, 1)), sg.Button('Submit', key='-SUBMIT-', size=(6,1))]
                 	]
		return sg.Window('Test', layout=layout, size=(800, 480), finalize=True)

	def run_game(self, parser, window):
		while True:
			event, values = window.read()
   
			if event == sg.WIN_CLOSED:
				break

			window['-DISPLAY-'].draw_image(filename='./assets/Sleeping Quarters.png', location=(0, 256))
			window['-DISPLAY-'].draw_image(filename='./assets/Underling.png', location=(256-64, 256))	
 
			self.log += '> ' + values['-IN-'] + '\n'
 
			window['-OUTPUT-'].update(self.log)
		window.close()