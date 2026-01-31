"""
Author: Alan Horacio Bejarano Castro Here goes the game logic for Tictactoe 
"""
##from game_logic import game
from game_logic import two_players
from menu import display_menu

def main():
    """
    Main function to run the Tic Tac Toe
    """
    while True:
        choise = display_menu()
        if choise == 1:
            print("One Player Game is not implemented yet.")
            # Here you would call the one player game fuction when implemented
        elif choise == 2:
            two_players()
        elif choise == 3:
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choise. Please select a valid option")

if __name__ == "__main__":
    main()