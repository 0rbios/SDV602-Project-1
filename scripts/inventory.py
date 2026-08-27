from pickup import Pickup

class Inventory:
	def __init__(self):
		self.items = []
   
	def add_item(self, pickup : Pickup):
		self.items.append(pickup)

	def remove_item(self, item : Pickup):
		self.items.remove(item)