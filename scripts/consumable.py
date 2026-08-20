from pickup import Pickup

class Comsumable(Pickup):
	def __init__(self, name, buff):
		super().__init__(name)
		self.buff = buff