
class GUI:

    @staticmethod
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
