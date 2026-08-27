from inventory import Inventory
from room import Room

class Door:
	def __init__(self, directionA, roomA, directionB, roomB, key = None):
		self.directions = {directionA: roomA, directionB: roomB}
		self.key = key
		self.locked = (self.key != None)

	def unlock(self, inventory : Inventory):
		if self.key in inventory.items:
			self.locked = False
			return "Door unlocked"
		else:
			return "Missing key"