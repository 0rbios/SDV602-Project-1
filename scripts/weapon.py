from pickup import Pickup

class Weapon(Pickup):
   def __init__(self, name, damage):
      super().__init__(name)
      self.damage = damage