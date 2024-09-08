from Classes.player import Player

class Human(Player):
    """
    Human class inherits the player.py file and asks input from a user through thr console to determin an action to play
    """
    def __init__(self, name: str, action: str = None):
        """
        Initialize Human
        """
        super().__init__(name, action)
        self.name = name
        self.score = Player.score
        self.action = action

    def play(self):
        """
        Method for human to input an action
        """
        try:
            # Obtain user input, convert to lowercase for error handling
            user_action: str = str(input("Choose an action (Rock, Paper, Scissors): ").lower())
            # input validation
            if user_action not in Player.possible_actions:
                raise ValueError
            else:
                self.action = user_action
                return self.action
            
        except ValueError:
            print(f"'{user_action}' is not a possible action")
            # Recursively call play() method until proper action is obtained
            return Human(Player).play()