class Room:
	def __init__(self, name, sprite, items = [], enemy = None, doors = []):
		self.name = name
		self.items = items
		self.enemy = enemy
		self.doors = doors
		self.sprite = sprite
   
	def move(self, location):
		for door in self.doors:
			if location in door.directions.keys():
				if door.directions[location] == self: return None
				return door.directions[location]
		return None