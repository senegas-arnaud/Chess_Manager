from app.views.View_menu import View_menu
from app.controllers.Controller_player_info import Controller_player_info
from app.controllers.Controller_tournament import Controller_tournament
from app.models.Model_player_info import Model_player_info
from app.models.Model_tournament import Model_tournament
import os


class Controller_menu:

    def __init__(self):
        self.view = View_menu()
        self.player_controller = Controller_player_info()
        self.tournament_controller = Controller_tournament()
        self.player_model = Model_player_info()
        self.tournament_model = Model_tournament()

    def main_menu(self):
        while True:
            choice = self.view.display_main_menu()

            if choice == "0":
                self.view.exit_message()
                break

            elif choice == "1":
                self.manage_players_menu()

            elif choice == "2":
                self.manage_tournaments_menu()

            elif choice == "3":
                self.view.display_reports_menu()

    def manage_players_menu(self):
        while True:
            players = self.player_model.load_player_data()

            players_sorted = sorted(
                players,
                key=lambda p: (p['name'].lower(), p['surname'].lower())
            )

            choice = self.view.display_players_menu(players_sorted)

            if choice == "1":
                self.player_controller.add_player()

            elif choice == "2":
                os.system('cls' if os.name == 'nt' else 'clear')
                input("\n[Press Enter to continue...]")

            elif choice == "3":
                break

    def manage_tournaments_menu(self):
        while True:
            tournaments = self.tournament_model.get_all_tournaments()

            choice = self.view.display_tournaments_menu(tournaments)

            if choice == "1":
                self.tournament_controller.create_tournament()

            elif choice == "2":
                os.system('cls' if os.name == 'nt' else 'clear')
                input("\n[Press Enter to continue...]")

            elif choice == "3":
                os.system('cls' if os.name == 'nt' else 'clear')
                input("\n[Press Enter to continue...]")

            elif choice == "4":
                if not tournaments:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("\n⚠️  No tournaments available.")
                    input("\n[Press Enter to continue...]")
                    continue

                selected_tournament = self.view.select_tournament_by_index(tournaments)

                if selected_tournament:
                    self.tournament_controller.manage_selected_tournament(selected_tournament)

            elif choice == "5":
                # Go back
                break
