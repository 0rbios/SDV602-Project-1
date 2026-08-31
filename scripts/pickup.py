class Pickup:
	def __init__(self, name):
		self.name = name

	def use(self) -> str:
		return 'This item cannot be used.'