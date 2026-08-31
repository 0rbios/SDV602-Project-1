from pickup import Pickup

class Consumable(Pickup):
	def __init__(self, name, buff):
		super().__init__(name)
		self.buff = buff
  
	def use(self) -> str:
		self.buff.apply()
		return 'Used ' + self.name