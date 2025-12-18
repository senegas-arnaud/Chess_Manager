from app.views.View_menu import View_menu
from app.controllers.Controller_player_info import Controller_player_info
from rich.console import Console

class Controller_menu:

    def __init__(self):
        self.view = View_menu()
        self.player_controller = Controller_player_info()
        self.console = Console()
    def main_menu(self):
        self.console.clear()
        while True:
            choice = self.view.display_main_menu()
            if choice == "0":
                break
            elif choice == "1":
                self.player_controller.add_player()
                pass
            elif choice == "2":
                # Logic to list all players
                pass
            elif choice == "3":
                # Logic to create a tournament
                pass
            elif choice == "4":
                # Logic to manage tournament
                pass
            elif choice == "5":
                # Logic for reports
                pass