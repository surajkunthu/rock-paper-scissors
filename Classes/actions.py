class Actions:
    """
    Actions class is the rock-paper-scissors logic of the game
    """

    def logic(self, action_1: str, action_2: str):
        """
        method defining rock-paper-scissors logic
        """
        print(f"You choose: '{action_1}' | Computer: '{action_2}'")
        if (action_1 == "paper") and (action_2 == "rock"):
            return True
        elif (action_1 == "rock") and (action_2 == "paper"):
            return False
        elif (action_1 == "scissors") and (action_2 == "paper"):
            return True
        elif (action_1 == "paper") and (action_2 == "scissors"):
            return False
        elif (action_1 == "rock") and (action_2 == "scissors"):
            return True
        elif (action_1 == "scissors") and (action_2 == "rock"):
            return False
        else:
            return "Tie"