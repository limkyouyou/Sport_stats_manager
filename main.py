from gui import GUI
from data import Data
from util import *


class AthletesManagerApp:
    def __init__(self):
        self.data = Data()
        
    def run(self):

        while True:
            choice = GUI.get_main_menu_choice()

            if choice == '1':       # Load File

                filename = GUI.get_filename()       # prompt user for file name and returns it
                raw_data = load_file(filename)
                is_file_loaded = self.data.load_data(raw_data, filename)
                GUI.display_file_loaded_message(is_file_loaded)

            elif choice == '2':     # Print Stats

                if self.data.athletes:
                    players_stats = self.data.get_statistics()
                    GUI.display_stats(players_stats)
                else:
                    GUI.display_file_loaded_message(False)

            elif choice == '3':     # Delete Athlete

                if self.data.athletes:
                    athlete_name = GUI.get_string_input("Enter the name of the athlete: ")
                    atheltes_found = self.data.find_athlete_by_name(athlete_name)
                    if atheltes_found:
                        if len(atheltes_found) > 1:
                            GUI.display_message(f"Multiple athletes found with the name '{athlete_name}'")
                            confirmation = GUI.get_confirmation("Do you want to delete all of them?")
                            if not confirmation:
                                continue
                        self.data.delete_athlete(athlete_name)
                        GUI.display_message(f"Athlete '{athlete_name.title()}' has been deleted successfully.")
                    else:
                        GUI.display_message(f"No athlete found with the name '{athlete_name}'.")
                else:
                    GUI.display_file_loaded_message(False)

            elif choice == '4':     # Save File

                filename = self.data.filename()
                if filename is not None:
                    confirmation = GUI.get_confirmation(f"Do you want to save and overwrite to {filename}?")
                    if not confirmation:
                        continue
                    lines = self.data.save_data()
                    saved_confirmation = save_file(filename, lines)
                    if saved_confirmation:
                        self.data.dirty = False
                    GUI.display_message(f"Data successfully saved to '{filename}'.")
                else:
                    GUI.display_message(f"Invalid filename. Please load a valid file and try again.")

            elif choice == '5':     # Athlete Info

                if self.data.athletes:
                    athlete_name = GUI.get_string_input("Enter the name of the athlete: ")
                    athlete = self.data.get_athlete_info(athlete_name)
                    GUI.display_athlete_info(athlete)
                else:
                    GUI.display_file_loaded_message(False)
                
            elif choice == '6':     # Display Chart

                if not self.data.athletes:
                    GUI.display_file_loaded_message(False)
                    continue
                
                data = None
                title = None
                while True:
                    sub_menu_choice = GUI.get_chart_menu_choice()

                    if sub_menu_choice == '1':
                        data = self.data.get_level_1_athlete_counts()
                        title = "Number of Athletes (Level 1 Classes)"
                        break
                    elif sub_menu_choice == '2':
                        data = self.data.get_leaf_athlete_counts()
                        title = "Number of Athletes (Leaf Level Classes)"
                        break
                    elif sub_menu_choice == '3':
                        data = self.data.get_level_1_athlete_average_salary()
                        title = "Average salary (Level 1 Classes)"
                        break
                    elif sub_menu_choice == '4':
                        data = self.data.get_leaf_level_athlete_average_salary()
                        title = "Average salary (Leaf Level Classes)"
                        break
                    elif sub_menu_choice == '5':
                        data = self.data.get_endorsement_counts()
                        title = "Number of Endorsements"
                        break
                    else:
                        GUI.display_message("Invalid input, please try again.")
                        continue
                if data is not None:
                    GUI.display_pie_chart(data, title)
                    
            elif choice == '7':     # Exit

                if self.data.dirty:
                    GUI.display_message("Warning: You have unsaved changes. If you exit now, all changes will be lost.")
                    confirmation = GUI.get_confirmation(f"Do you still want to exit?")
                    if not confirmation:
                        continue
                GUI.display_exit_app_message()
                break

            # For debugging
            # elif choice == '0':
            #     GUI.displat_all_athletes_stats(self.data.athletes)

            else:
                GUI.display_invalid_input_message_main_menu()


if __name__ == "__main__":
    app = AthletesManagerApp()
    app.run()
