from gui import GUI
from data import Data
from util import Util

class AthletesManagerApp:
    def __init__(self):
        # Initialize util class, GUI class, anda data class
        self.data = Data()
        
    def run(self):

        while True:
            choice = GUI.get_main_menu_choice()
            if choice == '1':
                filename = GUI.get_filename()
                raw_data = Util.load_file(filename)
                is_file_loaded = self.data.load_data(raw_data)
                GUI.display_file_loaded_message(is_file_loaded)
            elif choice == '2':
                if self.data.athletes:
                    players_stats = self.data.get_statistics()
                    GUI.display_stats(players_stats)
                else:
                    GUI.display_file_loaded_message(False)
            elif choice == '3':
                if self.data.athletes:
                    athlete_name = GUI.get_string_input("Enter the name of the athlete: ")
                    atheltes_found = self.data.find_athlete_by_name(athlete_name)
                    if atheltes_found:
                        if len(atheltes_found) > 1:
                            GUI.display_message(f"Multiple athletes found with the name '{athlete_name}':")
                            confirmation = GUI.get_confirmation("Do you want to delete all of them?")
                            if not confirmation:
                                continue
                        self.data.delete_athlete(athlete_name)
                    else:
                        GUI.display_message(f"No athlete found with the name '{athlete_name}'.")
                else:
                    GUI.display_file_loaded_message(False)
            elif choice == '4':
                continue
            elif choice == '5':
                continue
            elif choice == '6':
                continue
            elif choice == '7':
                GUI.display_exit_app_message()
                break
            elif choice == '0':
                GUI.displat_all_athletes_stats(self.data.athletes)
            else:
                GUI.display_invalid_input_message_main_menu()


if __name__ == "__main__":
    app = AthletesManagerApp()
    app.run()
