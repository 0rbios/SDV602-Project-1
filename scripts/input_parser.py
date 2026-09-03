class Parser:
	def __init__(self, game):
		self.game = game
   
	def parse_input(self, input):
		action_array = input.strip().split(" ")
   
		match action_array[0].lower():
     
			case "attack":
				if not self.game.combat: return "There's nothing to attack"
    
				attack_events = self.game.current_combat.deal_damage(self.game.current_combat.player, self.game.current_combat.enemy)
    
				if self.game.combat:
					attack_events += "\n> " + self.game.current_combat.deal_damage(self.game.current_combat.enemy, self.game.current_combat.player)
    
				return  attack_events

			case "move":
				if self.game.combat: return "Never back down"
      
				if len(action_array) <= 1: return "Move where?"
    
				attempt_move = self.game.current_room.move(action_array[1].capitalize())
				if attempt_move == None: return "Cannot go that way"
				
				self.game.current_room = attempt_move
				self.game.current_combat = None
				self.game.combat = self.game.check_combat()
    
				if self.game.combat:
					return self.game.current_combat.show_initiation()
  
				return "Moving to " + attempt_move.name

			case "unlock":
				if self.game.combat: return f"{self.game.current_room.enemy} blocks your path"
    
				if len(action_array) <= 1: return "Unlock which door?"

				for door in self.game.current_room.doors:
					if action_array[1].capitalize() in door.directions.keys() and door.directions[action_array[1].capitalize()] != self.game.current_room:
						return door.unlock(self.game.inventory)

				return "Not a door in this room"
				
			case "pickup":
				if self.game.combat: return f"{self.game.current_room.enemy} blocks your path"
    
				if len(action_array) <= 1: return "Pick up what item?"
    
				find_item = ""
    
				for input in range(len(action_array)):
					if input < 1: continue
					find_item += action_array[input] + " "
     
				find_item = find_item.strip()			
    
				if self.game.current_room.enemy != None:
					for item in self.game.current_room.enemy.loot :
						if item.name.lower() == find_item.lower():
							self.game.inventory.add_item(item)
							self.game.current_room.enemy.remove_item(item)
							return "Picked up " + item.name
    
				for item in self.game.current_room.items :
					if item.name.lower() == find_item.lower():
						self.game.inventory.add_item(item)
						self.game.current_room.remove_item(item)
						return "Picked up " + item.name

				return "That item isn't here"
   
			case "drop":
				if self.game.combat: return "That's a bad idea right now"
    
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
						if self.game.combat:
							return f"{item.use(self.game.inventory)}\n{self.game.current_combat.deal_damage(self.game.current_combat.enemy, self.game.current_combat.player)}"
						return item.use(self.game.inventory)

				return "You aren't holding that item"
   
			case "search":
				if self.game.combat: return "Now isn't a good time for that"
    
				if len(action_array) <= 1: return "What do you want to search?"
    
				item_list = "You search for items:"
    
				match action_array[1].lower():
					case "room":
						for item in self.game.current_room.items:
							item_list += f"\n\t- {item.name}"
			
						if item_list == "You search for items:":
							item_list += f"\n\t- There are no items here"
       
					case "enemy":
						if self.game.current_room.enemy == None: return "There is no enemy to search"
						for item in self.game.current_room.enemy.loot:
							item_list += f"\n\t- {item.name}"
			
						if item_list == "You search for items:":
							item_list += f"\n\t- There is nothing to find"

				return item_list
   
			case "doors":
				if self.game.combat: return "Now isn't a good time for that"
    
				door_list = "You look around for doors:"
      
				for door in self.game.current_room.doors:
					for direction in door.directions.keys():
						if door.directions[direction] != self.game.current_room:
							door_list += f"\n\t- There is a door to the {direction}"
       
				return door_list
   
			case "help":
				return f"\nMove – Switches to another location scene\
       						\n\tArgument(s): Location e.g. “north”\
                			\nAttack – Uses the currently equipped weapon to deal damage to an enemy\
                      	\nUnlock – Uses an available valid key to make an area enterable\
                        \n\tArgument(s): Door to unlock e.g. “north”\
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
                        \n\tArgument(s): Element e.g. “fire” (Leave blank to view advantage chart)"
   
			case "inventory":
				item_list = "You are currently carrying these items:"
    
				for item in self.game.inventory.items:
					item_list += f"\n\t- {item.name}"
    
				if item_list == "You are currently carrying these items:":
					item_list += f"\n\t- You're not holding anything"

				return item_list
   
			case "status":
				weapon_string = "None"
				shield_string = "None"
    
				if self.game.player.weapon != None:
					weapon_string = self.game.player.weapon.name
    
				if self.game.player.shield != None:
					shield_string = self.game.player.shield.name
    
				return f"You check yourself:\n\tHP: {self.game.player.stats["health"]}\n\tStrength: {self.game.player.stats["strength"]}\n\tSen: {self.game.player.sen.name}\n\tWeapon: {weapon_string}\n\tShield: {shield_string}"
   
			case "sen":
      
				# Prints the chart of what sen elements are advantageous over each other if the player doesn't specify an element
				if len(action_array) <= 1: return f"Sen Chart:\n\tBlood < Fire > Air\n\tFire < Water > Blood\n\tFire < Earth > Water\n\tEarth < Air > Snow\n\tEarth < Snow > Water\n\tAir < Blood > Snow"

				for element in self.game.sen_elements:
					if element.name.lower() == action_array[1].lower():
						self.game.player.sen = element
						if self.game.combat:
							return f"Switched Sen element to {element.name}\n{self.game.current_combat.deal_damage(self.game.current_combat.enemy, self.game.current_combat.player)}"
						return "Switched Sen element to " + element.name

				return f"Sen elements:\n\t- Fire\n\t- Water\n\t- Earth\n\t- Air\n\t- Snow\n\t- Blood"
   
			case _: return "Invalid Command 	('help' to show commands)"