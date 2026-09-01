class Player:
    def __init__(self, health, sen, strength):
        self.sen = sen
        
        self.stats = {
				"health": health,
				"strength": strength
		  }
        
        self.weapon = None
        self.shield = None