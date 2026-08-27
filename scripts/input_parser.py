class Parser:
	def __init__(self, game):
		self.game = game
   
	def parse_input(self, input):
		action_array = input.strip().split(' ')
   
		match action_array[0].lower():
     
			case 'move':
				if len(action_array) > 1:
					attempt_move = self.game.current_room.move(action_array[1].lower())
					if attempt_move == None: return 'Cannot go that way'
					
					self.game.current_room = attempt_move
					return "Moving to " + attempt_move.name
				else:
					return("A door is required to move")
  
			case 'attack': pass
   
			case 'unlock':
				if len(action_array) <= 1: return "A door is required to move"

				for door in self.game.current_room.doors:
					if action_array[1].lower() in door.directions.keys() and door.directions[action_array[1].lower()] != self.game.current_room:
						return self.game.current_room.doors[action_array[1].lower()].unlock(self.game.player.inventory)

				return "Not a door in this room"
				
			case 'pickup': pass
   
			case 'drop': pass
   
			case 'use': pass
   
			case 'search': pass
   
			case 'doors':
				door_list = 'You look around for doors:'
      
				for door in self.game.current_room.doors:
					for direction in door.directions.keys():
						if door.directions[direction] != self.game.current_room:
							door_list += '\n- There is a door to the ' + direction
       
				return door_list
   
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