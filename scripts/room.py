class Room:
	def __init__(self, name, sprite, items = [], enemy = None, doors = []):
		self.name = name
		self.items = items
		self.enemy = enemy
		self.doors = doors
		self.sprite = sprite
   
	def move(self, location: str):
		for door in self.doors:
			if location in door.directions.keys():
				if door.directions[location] == self: continue
				if door.locked: continue
				return door.directions[location]
		return None

	def add_item(self, item):
		self.items.append(item)

	def remove_item(self, item):
		self.items.remove(item)