from athlete import Athlete
from hockey import HockeyPlayer
from swimmer import Swimmer
from ball import BallPlayer
from football import FootballPlayer
from basketball import BasketballPlayer

class GUI:

    def _display_main_menu():
        print("======== Athlete Database Menu ========")
        print("1. Load File")
        print("2. Print Stats")
        print("3. Delete Athlete")
        print("4. Save File")
        print("5. Athlete Info")
        print("6. Display Chart")
        print("7. Exit")
        print("=======================================")
        
    @staticmethod
    def get_main_menu_choice() -> str:
        GUI._display_main_menu()
        return input("Enter your choice (1-7): ").strip()

    @staticmethod
    def display_exit_app_message():
        print("\nThanks for using the Athlete Database. Goodbye!\n")

    @staticmethod
    def display_invalid_input_message_main_menu():
        print("\nInvalid choice, please choose an option from the menu (1-7).\n")

    @staticmethod
    def get_filename() -> str:
        return input("Enter the name of the data file (e.g. athletes.txt): ").strip()

    @staticmethod
    def display_file_loaded_message(is_file_loaded : bool):
        if is_file_loaded:
            print(f"Data loaded successfully.")
        else:
            print("No file loaded. Please try again.")
        print()

    @staticmethod
    def display_stats(player_stats : dict):
        print()
        print("======== Athlete Stats ========")
        for stat_name, stat in player_stats.items():
            print()
            print(f"{stat_name}:")
            print("-------------------")
            if stat_name == "Endorsements":
                for endorsement, count in stat.items():
                    print(f"{endorsement} ({str(count)})")
            else:
                for key, value in stat.items():
                    print(f"{str(value)} {key}")
        print()

    @staticmethod
    def displat_all_athletes_stats(athletes: list[Athlete]):
        print()
        print("======== All Athletes Stats ========")
        for athlete in athletes:
            athlete.print_stats()
        print()
            
                
