from room import Room
from door import Door

class Game:
	room = Room('Padded Cell', './assets/Kitchen.png')
 
	door = Door("north", room, "south", room, None)
   
	def __init__(self):
		self.current_room = self.room
		self.current_room.doors = [self.door]