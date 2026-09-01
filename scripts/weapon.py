from pickup import Pickup

class Weapon(Pickup):
	def __init__(self, player, name, damage):
		super().__init__(name)
		self.player = player
		self.damage = damage

	def use(self, inventory) -> str:
		self.player.weapon = self
		return 'Equipped ' + self.name