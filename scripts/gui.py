import FreeSimpleGUI as sg
class GUI:
	def __init__(self, game):
		self.game = game
		self.log = f"> You have just entered the former Allt temple in Polid Valley, Ghurja.\nThe Mad One has taken control and you must defeat him!\n"
		self.window = self.create_window()
  
		self.window["-OUTPUT-"].update(self.log)
  
		self.window["-DISPLAY-"].draw_image(filename=self.game.current_room.sprite, location=(0, 256))
		if self.game.current_room.enemy != None:
			if self.game.current_room.enemy.active == True:
				self.window["-DISPLAY-"].draw_image(filename=self.game.current_room.enemy.sprite, location=(256-64, 256 / 2 + 64))	

	def create_window(self):
		layout = [
     						[sg.Push(), sg.Graph(canvas_size=(512, 256), graph_bottom_left=(0,0), graph_top_right=(512, 256), key="-DISPLAY-"), sg.Push()],
            			[sg.Multiline("", autoscroll=True, size=(97, 10), key="-OUTPUT-", background_color="#222222", text_color="#FFFFFF", disabled=True, \
                           					sbar_trough_color="#222222", sbar_relief=sg.RELIEF_FLAT, sbar_arrow_color="#222222")],
               		[sg.Input(key="-IN-", size=(90, 1), focus=True), sg.Button("Submit", key="-SUBMIT-", size=(6,1), bind_return_key=True)]
                 	]
		return sg.Window("Test", layout=layout, finalize=True)

	# This is where the UI handles I/O
	def run_game(self, parser, window):
		while True:
			event, values = window.read()
   
			if event == sg.WIN_CLOSED: break
 
			# Sends a command if either the enter key or submit button are clicked
			if event == "-SUBMIT-":
      
				# Sends the requested command to the parser and then loads the result into the log
				self.log += "> " + parser.parse_input(values["-IN-"]) + "\n"
	
				# Update the text terminal to show the new output and clear the input
				window["-OUTPUT-"].update(self.log)
				window["-IN-"].update("")
    
				window["-DISPLAY-"].erase()
				self.window["-DISPLAY-"].draw_image(filename=self.game.current_room.sprite, location=(0, 256))
				if self.game.current_room.enemy != None:
					if self.game.current_room.enemy.active == True:
						self.window["-DISPLAY-"].draw_image(filename=self.game.current_room.enemy.sprite, location=(256-64, 256 / 2 + 64))	
   
		window.close()