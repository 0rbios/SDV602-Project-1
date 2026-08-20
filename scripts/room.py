class Room:
   def __init__(self, name, items = [], enemy = None, doors = []):
      self.name = name
      self.items = items
      self.enemy = enemy
      self.doors = doors