class Parser:
	def __init__(self, game):
		self.game = game
   
	def parse_input(self, input):
		action_array = input.strip().split(" ")
   
		match action_array[0].lower():
     
			case "move":
				if len(action_array) <= 1: return "Move where?"
    
				attempt_move = self.game.current_room.move(action_array[1].capitalize())
				if attempt_move == None: return "Cannot go that way"
				
				self.game.current_room = attempt_move
				return "Moving to " + attempt_move.name
					
  
			case "attack": pass
   
			case "unlock":
				if len(action_array) <= 1: return "Unlock which door?"

				for door in self.game.current_room.doors:
					if action_array[1].lower() in door.directions.keys() and door.directions[action_array[1].lower()] != self.game.current_room:
						return self.game.current_room.doors[action_array[1].lower()].unlock(self.game.player.inventory)

				return "Not a door in this room"
				
			case "pickup":
				if len(action_array) <= 1: return "Pick up what item?"
    
				find_item = ""
    
				for input in range(len(action_array)):
					if input < 1: continue
					find_item += action_array[input] + " "
     
				find_item = find_item.strip()			
    
				for item in self.game.current_room.items:
					if item.name.lower() == find_item.lower():
						self.game.inventory.add_item(item)
						self.game.current_room.remove_item(item)
						return "Picked up " + item.name

				return "That item isn't here"
   
			case "drop":
				if len(action_array) <= 1: return "Drop what item?"
    
				find_item = ""
    
				for input in range(len(action_array)):
					if input < 1: continue
					find_item += action_array[input] + " "
     
				find_item = find_item.strip()			
    
				for item in self.game.inventory.items:
					if item.name.lower() == find_item.lower():
						self.game.current_room.add_item(item)
						self.game.inventory.remove_item(item)
						return "Dropped " + item.name

				return "You aren't holding that item"
   
			case "use":
				if len(action_array) <= 1: return "Use what item?"
    
				find_item = ""
    
				for input in range(len(action_array)):
					if input < 1: continue
					find_item += action_array[input] + " "
     
				find_item = find_item.strip()			
    
				for item in self.game.inventory.items:
					if item.name.lower() == find_item.lower():
						return item.use()

				return "You aren't holding that item"
   
			case "search":
				item_list = "You look around for items:"
    
				for item in self.game.current_room.items:
					item_list += "\n\t- " + item.name
    
				if item_list == "You look around for items:":
					item_list += "\n\t- There are no items here"

				return item_list
   
			case "doors":
				door_list = "You look around for doors:"
      
				for door in self.game.current_room.doors:
					for direction in door.directions.keys():
						if door.directions[direction] != self.game.current_room:
							door_list += "\n\t- There is a door to the " + direction
       
				return door_list
   
			case "help":
				return f"\nMove – Switches to another location scene\
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
                        \n\tArgument(s): Element e.g. “fire” or elements e.g. “fire + water”"
   
			case "inventory":
				item_list = "You are currently carrying these items:"
    
				for item in self.game.inventory.items:
					item_list += "\n\t- " + item.name
    
				if item_list == "You are currently carrying these items:":
					item_list += "\n\t- You're not holding anything"

				return item_list
   
			case "status":
				weapon_string = "None"
				shield_string = "None"
    
				if self.game.player.status.weapon != None:
					weapon_string = self.game.player.status.weapon.name
    
				if self.game.player.status.shield != None:
					shield_string = self.game.player.status.shield.name
    
				return f"You check yourself:\n\tHP: {self.game.player.status.stats["health"]}\n\tStrength: {self.game.player.status.stats["strength"]}\n\tSen: {self.game.player.status.sen.name}\n\tWeapon: {weapon_string}\n\tShield: {shield_string}"
   
			case "sen":
				if len(action_array) <= 1: return f"Sen elements:\n\t- Fire\n\t- Water\n\t- Earth\n\t- Air\n\t- Snow\n\t- Blood"

				for element in self.game.sen_elements:
					if element.name.lower() == action_array[1].lower():
						self.game.player.status.sen = element
						return "Switched Sen element to " + element.name

				return f"Sen elements:\n\t- Fire\n\t- Water\n\t- Earth\n\t- Air\n\t- Snow\n\t- Blood"
   
   
			case _: return "Invalid Command"