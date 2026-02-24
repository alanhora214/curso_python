from colorama import Fore, Back, Style, init
init(autoreset=True)

class ColoramaUI:
    def __init__(self):
        self.tournament = None
        self.current_file = None
    def set_current_file(self, file_path: str):
        self.current_file = file_path
    def run(self):
        colorama.init(autoreset=True)
        self.show_menu()
    def show_menu(self):
        while True:
            print("\nTournament")
            print("1. Load Tournament from JSON")
            print("2. Display Tournament")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                file_path = input("Enter the path to the tournament JSON file: ")
                self.set_current_file(file_path)
                self.load_tournament()
            elif choice == '2':
                self.display_tournament()
            elif choice == '3':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")