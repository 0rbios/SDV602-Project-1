class Combat:
	def __init__(self, game, player, enemy):
		self.game = game
		self.player = player
		self.enemy = enemy

	def deal_damage(self, attacker, target):
		if attacker == self.player:
			target.health -= attacker.status.stats["strength"]

			if target.health <= 0:
				return self.enemy_defeated()

			return f"You attacked {self.enemy.name}\n" + self.show_state()
  
		else:
			target.status.stats["health"] -= attacker.baseDMG
   
			return f"{self.enemy.name} attacked you\n" + self.show_state()

	def show_initiation(self) -> str:
		return f"{self.enemy.name} attacks you\n" + self.show_state()

	def show_state(self) -> str:
		return f"Your health: {self.player.status.stats["health"]}\nEnemies health: {self.enemy.health}"

	def enemy_defeated(self) -> str:
		self.enemy.active = False
		self.game.combat = False
		return "You defeated " + self.enemy.name