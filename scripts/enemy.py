class Enemy:
   def __init__(self,
                		name,
                		health,
                		baseDMG,
                		weapon,
                		shield,
                		element,
							sprite,
							loot = None
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