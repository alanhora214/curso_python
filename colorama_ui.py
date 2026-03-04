""" Text user interface for the tournament """
from colorama import Fore, Back, Style, init
import colorama
init(autoreset=True)
from Tournament import Tournament
import os

class ColoramaUI:
    def __init__(self):
        self.tournament = None
        self.current_file = None 
    def set_current_file(self, file_path: str):
        self.current_file = file_path
    def run (self):
        """ Run the colorama ui """
        colorama.init(autoreset=True)
        self.display_menu()
    def show_menu(self):
        """ Show the menu """
        while True:
            print("\nTournament")
            print(Fore.GREEN + "1. Load tournament")
            print(Fore.CYAN + "2. Display tournament")
            print(Fore.RED + "3. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                file_path = input("Engter the path to the JSON file: ")
                self.set_current_file(file_path)
                self.open_tournament(file_path)
            elif choice == "2":
                self.display_tournament()
            elif choice == "3":
                self.exit_app()
            else:
                print("Invalid choice. Please try again.")
    def open_tournament(self, file_path: str):
        """ Open tournament from JSON file """
        self.tournament = Tournament("Tournament")
        self.tournament.load_json(file_path)
    def display_tournament(self):
        """ Display tournament """
        # clear screen
        os.system("cls" if os.name == "nt" else "clear")
        # set background color to gray and text colo to white
        print(Back.LIGHTBLACK_EX + Fore.WHITE + str(self.tournament))
        for group in self.tournament.groups:
            print(group)
        for game in self.tournament.games:
            print(game)
        else: 
            print("No tournament loaded.")
    def exit_app(self):
        """ Exit the application """
        print("Exiting application...")
        exit()

    def get_tournament_json(self):
        """ Get the tournament """
        file_path = input("Enter the path to the JSON file: ")
        self.set_current_file(file_path)
        self.open_tournament()

    def display_menu(self):
        """ Display the menu """
        dictionary_menu = {
            "1": "Load tournament",
            "2": "Display tournament",
            "3": "Exit"
        }
        action_dictionary = {
            "1": self.get_tournament_json,
            "2": self.display_tournament,
            "3"
            "5": self.exit_app
        }

        while True:
            print("\nTournament")
            for key in sorted(dictionary_menu.keys()):
                print(f"{key}. {dictionary_menu[key]}")
            choice = input("Enter your choice: ")
            if choice in action_dictionary:
                action_dictionary[choice]()
            else:
                print("Invalid choice. Please try again.")  

    def display_groups(self):
        os.system("cls" if os.name == "nt" else "clear")
        print(Back.LIGHTBLACK_EX + Fore.WHITE + str(self.tournament))
        for group in self.tournament.groups:
            print(group)
        else:
            print("No tournament loaded.") 

if __name__ == "__main__":
    ui = ColoramaUI()
    ui.set_current_file("tournament.json")
    ui.open_tournament
    ui.run()    