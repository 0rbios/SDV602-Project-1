class Enemy:
	def __init__(self,
                		name,
                		health,
                		baseDMG,
                		weapon,
                		shield,
                		element,
							sprite,
							pre_dialogue,
							post_dialogue,
							loot : list = []
							):
		self.name = name
		self.health = health
		self.baseDMG = baseDMG
		self.weapon = weapon
		self.shield = shield
		self.element = element
		self.active = True
		self.sprite = sprite
		self.loot = loot

		self.pre_dialogue = pre_dialogue
		self.post_dialogue = post_dialogue
      
	def remove_item(self, item):
		self.loot.remove(item)