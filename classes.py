class Player():
    """
    Class Player. Contains attributes:
    :param name: player's name
    :tupe name: str
    """
    def __init__(self, name, lives=1):
        self.name = name
        self.lives = lives

    def info(self):
        if (self.lives == 1):
            return f'My name is {self.name}. I have 1 life left'
        else:
            return f'My name is {self.name}. I have {self.lives} lives left'
