class Monster:
    def __init__(self, sound, **kwargs):
        self.sound = sound
        for attribute, value in kwargs.items():
            setattr(self, attribute, value)


    def battlecry(self, sound):
        return self.sound.upper()