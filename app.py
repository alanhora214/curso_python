"""
Author: Alan Horacio Bejarano Castro Here goes the game logic for Tictactoe 
"""
from game_logic import game

def main():
    """ Main function to start the game
    """
    playing = True
    score = {'X':0, 'O': 0, 'Ties': 0}
    while playing:
        winner = game()
        if len(winner) > 0:
            print(f"winner: Player {winner}")
        else:
            print("It´s a tie!")
            winner = 'Ties'
        score[winner] += 1
        replay = input("Do you want to play again? (y/n): ").strip().lower()
        if replay != 'y':
            playing = False
        print(f"Score: X = {score['X']}, 0 = {score['0']}, Ties = {score['Ties']}")

if __name__ == "__main__":
    main()