class Combat:
	def __init__(self, game, player, enemy):
		self.game = game
		self.player = player
		self.enemy = enemy

	def deal_damage(self, attacker, target):
		if attacker == self.player:
			damage = attacker.status.stats["strength"]
   
			if attacker.status.weapon != None: damage += attacker.status.weapon.damage
   
			if target.element in attacker.status.sen.advantage: damage += 5
   
			if target.shield != None: damage -= target.shield.defense
     
			target.health -= damage

			if target.health <= 0:
				return self.enemy_defeated()

			return f"You attacked {self.enemy.name}\n" + self.show_state()
  
		else:
			damage = attacker.baseDMG
   
			if attacker.weapon != None: damage += attacker.weapon.damage
   
			if attacker.element != None:
				if target.status.sen in attacker.element.advantage: damage += 5
   
			if target.status.shield != None: damage -= target.status.shield.defense
     
			target.status.stats["health"] -= damage
   
			return f"{self.enemy.name} attacked you\n" + self.show_state()

	def show_initiation(self) -> str:
		return f"{self.enemy.name} attacks you\n" + self.show_state()

	def show_state(self) -> str:
		return f"Your health: {self.player.status.stats["health"]}\nEnemies health: {self.enemy.health}"

	def enemy_defeated(self) -> str:
		self.enemy.active = False
		self.game.combat = False
  
		self.player.status.strength = 1
  
		return "You defeated " + self.enemy.name