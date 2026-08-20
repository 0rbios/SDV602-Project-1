from pickup import Pickup

class Shield(Pickup):
   def __init__(self, name, defense):
      super().__init__(name)
      self.defense = defense