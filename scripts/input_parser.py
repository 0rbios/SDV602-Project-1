class Parser:
	def __init__(self, game):
		self.game = game
   
	def parse_input(self, input):
		action_array = input.split(' ')
      
		match action_array[0].lower():
			case 'move':
				if len(action_array) > 1:
					self.game.current_room.move(action_array[1].lower())
				else:
					print("A door is required to move")
			case 'attack': pass
			case 'unlock': pass
			case 'pickup': pass
			case 'drop': pass
			case 'use': pass
			case 'search': pass
			case 'doors': pass
			case 'equip': pass
			case 'help': pass
			case 'inventory': pass
			case 'status': pass
			case 'sen': pass
			case _: pass