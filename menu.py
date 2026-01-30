"""
Menu in main window
"""

def display_menu()-> int:
    """
    display_menu function shows the main menu and gets user choise
    """
    print("Welcome to Tic Tac Toe!")
    print("1. One Player Game")
    print("2. Two Player Game")
    print("3. Exit")
    choise = input("Please select an option (1-3): ")
    return int(choise)

if __name__ == "__main__":
    display_menu()