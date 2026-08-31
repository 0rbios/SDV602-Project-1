class Buff:
	def __init__(self, status, stat, amount):
		self.status = status
		self.stat = stat
		self.amount = amount
      
	def apply(self):
		if self.stat in self.status.stats:
			self.status.stats[self.stat] += self.amount