class Buff:
	def __init__(self, player, stat, amount):
		self.player = player
		self.stat = stat
		self.amount = amount
      
	def apply(self):
		if self.stat in self.player.stats:
			self.player.stats[self.stat] += self.amount