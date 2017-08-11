class Monster:
  def __init__(self, **kwargs):
    self.name = kwargs.get('name', 'monster')
    self.damage = kwargs.get('damage', '1')
    self.sound = kwargs.get('sound', 'roar')
    self.attack = kwargs.get('attack', 'munched')


  def battlecry(self):
    return self.sound.upper()