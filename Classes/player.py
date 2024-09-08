import random

class Player():
    """
    Player class defines a player's characteristics, actions, scors
    """
    # List of possible actions
    possible_actions: list[str] = ["rock", "paper", "scissors"]

    # intial score
    score: int = 0

    def __init__(self, name: str, action: str):
        """
        Initialize Player
        """
        self.name = name
        self.action = action

    def show_characteristics(self):
        """
        Method to display characteristics of Player
        """
        print(f"Name: {self.name}")
        print(f"Score: {self.score}")

    def play(self):
        """
        Method to chooses a random action
        """
        self.action = random.choice(self.possible_actions)
        return self.action