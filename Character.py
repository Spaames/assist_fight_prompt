class Character :
  def __init__(self, name, hp, order, friendly):
    self.name = name
    self.hp = hp
    self.order = order
    self.friendly = friendly

  def get_name(self):
    return self.name

  def get_hp(self):
    return self.hp

  def get_order(self):
    return self.order

  def is_friendly(self):
    return self.friendly
  
  def lower_health(self, degat):
    self.hp -= degat

  def is_dead(self):
    return self.hp <= 0
