from room import Room
from door import Door
from player import Player
from inventory import Inventory
from consumable import Comsumable
from status import Status
from element import Element

class Game:
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
    
	player = Player(Status(10, sen_elements[0], 5))
	inventory = Inventory()
   
	test_box = Comsumable("Test Box", None)
   
	room1 = Room('Less Padded Cell', './assets/Watchtower.png', [test_box])
	room2 = Room('Padded Cell', './assets/Kitchen.png')
 
	door = Door("north", room1, "south", room2, None)
 
	room1.doors = [door]
	room2.doors = [door]
   
	def __init__(self):
		self.current_room = self.room1