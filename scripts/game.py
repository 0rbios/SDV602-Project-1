from room import Room
from door import Door
from player import Player
from inventory import Inventory
from consumable import Consumable
from status import Status
from element import Element
from buff import Buff
from shield import Shield
from weapon import Weapon
from combat import Combat
from enemy import Enemy
from pickup import Pickup

class Game:

	def __init__(self):
		# Loads Sen elements
		
		self.sen_elements = [
			Element("Fire"),
			Element("Water"),
			Element("Earth"),
			Element("Air"),
			Element("Snow"),
			Element("Blood")
		]
	
		self.sen_elements[0].advantage = (self.sen_elements[5], self.sen_elements[3])
		self.sen_elements[1].advantage = (self.sen_elements[0], self.sen_elements[5])
		self.sen_elements[2].advantage = (self.sen_elements[0], self.sen_elements[1])
		self.sen_elements[3].advantage = (self.sen_elements[2], self.sen_elements[4])
		self.sen_elements[4].advantage = (self.sen_elements[2], self.sen_elements[1])
		self.sen_elements[5].advantage = (self.sen_elements[3], self.sen_elements[4])
		
		# Creates a player
		
		self.player = Player(Status(20, self.sen_elements[0], 1))
		self.inventory = Inventory()
		
		# Creates the health and strength increases
		
		self.buffs = [
			Buff(self.player.status, "health", 5),
			Buff(self.player.status, "strength", 2)
		]
		
		# Make a set of keys
		
		self.keys = {
			Pickup("Living Quarters' Key"),
			Pickup("Dining Hall Key"),
			Pickup("Dining Hall Exit Key"),
			Pickup("Aviary Key"),
			Pickup("Vault Key")
		}
		
		# Creates unarmed enemies in a list

		self.enemies = [
		Enemy("Gatekeeper", 20, 1, None, None, self.sen_elements[2], "./assets/Gatekeeper.png", "Gatekeeper: Noone gets past me!", "Gatekeeper: N-No... You can't get past me...", [key for key in self.keys if key.name =="Living Quarters' Key"]),
		Enemy("Archer", 30, 2, None, None, self.sen_elements[3], "./assets/Archer.png", "Archer: I'm going to fill you with arrows!", "Archer: I guess my aim wasn't precise enough!", [key for key in self.keys if key.name =="Dining Hall Key"]),
		Enemy("Chef", 45, 4, None, None, self.sen_elements[0], "./assets/Chef.png", "Chef: You're cooked!", "Chef: In the end, I guess it was I who was cooked!",[key for key in self.keys if key.name =="Dining Hall Exit Key"]),
		Enemy("Initiate", 58, 7, None, None, self.sen_elements[1], "./assets/Initiate.png", "Initiate: Your traitor! I'll stop you!", "Initiate: There's a reason I'm still in training...", [key for key in self.keys if key.name =="Aviary Key"]),
		Enemy("Underling", 73, 12, None, None, self.sen_elements[4], "./assets/Underling.png", "Mad One's Underling: The master is the king, how dare you question him!", "Mad One's Underling: S-Stay away from him!", [key for key in self.keys if key.name =="Vault Key"]),
		Enemy("The Mad One", 80, 15, None, None, self.sen_elements[5], "./assets/Mad One.png", "The Mad One: You made it all this way, I'm impressed... But now I'll end you!", "You have defeated the Mad One, congradulations!")
		]
		
		# Give the enemies weapons / shields
		
		self.enemies[0].weapon = Weapon(self.enemies[0], "Spear", 2)
		self.enemies[1].weapon = Weapon(self.enemies[1], "Bow", 3)
		self.enemies[2].weapon = Weapon(self.enemies[2], "Knife", 5)
		self.enemies[3].weapon = Weapon(self.enemies[3], "Wooden Sword", 3)
		self.enemies[4].weapon = Weapon(self.enemies[4], "Chains", 10)
		self.enemies[5].weapon = Weapon(self.enemies[5], "Mad Ones Sword", 16)
		
		# Create all of the disconnected rooms
		
		self.rooms = {
			"Entryway": Room("Entryway", "./assets/Room Center Right.png", items=[Shield(self.player.status, "Small Shield", 2)]),
			"South Corridor": Room("South Corridor", "./assets/Room Left Right.png", items=[Consumable("Health Item", self.buffs[0])]),
			"Armoury": Room("Armoury", "./assets/Armoury.png", enemy=self.enemies[0]),
			"Vault Entrance": Room("Vault Entrance", "./assets/Room Left Right.png", items=[Consumable("Health Item", self.buffs[0])]),
			"Vault": Room("Vault", "./assets/Vault.png", items=[Weapon(self.player.status, "Legend's Sword", 15)]),
			"South-East Corridor": Room("South-East Corridor", "./assets/Room Center Right.png"),
			"Watch Tower": Room("Watch Tower", "./assets/Watchtower.png", items=[Weapon(self.player.status, "Hand Axe", 2)], enemy=self.enemies[1]),
			"East Corridor": Room("East Corridor", "./assets/Room Left Right.png", items=[Consumable("Strength Item", self.buffs[1])]),
			"Storage Room": Room("Storage Room", "./assets/Storage.png", items=[Consumable("Health Item", self.buffs[0]), Weapon(self.player.status, "Short Sword", 4)]),
			"North-East Corridor": Room("North-East Corridor", "./assets/Room Left Right.png", items=[Consumable("Health Item", self.buffs[0])]),
			"Kitchen": Room("Kitchen", "./assets/Kitchen.png", items=[Shield(self.player.status, "Shield", 5)], enemy=self.enemies[2]),
			"East-Central Corridor": Room("East-Central Corridor", "./assets/Room Center Right.png", items=[Consumable("Health Item", self.buffs[0])]),
			"Dining Hall": Room("Dining Hall", "./assets/Dining Hall.png", items=[Consumable("Health Item", self.buffs[0]), Weapon(self.player.status, "Battle Axe", 7)]),
			"South-Central Corridor": Room("South-Central Corridor", "./assets/Room Left Right.png", items=[Consumable("Strength Item", self.buffs[1])]),
			"North-Central Corridor": Room("North-Central Corridor", "./assets/Room Left Right.png", items=[Consumable("Strength Item", self.buffs[1])]),
			"Training Room": Room("Training Room", "./assets/Training Room.png", items=[Weapon(self.player.status, "Pistol", 8)]),
			"Training Armoury": Room("Training Armoury", "./assets/Training Armoury.png", enemy=self.enemies[3]),
			"North-West Corridor": Room("North-West Corridor", "./assets/Room Left Right.png", items=[Consumable("Strength Item", self.buffs[1])]),
			"Living Quarters": Room("Living Quarters", "./assets/Room All.png", items=[Weapon(self.player.status, "Saber", 7)]),
			"East Living Corridor": Room("East Living Corridor", "./assets/Room Center Right.png", items=[Consumable("Health Item", self.buffs[0])]),
			"North Living Corridor": Room("North Living Corridor", "./assets/Room Left Right.png", items=[Consumable("Health Item", self.buffs[0])]),
			"Sleeping Quarters": Room("Sleeping Quarters", "./assets/Sleeping Quarters.png", items=[Weapon(self.player.status, "Rifle", 9)], enemy=self.enemies[4]),
			"West Living Corridor": Room("West Living Corridor", "./assets/Room Center Right.png", items=[Consumable("Health Item", self.buffs[0])]),
			"North Corridor": Room("North Corridor", "./assets/Room Left Right.png"),
			"Aviary": Room("Aviary", "./assets/Aviary.png", enemy=self.enemies[5])
		}
		
		# Make the doors between each room and automatically adds all door to rooms
		
		self.doors = [
			Door("South", self.rooms["Entryway"], "North", self.rooms["South-Central Corridor"]),
			Door("West", self.rooms["Entryway"], "East", self.rooms["South Corridor"]),
			Door("West",self.rooms["South Corridor"], "East", self.rooms["Armoury"]),
			Door("West", self.rooms["Armoury"], "East", self.rooms["South-East Corridor"]),
			Door("South", self.rooms["Armoury"], "North", self.rooms["Vault Entrance"]),
			Door("South", self.rooms["Vault Entrance"], "North", self.rooms["Vault"], [key for key in self.keys if key.name =="Vault Key"]),
			Door("West", self.rooms["South-East Corridor"], "North", self.rooms["Watch Tower"]),
			Door("South", self.rooms["Watch Tower"], "North", self.rooms["East Corridor"]),
			Door("North", self.rooms["Storage Room"], "South", self.rooms["East Corridor"]),
			Door("West", self.rooms["North-East Corridor"], "East",self.rooms["Storage Room"]),
			Door("East", self.rooms["North-East Corridor"], "West", self.rooms["Kitchen"]),
			Door("North", self.rooms["Kitchen"], "South", self.rooms["East-Central Corridor"]),
			Door("East", self.rooms["East-Central Corridor"], "West", self.rooms["Dining Hall"], [key for key in self.keys if key.name =="Dining Hall Key"]),
			Door("North", self.rooms["Dining Hall"], "South", self.rooms["South-Central Corridor"], [key for key in self.keys if key.name =="Dining Hall Key"]),
			Door("South", self.rooms["Dining Hall"], "North", self.rooms["North-Central Corridor"], [key for key in self.keys if key.name =="Dining Hall Exit Key"]),
			Door("South", self.rooms["North-Central Corridor"], "North", self.rooms["Training Room"]),
			Door("East", self.rooms["Training Room"], "West", self.rooms["North Corridor"]),
			Door("East", self.rooms["North Corridor"], "West", self.rooms["Training Armoury"]),
			Door("North", self.rooms["Training Armoury"], "South", self.rooms["North-West Corridor"]),
			Door("North", self.rooms["North-West Corridor"], "South", self.rooms["Living Quarters"], [key for key in self.keys if key.name =="Living Quarters' Key"]),
			Door("North", self.rooms["Living Quarters"], "South", self.rooms["East Living Corridor"]),
			Door("West", self.rooms["Living Quarters"], "East", self.rooms["North Living Corridor"]),
			Door("East", self.rooms["North Living Corridor"], "West", self.rooms["Sleeping Quarters"]),
			Door("North", self.rooms["Sleeping Quarters"], "South", self.rooms["West Living Corridor"]),
			Door("East", self.rooms["East Living Corridor"], "West", self.rooms["Aviary"], [key for key in self.keys if key.name =="Aviary Key"]),
			Door("West", self.rooms["West Living Corridor"], "East", self.rooms["Aviary"], [key for key in self.keys if key.name =="Aviary Key"])
		]
		
		for room in self.rooms:
			room_doors = []
	
			for door in self.doors:
				if self.rooms[room] in door.directions.values():
					room_doors.append(door)
		
			self.rooms[room].doors = room_doors
    
		self.current_room = self.rooms["Entryway"]
		self.current_combat = None
		self.combat = False
  
	def check_combat(self):
		if self.current_room.enemy == None: return False
		if self.current_room.enemy.active == False: return False
  
		self.current_combat = Combat(self, self.player, self.current_room.enemy)

		return True