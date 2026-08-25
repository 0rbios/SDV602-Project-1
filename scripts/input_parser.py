class Parser:
	def parse_input(self, input):
		action_array = input.split(' ')
      
		match action_array[0].lower():
			case 'move': pass
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