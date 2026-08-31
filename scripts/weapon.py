from pickup import Pickup

class Weapon(Pickup):
	def __init__(self, status, name, damage):
		super().__init__(name)
		self.status = status
		self.damage = damage

	def use(self) -> str:
		self.status.weapon = self
		return 'Equipped ' + self.name