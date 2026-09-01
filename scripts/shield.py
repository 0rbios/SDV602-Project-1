from pickup import Pickup

class Shield(Pickup):
	def __init__(self, player, name, defense):
		super().__init__(name)
		self.player = player
		self.defense = defense

	def use(self, inventory) -> str:
		self.player.shield = self
		return 'Equipped ' + self.name