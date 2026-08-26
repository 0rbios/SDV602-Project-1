import FreeSimpleGUI as sg
from input_parser import Parser

class GUI:
	def __init__(self):
		self.log = ''
		self.window = self.create_window()
  
	def create_window(self):
		layout = [
     						[sg.Push(), sg.Graph(canvas_size=(512, 256), graph_bottom_left=(0,0), graph_top_right=(512, 256), key='-DISPLAY-'), sg.Push()],
            			[sg.Multiline('', autoscroll=True, size=(108, 10), key='-OUTPUT-', background_color='#222222', text_color='#FFFFFF', disabled=True, \
                           					sbar_trough_color='#222222', sbar_relief=sg.RELIEF_FLAT, sbar_arrow_color='#222222')],
               		[sg.Input(key='-IN-', size=(87, 1)), sg.Button('Submit', key='-SUBMIT-', size=(7,1))]
                 	]
		return sg.Window('Test', layout=layout, size=(900, 525), finalize=True)

	# This is where the UI handles I/O
	def run_game(self, parser, window):
		while True:
			event, values = window.read()
   
			if event == sg.WIN_CLOSED:
				break

			window['-DISPLAY-'].draw_image(filename='./assets/Sleeping Quarters.png', location=(0, 256))
			window['-DISPLAY-'].draw_image(filename='./assets/Underling.png', location=(256-64, 256))	
 
			self.log += '> ' + parser.parse_input(values['-IN-']) + '\n'
 
			window['-OUTPUT-'].update(self.log)
   
			window['-IN-'].update('')
   
		window.close()