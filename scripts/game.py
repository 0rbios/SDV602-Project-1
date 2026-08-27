from room import Room
from door import Door
from player import Player
from inventory import Inventory
from consumable import Comsumable

class Game:
	player = Player()
	inventory = Inventory()
   
	test_box = Comsumable("Test Box", None)
   
	room1 = Room('Less Padded Cell', './assets/Watchtower.png', [test_box])
	room2 = Room('Padded Cell', './assets/Kitchen.png')
 
	door = Door("north", room1, "south", room2, None)
 
	room1.doors = [door]
	room2.doors = [door]
   
	def __init__(self):
		self.current_room = self.room1