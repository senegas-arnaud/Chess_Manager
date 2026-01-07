from app.models.Model_tournament import Model_tournament
from app.views.View_tournament import View_tournament
from app.models.Model_player_info import Model_player_info


class Controller_tournament:
    def __init__(self):
        self.view = View_tournament()
        self.model = Model_tournament()
        self.player_model = Model_player_info()

    def create_tournament(self):
        while True:
            data = self.view.tournament_info()
            tournament = Model_tournament(data[0], data[1], data[2], data[3], data[4])

            errors = tournament.validate_tournament_info()
            if errors:
                for error in errors:
                    self.view.display_error(error)

                choice = self.view.display_secondary_menu()

                if choice == "1":
                    # Retry
                    continue
                elif choice == "2":
                    # Go back
                    break
            else:
                result = tournament.save_tournament_data()
                self.view.display_success(result)

                choice = self.view.display_secondary_menu()

                if choice == "1":
                    # Retry
                    continue
                elif choice == "2":
                    # Go back
                    break

    def manage_selected_tournament(self, tournament):
        from app.controllers.Controller_match import Controller_match
        match_controller = Controller_match()

        while True:
            updated_tournament = self.model.get_tournament_by_id(tournament['name'])

            if not updated_tournament:
                self.view.display_error("Tournament not found!")
                input("\n[Press Enter to continue...]")
                break

            all_players = self.player_model.load_player_data()

            choice = self.view.display_tournament_management(updated_tournament, all_players)

            current_round = updated_tournament.get('current_round', 0)

            if current_round > 0:
                if choice == "1":
                    match_controller.manage_current_round(updated_tournament['name'])

                elif choice == "2":
                    self.add_player_to_tournament(updated_tournament, all_players)

                elif choice == "3":
                    self.delete_player_from_tournament(updated_tournament, all_players)

                elif choice == "4":
                    # Go back
                    break
            else:
                if choice == "1":
                    self.add_player_to_tournament(updated_tournament, all_players)

                elif choice == "2":
                    self.delete_player_from_tournament(updated_tournament, all_players)

                elif choice == "3":
                    match_controller.start_tournament(updated_tournament)

                elif choice == "4":
                    # Go back
                    break

    def add_player_to_tournament(self, tournament, all_players):
        while True:
            player_id = self.view.player_registration()

            if player_id == "0" or not player_id:
                break

            errors = self.model.validate_player_registration(
                tournament['name'],
                player_id,
                all_players
            )

            if errors:
                for error in errors:
                    self.view.display_error(error)

                choice = self.view.display_secondary_menu()

                if choice == "1":
                    # Retry
                    continue
                elif choice == "2":
                    # Go back
                    break
            else:
                result = self.model.register_player(tournament['name'], player_id)
                self.view.display_success(result)

                choice = self.view.display_secondary_menu()

                if choice == "1":
                    # Retry
                    continue
                elif choice == "2":
                    # Go back
                    break

    def delete_player_from_tournament(self, tournament, all_players):
        player_id = self.view.select_player_to_delete(tournament, all_players)

        if not player_id:
            return

        result = self.model.delete_player(tournament['name'], player_id)
        self.view.display_success(result)
        input("\n[Press Enter to continue...]")
