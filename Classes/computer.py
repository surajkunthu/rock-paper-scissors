from Classes.player import Player

class Computer(Player):
    """
    Inherits the player.py file and chooses a random action to play. Inherited action is invoked by calling Computer().play()
    """
    def __init__(self, name: str = "Computer", action: str = None):
        """
        Initialize Computer
        """
        super().__init__(name, action)
        self.name = name
        self.score = Player.score
        self.action = action