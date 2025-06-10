import matplotlib.pyplot as plt
from athlete import Athlete
from ball import BallPlayer


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
                for endorsement, count in stat:
                    print(f"{endorsement} ({str(count)})")
            else:
                for name, count in stat:
                    print(f"{str(count)} {name}")
        print()

    @staticmethod
    def displat_all_athletes_stats(athletes: list[Athlete]):
        print()
        print("======== All Athletes Stats ========")
        for athlete in athletes:
            athlete.print_stats()
        print()
            
    @staticmethod
    def get_athlete_name() -> str:
        return input("Enter the name of the athlete: ").strip()
    
    @staticmethod
    def display_message(message: str):
        print(message)
        print()

    @staticmethod
    def get_string_input(prompt: str) -> str:
        return input(prompt).strip()
    
    @staticmethod
    def get_confirmation(prompt: str) -> bool:
        while True:
            response = input(prompt + " (y/n): ").strip().lower()
            if response in ['y', 'yes']:
                return True
            elif response in ['n', 'no']:
                return False
            else:
                print("Invalid input, please enter 'y' or 'n'.")

    @staticmethod
    def display_athlete_info(athlete: Athlete):
        print("\n======= Athlete Info =======")
        if athlete:
            athlete.print_stats()
            if isinstance(athlete, BallPlayer):
                athlete.print_endorsement()
        else:
            print("No athlete found with that name.")
        print()

    def _display_char_submenu():
        print()
        print("======= Display Chart =======")
        print("1. Number of Athletes (Level 1 Classes)")
        print("2. Number of Athletes (Leaf Classes)")
        print("3. Average Salary by Level 1 Class")
        print("4. Average Salary by Leaf Class")
        print("5. Endorsements")
        print("================================")
        print()

    @staticmethod
    def get_chart_menu_choice() -> str:
        GUI._display_char_submenu()
        return input("Enter your choice (1-5): ").strip()

    @staticmethod
    def display_pie_chart(data: dict[str, int], title: str):
        labels = list(data.keys())
        sizes = list(data.values())

        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title(title)
        plt.axis('equal')
        plt.show()

    