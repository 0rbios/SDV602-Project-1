from pickup import Pickup

class Shield(Pickup):
	def __init__(self, status, name, defense):
		super().__init__(name)
		self.status = status
		self.defense = defense

	def use(self) -> str:
		self.status.shield = self
		return 'Equipped ' + self.name