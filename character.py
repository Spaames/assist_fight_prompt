class Character :
  def __init__(self, name, hp, order, friendly):
    self.name = name
    self.hp = hp
    self.order = order
    if friendly == "1":
      self.friendly = True
    else:
      self.friendly = False

  def getName(self):
    return self.name

  def getHP(self):
    return self.hp

  def getOrder(self):
    return self.order

  def isFriendly(self):
    return self.friendly
  
  def lowerHealth(self, degat):
    self.hp -= degat

  def isDead(self):
    return self.hp <= 0
