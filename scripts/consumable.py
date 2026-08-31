from pickup import Pickup

class Consumable(Pickup):
	def __init__(self, name, buff):
		super().__init__(name)
		self.buff = buff
  
	def use(self, inventory) -> str:
		self.buff.apply()
		inventory.remove_item(self)
		return 'Used ' + self.name