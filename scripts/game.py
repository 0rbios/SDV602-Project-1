from room import Room
from door import Door
from player import Player
from inventory import Inventory
from consumable import Consumable
from status import Status
from element import Element
from buff import Buff
from pickup import Pickup
from shield import Shield
from weapon import Weapon

class Game:
    
    # Loads Sen elements
    
	sen_elements = [
		Element("Fire"),
		Element("Water"),
		Element("Earth"),
		Element("Air"),
		Element("Snow"),
		Element("Blood")
	]
 
	sen_elements[0].advantage = (sen_elements[5], sen_elements[3])
	sen_elements[1].advantage = (sen_elements[0], sen_elements[5])
	sen_elements[2].advantage = (sen_elements[0], sen_elements[1])
	sen_elements[3].advantage = (sen_elements[2], sen_elements[4])
	sen_elements[4].advantage = (sen_elements[2], sen_elements[1])
	sen_elements[5].advantage = (sen_elements[3], sen_elements[4])
    
    # Creates a player
    
	player = Player(Status(10, sen_elements[0], 5))
	inventory = Inventory()
   
   # Creates the health and strength increases
   
	buffs = [
		Buff(player.status, "health", 5),
		Buff(player.status, "Strength", 2)
	]
   
   # Create all of the disconnected rooms
   
	rooms = {
		"Entryway": Room("Entryway", "./assets/Entryway.png", items=[Shield(player.status, "Small Shield", 2)]),
		"South Corridor": Room("South Corridor", "./assets/Room Left Right.png", items=[Consumable("Health Item", buffs[0])]),
		"Armoury": Room("Armoury", "./assets/Armoury.png"),
		"Vault Entrance": Room("Vault Entrance", "./Room Left Right.png", items=[Consumable("Health Item", buffs[0])]),
		"Vault": Room("Vault", "./assets/Vault.png", items=[Weapon(player.status, "Legend's Sword", 15)]),
		"South-East Corridor": Room("South-East Corridor", "./assets/Room Center Right.png"),
		"Watch Tower": Room("Watch Tower", "./assets/Watch Tower.png", items=[Weapon(player.status, "Hand Axe", 2)]),
		"East Corridor": Room("East Corridor", "./assets/Room Left Right.png", items=[Consumable("Strength Item", buffs[1])]),
		"Storage Room": Room("Storage Room", "./assets/Storage Room.png", items=[Consumable("Health Item", buffs[0]), Weapon(player.status, "Short Sword", 4)]),
		"North-East Corridor": Room("North-East Corridor", "./assets/Room Left Right.png", items=[Consumable("Health Item", buffs[0])]),
		"Kitchen": Room("Kitchen", "./assets/Kitchen.png", items=[Shield(player.status, "Shield", 5)]),
		"East-Central Corridor": Room("East-Central Corridor", "./assets/Room Center Left.png", items=[Consumable("Health Item", buffs[0])]),
		"Dining Hall": Room("Dining Hall", "./assets/Dining Hall.png", items=[Consumable("Health Item", buffs[0]), Weapon(player.status, "Battle Axe", 7)]),
		"South-Central Corridor": Room("South-Central Corridor", "./assets/Room Left Right.png", items=[Consumable("Strength Item", buffs[1])]),
		"North-Central Corridor": Room("North-Central Corridor", "./assets/Room Left Right.png", items=[Consumable("Strength Item", buffs[1])]),
		"Training Room": Room("Training Room", "./assets/Training Room.png", items=[Weapon(player.status, "Pistol", 8)]),
		"Training Armoury": Room("Training Armoury", "./assets/Training Armoury.png"),
		"North-West Corridor": Room("North-West Corridor", "./assets/Room Left Right.png", items=[Consumable("Strength Item", buffs[1])]),
		"Communal Quarters": Room("Communal Quarters", "./assets/Room All.png", items=[Weapon(player.status, "Saber", 7)]),
		"East Living Corridor": Room("East Living Corridor", "./assets/Room Center Left.png", items=[Consumable("Health Item", buffs[0])]),
		"North Living Corridor": Room("North Living Corridor", "./assets/Room Left Right.png", items=[Consumable("Health Item", buffs[0])]),
		"Sleeping Quarters": Room("Sleeping Quarters", "./assets/Sleeping Quarters.png", items=[Weapon(player.status, "Rifle", 9)]),
		"West Living Corridor": Room("West Living Corridor", "./assets/Room Center Right.png", items=[Consumable("Health Item", buffs[0])]),
		"North Corridor": Room("North Corridor", "./assets/Room Left Right.png"),
		"Aviary": Room("Aviary", "./assets/Aviary.png")
	}
   
   # Make the doors between each room and automatically adds all door to rooms
   
	doors = [
		Door("South", rooms["Entryway"], "North", rooms["South-Central Corridor"]),
		Door("West", rooms["Entryway"], "East", rooms["South Corridor"]),
		Door("West", rooms["South Corridor"], "East", rooms["Armoury"]),
		Door("West", rooms["Armoury"], "East", rooms["South-East Corridor"]),
		Door("South", rooms["Armoury"], "North", rooms["Vault Entrance"]),
		Door("South", rooms["Vault Entrance"], "North", rooms["Vault"]),
  		Door("West", rooms["South-East Corridor"], "North", rooms["Watch Tower"]),
		Door("South", rooms["Watch Tower"], "North", rooms["East Corridor"]),
		Door("North", rooms["Storage Room"], "South", rooms["East Corridor"]),
		Door("East", rooms["North-East Corridor"], "West", rooms["Storage Room"]),
		Door("East", rooms["North-East Corridor"], "West", rooms["Kitchen"]),
		Door("North", rooms["Kitchen"], "South", rooms["East-Central Corridor"]),
		Door("East", rooms["East-Central Corridor"], "West", rooms["Dining Hall"]),
		Door("North", rooms["Dining Hall"], "South", rooms["South-Central Corridor"]),
		Door("South", rooms["Dining Hall"], "North", rooms["North-Central Corridor"]),
		Door("South", rooms["North-Central Corridor"], "North", rooms["Training Room"]),
		Door("East", rooms["Training Room"], "West", rooms["North Corridor"]),
		Door("East", rooms["North Corridor"], "West", rooms["Training Armoury"]),
		Door("North", rooms["Training Armoury"], "South", rooms["North-West Corridor"]),
		Door("North", rooms["North-West Corridor"], "South", rooms["Communal Quarters"]),
		Door("North", rooms["Communal Quarters"], "South", rooms["East Living Corridor"]),
		Door("West", rooms["Communal Quarters"], "East", rooms["North Living Corridor"]),
		Door("East", rooms["North Living Corridor"], "West", rooms["Sleeping Quarters"]),
		Door("North", rooms["Sleeping Quarters"], "South", rooms["West Living Corridor"]),
		Door("East", rooms["East Living Corridor"], "West", rooms["Aviary"]),
		Door("West", rooms["West Living Corridor"], "East", rooms["Aviary"])
	]
   
	for room in rooms:
		room_doors = []
  
		for door in doors:
			if rooms[room] in door.directions.values():
				room_doors.append(door)
     
		rooms[room].doors = room_doors
   
	def __init__(self):
		self.current_room = self.rooms["Entryway"]