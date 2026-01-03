from app.views.View_menu import View_menu
from app.controllers.Controller_player_info import Controller_player_info
from app.controllers.Controller_tournament import Controller_tournament
from rich.console import Console
import os


class Controller_menu:

    def __init__(self):
        self.view = View_menu()
        self.player_controller = Controller_player_info()
        self.tournament_controller = Controller_tournament()
        self.console = Console()

    def main_menu(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        while True:
            choice = self.view.display_main_menu()
            if choice == "0":
                self.view.exit_message()
                break
            elif choice == "1":
                self.player_controller.add_player()

                while True:
                    sub_choice = self.view.display_secondary_menu()
                    if sub_choice == "1":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        self.player_controller.add_player()
                    elif sub_choice == "2":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        break
                    elif sub_choice == "3":
                        self.view.exit_message()
                        return

            elif choice == "2":
                os.system('cls' if os.name == 'nt' else 'clear')
                self.player_controller.list_all_players()

            elif choice == "3":
                os.system('cls' if os.name == 'nt' else 'clear')
                self.tournament_controller.create_tournament()
                while True:
                    sub_choice = self.view.display_secondary_menu()
                    if sub_choice == "1":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        self.tournament_controller.create_tournament()
                    elif sub_choice == "2":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        break
                    elif sub_choice == "3":
                        self.view.exit_message()
                        return

            elif choice == "4":
                # Register player for a tournament
                pass
            elif choice == "5":
                # Lauch tournament 
                pass
            elif choice == "5":
                # reports
                pass
