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
    
	player = Player(Status(20, sen_elements[0], 1))
	inventory = Inventory()
   
   # Creates the health and strength increases
   
	buffs = [
		Buff(player.status, "health", 5),
		Buff(player.status, "strength", 2)
	]
   
   # Make a set of keys
   
	keys = {
		Pickup("Living Quarters' Key"),
		Pickup("Dining Hall Key"),
		Pickup("Dining Hall Exit Key"),
		Pickup("Aviary Key"),
		Pickup("Vault Key")
	}
   
   # Creates unarmed enemies in a list

	enemies = [
    Enemy("Gatekeeper", 20, 1, None, None, sen_elements[2], "./assets/Gatekeeper.png", "Gatekeeper: Noone gets past me!", "Gatekeeper: N-No... You can't get past me...", [key for key in keys if key.name =="Living Quarters' Key"]),
    Enemy("Archer", 30, 2, None, None, sen_elements[3], "./assets/Archer.png", "Archer: I'm going to fill you with arrows!", "Archer: I guess my aim wasn't precise enough!", [key for key in keys if key.name =="Dining Hall Key"]),
    Enemy("Chef", 45, 4, None, None, sen_elements[0], "./assets/Chef.png", "Chef: You're cooked!", "Chef: In the end, I guess it was I who was cooked!",[key for key in keys if key.name =="Dining Hall Exit Key"]),
    Enemy("Initiate", 58, 7, None, None, sen_elements[1], "./assets/Initiate.png", "Initiate: Your traitor! I'll stop you!", "Initiate: There's a reason I'm still in training...", [key for key in keys if key.name =="Aviary Key"]),
    Enemy("Underling", 73, 12, None, None, sen_elements[4], "./assets/Underling.png", "Mad One's Underling: The master is the king, how dare you question him!", "Mad One's Underling: S-Stay away from him!", [key for key in keys if key.name =="Vault Key"]),
    Enemy("The Mad One", 80, 15, None, None, sen_elements[5], "./assets/Mad One.png", "The Mad One: You made it all this way, I'm impressed... But now I'll end you!", "You have defeated the Mad One, congradulations!")
   ]
   
   # Give the enemies weapons / shields
   
	enemies[0].weapon = Weapon(enemies[0], "Spear", 2)
	enemies[1].weapon = Weapon(enemies[1], "Bow", 3)
	enemies[2].weapon = Weapon(enemies[2], "Knife", 5)
	enemies[3].weapon = Weapon(enemies[3], "Wooden Sword", 3)
	enemies[4].weapon = Weapon(enemies[4], "Chains", 10)
	enemies[5].weapon = Weapon(enemies[5], "Mad Ones Sword", 16)
   
   # Create all of the disconnected rooms
   
	rooms = {
		"Entryway": Room("Entryway", "./assets/Room Center Right.png", items=[Shield(player.status, "Small Shield", 2)]),
		"South Corridor": Room("South Corridor", "./assets/Room Left Right.png", items=[Consumable("Health Item", buffs[0])]),
		"Armoury": Room("Armoury", "./assets/Armoury.png", enemy=enemies[0]),
		"Vault Entrance": Room("Vault Entrance", "./assets/Room Left Right.png", items=[Consumable("Health Item", buffs[0])]),
		"Vault": Room("Vault", "./assets/Vault.png", items=[Weapon(player.status, "Legend's Sword", 15)]),
		"South-East Corridor": Room("South-East Corridor", "./assets/Room Center Right.png"),
		"Watch Tower": Room("Watch Tower", "./assets/Watchtower.png", items=[Weapon(player.status, "Hand Axe", 2)], enemy=enemies[1]),
		"East Corridor": Room("East Corridor", "./assets/Room Left Right.png", items=[Consumable("Strength Item", buffs[1])]),
		"Storage Room": Room("Storage Room", "./assets/Storage.png", items=[Consumable("Health Item", buffs[0]), Weapon(player.status, "Short Sword", 4)]),
		"North-East Corridor": Room("North-East Corridor", "./assets/Room Left Right.png", items=[Consumable("Health Item", buffs[0])]),
		"Kitchen": Room("Kitchen", "./assets/Kitchen.png", items=[Shield(player.status, "Shield", 5)], enemy=enemies[2]),
		"East-Central Corridor": Room("East-Central Corridor", "./assets/Room Center Right.png", items=[Consumable("Health Item", buffs[0])]),
		"Dining Hall": Room("Dining Hall", "./assets/Dining Hall.png", items=[Consumable("Health Item", buffs[0]), Weapon(player.status, "Battle Axe", 7)]),
		"South-Central Corridor": Room("South-Central Corridor", "./assets/Room Left Right.png", items=[Consumable("Strength Item", buffs[1])]),
		"North-Central Corridor": Room("North-Central Corridor", "./assets/Room Left Right.png", items=[Consumable("Strength Item", buffs[1])]),
		"Training Room": Room("Training Room", "./assets/Training Room.png", items=[Weapon(player.status, "Pistol", 8)]),
		"Training Armoury": Room("Training Armoury", "./assets/Training Armoury.png", enemy=enemies[3]),
		"North-West Corridor": Room("North-West Corridor", "./assets/Room Left Right.png", items=[Consumable("Strength Item", buffs[1])]),
		"Living Quarters": Room("Living Quarters", "./assets/Room All.png", items=[Weapon(player.status, "Saber", 7)]),
		"East Living Corridor": Room("East Living Corridor", "./assets/Room Center Right.png", items=[Consumable("Health Item", buffs[0])]),
		"North Living Corridor": Room("North Living Corridor", "./assets/Room Left Right.png", items=[Consumable("Health Item", buffs[0])]),
		"Sleeping Quarters": Room("Sleeping Quarters", "./assets/Sleeping Quarters.png", items=[Weapon(player.status, "Rifle", 9)], enemy=enemies[4]),
		"West Living Corridor": Room("West Living Corridor", "./assets/Room Center Right.png", items=[Consumable("Health Item", buffs[0])]),
		"North Corridor": Room("North Corridor", "./assets/Room Left Right.png"),
		"Aviary": Room("Aviary", "./assets/Aviary.png", enemy=enemies[5])
	}
   
   # Make the doors between each room and automatically adds all door to rooms
   
	doors = [
		Door("South", rooms["Entryway"], "North", rooms["South-Central Corridor"]),
		Door("West", rooms["Entryway"], "East", rooms["South Corridor"]),
		Door("West", rooms["South Corridor"], "East", rooms["Armoury"]),
		Door("West", rooms["Armoury"], "East", rooms["South-East Corridor"]),
		Door("South", rooms["Armoury"], "North", rooms["Vault Entrance"]),
		Door("South", rooms["Vault Entrance"], "North", rooms["Vault"], [key for key in keys if key.name =="Vault Key"]),
  		Door("West", rooms["South-East Corridor"], "North", rooms["Watch Tower"]),
		Door("South", rooms["Watch Tower"], "North", rooms["East Corridor"]),
		Door("North", rooms["Storage Room"], "South", rooms["East Corridor"]),
		Door("West", rooms["North-East Corridor"], "East", rooms["Storage Room"]),
		Door("East", rooms["North-East Corridor"], "West", rooms["Kitchen"]),
		Door("North", rooms["Kitchen"], "South", rooms["East-Central Corridor"]),
		Door("East", rooms["East-Central Corridor"], "West", rooms["Dining Hall"], [key for key in keys if key.name =="Dining Hall Key"]),
		Door("North", rooms["Dining Hall"], "South", rooms["South-Central Corridor"], [key for key in keys if key.name =="Dining Hall Key"]),
		Door("South", rooms["Dining Hall"], "North", rooms["North-Central Corridor"], [key for key in keys if key.name =="Dining Hall Exit Key"]),
		Door("South", rooms["North-Central Corridor"], "North", rooms["Training Room"]),
		Door("East", rooms["Training Room"], "West", rooms["North Corridor"]),
		Door("East", rooms["North Corridor"], "West", rooms["Training Armoury"]),
		Door("North", rooms["Training Armoury"], "South", rooms["North-West Corridor"]),
		Door("North", rooms["North-West Corridor"], "South", rooms["Living Quarters"], [key for key in keys if key.name =="Living Quarters' Key"]),
		Door("North", rooms["Living Quarters"], "South", rooms["East Living Corridor"]),
		Door("West", rooms["Living Quarters"], "East", rooms["North Living Corridor"]),
		Door("East", rooms["North Living Corridor"], "West", rooms["Sleeping Quarters"]),
		Door("North", rooms["Sleeping Quarters"], "South", rooms["West Living Corridor"]),
		Door("East", rooms["East Living Corridor"], "West", rooms["Aviary"], [key for key in keys if key.name =="Aviary Key"]),
		Door("West", rooms["West Living Corridor"], "East", rooms["Aviary"], [key for key in keys if key.name =="Aviary Key"])
	]
   
	for room in rooms:
		room_doors = []
  
		for door in doors:
			if rooms[room] in door.directions.values():
				room_doors.append(door)
     
		rooms[room].doors = room_doors
   
	def __init__(self):
		self.current_room = self.rooms["Entryway"]
		self.current_combat = None
		self.combat = False
  
	def check_combat(self):
		if self.current_room.enemy == None: return False
		if self.current_room.enemy.active == False: return False
  
		self.current_combat = Combat(self, self.player, self.current_room.enemy)

		return True