class Door:
   def __init__(self, directionA, roomA, directionB, roomB, key = None):
      self.directions = {directionA: roomA, directionB: roomB}
      self.key = key