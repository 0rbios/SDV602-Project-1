class Combat:
	def __init__(self, game, player, enemy):
		self.game = game
		self.player = player
		self.enemy = enemy

	def deal_damage(self, attacker, target):
    
		# If the player attacks the enemy
		if attacker == self.player:
     
			# Base Damage
			damage = attacker.stats["strength"]
   
			# Weapon Damage
			if attacker.weapon != None: damage += attacker.weapon.damage
   
			# Element Advantage
			if target.element in attacker.sen.advantage: damage += 5
   
			# Shield Reduction
			if target.shield != None: damage -= target.shield.defense
     
			target.health -= damage

			# Did that attack kill them
			if target.health <= 0: return self.enemy_defeated()

			return f"You attacked {self.enemy.name}\n" + self.show_state()
  
		# If the enemy attacks the player
		else:
     
			# Base Damage
			damage = attacker.baseDMG
   
			# Weapon Damage Increase
			if attacker.weapon != None: damage += attacker.weapon.damage
   
			# Checks for an element and applies elemental advantage damage
			if attacker.element != None:
				if target.sen in attacker.element.advantage: damage += 5
   
			# Shield Reduction
			if target.shield != None: damage -= target.shield.defense
     
			target.stats["health"] -= damage
   
			# Did that kill the enemy
			if target.stats["health"] <= 0:
				self.game.__init__()
				return f"{self.enemy.name} defeated you\nYou're quest ends here... You have failed."
   
			return f"{self.enemy.name} attacked you\n{self.show_state()}"

# The message that displays when the combat is initiated
	def show_initiation(self) -> str:
		return f"{self.enemy.name} attacks you\n{self.enemy.pre_dialogue}\n{self.show_state()}"

# Shows the player and enemy health
	def show_state(self) -> str:
		return f"Your health: {self.player.stats["health"]}\nEnemies health: {self.enemy.health}"

# What happens when the player wins in combat
	def enemy_defeated(self) -> str:
		self.enemy.active = False
		self.game.combat = False
  
		self.player.stats["strength"] = 1
  
		return self.enemy.post_dialogue + "\n> You defeated " + self.enemy.name