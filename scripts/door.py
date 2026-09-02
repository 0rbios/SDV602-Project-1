from inventory import Inventory

class Door:
	def __init__(self, directionA, roomA, directionB, roomB, key = None):
		self.directions = {directionA: roomA, directionB: roomB}
		self.key = key
		self.locked = (self.key != None) # Leaves the door unlocked if there is no assigned key

	def unlock(self, inventory : Inventory):
		if self.key == None: return f"That door is already unlocked"
  
		if self.key[0] in inventory.items:
			self.locked = False
			return "Unlocked door"
		else:
			return "You don't have that key"