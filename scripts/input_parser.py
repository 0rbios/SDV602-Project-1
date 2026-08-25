class Parser:
	def __init__(self, game):
		self.game = game
   
	def parse_input(self, input):
		action_array = input.strip().split(' ')
   
		match action_array[0].lower():
     
			case 'move':
				if len(action_array) > 1:
					return self.game.current_room.move(action_array[1].lower())
				else:
					return("A door is required to move")
  
			case 'attack': pass
   
			case 'unlock': pass
   
			case 'pickup': pass
   
			case 'drop': pass
   
			case 'use': pass
   
			case 'search': pass
   
			case 'doors': pass
   
			case 'equip': pass
   
			case 'help':
				return f'\nMove – Switches to another location scene\
       						\n\tArgument(s): Location e.g. “north”\
                			\nAttack – Uses the currently equipped weapon to deal damage to an enemy\
                      	\nUnlock – Uses an available valid key to make an area enterable\
                        \n\tArgument(s): Door to unlock e.g. “north door”\
                        \nPickup – Picks up an item and puts it into the players inventory\
                        \n\tArgument(s): Item e.g. “bandage”\
                        \nDrop – Removes an item from the players inventory\
                        \n\tArgument(s): Item e.g. “bandage”\
                        \nUse – Attempts to use an item from the players inventory\
                        \n\tArgument(s): Item e.g. “bandage”\
                        \nSearch – Will display any items which can be found\
                        \n\tArgument(s): Search area e.g. “room”, “enemy”\
                        \nDoors – Display a list of all locked doors in a room\nEquip – Will change the currently equipped weapon\
                        \n\tArgument(s): Weapon e.g. “short sword”\
                        \nHelp – Display a list of commands which the player can use\
                        \nInventory – Displays the player’s current inventory\
                        \nStatus – Displays the player’s current status\
                        \nSen – Changes the player’s current element\
                        \n\tArgument(s): Element e.g. “fire” or elements e.g. “fire + water”'
   
			case 'inventory': pass
   
			case 'status': pass
   
			case 'sen': pass
   
			case _: return 'Invalid Command'