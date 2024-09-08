from Classes.actions import Actions
from Classes.human import Human
from Classes.computer import Computer
# import tabulate from fancier tables
from tabulate import tabulate

# initialize game
GAME_STATE: bool = True
WINNING_SCORE: int = 3
ROUND: int = 0
computer_player = Computer()
user_name: str = str(input("Please enter your name: "))
user = Human(user_name)

def display_match(result, player_1, player_2):
    """
    Helper function to determine match winner, increase score for winner
    """
    if (result == "Tie"):
        print(f"Result: {result}\n")
    elif (result):
        print(f"Result: {player_1.name} beats {player_2.name}!\n")
        player_1.score += 1
    else:
        print(f"Result: {player_2.name} beats {player_1.name}!\n")
        player_2.score += 1

    standings_list = [[player_1.name, player_1.score],
                      [player_2.name, player_2.score]]
    print(tabulate(standings_list, headers= ["Player", "Score"], tablefmt="grid"))
    return

def display_results(player_1, player_2):
    """
    Helper function for displaying final results table
    """
    final_list = [[player_1.name, "Wins!"],
                  [player_2.name, "Loses!"]]
    
    print(f"\nFINAL -- {ROUND} rounds")
    print(tabulate(final_list, headers= ["Player", "State"], tablefmt="grid"))
    return

# Main game loop
while (GAME_STATE):
    game = Actions()
    result = game.logic(user.play(), computer_player.play())

    ROUND += 1
    print("\nRound: ", ROUND)
    display_match(result, user, computer_player)

    # End game
    if (user.score == WINNING_SCORE):
        display_results(user, computer_player)
        GAME_STATE = False
    elif (computer_player == WINNING_SCORE):
        display_results(computer_player, user)
        GAME_STATE = False