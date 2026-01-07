from app.models.Model_tournament import Model_tournament
from app.views.View_tournament import View_tournament
from app.models.Model_player_info import Model_player_info


class Controller_tournament:
    def __init__(self):
        self.view = View_tournament()
        self.model = Model_tournament()
        self.player_model = Model_player_info()

    def create_tournament(self):
        data = self.view.tournament_info()
        tournament = Model_tournament(data[0], data[1], data[2], data[3], data[4])

        errors = tournament.validate_tournament_info()
        if errors:
            for error in errors:
                self.view.display_error(error)
        else:
            result = tournament.save_tournament_data()
            self.view.display_success(result)

    def register_player_for_tournament(self):
        tournaments = self.model.get_all_tournaments()

        if not tournaments:
            self.view.no_tournament()
            return

        selected_tournament = self.view.display_and_select_tournaments(tournaments)

        if not selected_tournament:
            return

        while True:
            tournament = self.model.get_tournament_by_id(selected_tournament['name'])

            all_players = self.player_model.load_player_data()

            choice = self.view.display_tournament_management(tournament, all_players)

            if choice == "1":
                self.add_player_to_tournament(tournament)

            elif choice == "2":
                self.delete_player_from_tournament(tournament, all_players)

            elif choice == "3":
                break

    def add_player_to_tournament(self, tournament):
        player_id = self.view.player_registration()

        if player_id.upper() == "0" or not player_id:
            return

        player_id = player_id.upper().strip()

        all_players = self.player_model.load_player_data()

        errors = self.model.validate_player_registration(
            tournament['name'],
            player_id,
            all_players
        )

        if errors:
            for error in errors:
                self.view.display_error(error)
            input("\n[Press Enter to continue...]")
        else:
            result = self.model.register_player(tournament['name'], player_id)
            self.view.display_success(result)
            input("\n[Press Enter to continue...]")

    def delete_player_from_tournament(self, tournament, all_players):
        player_id = self.view.select_player_to_delete(tournament, all_players)

        if not player_id:
            return

        result = self.model.delete_player(tournament['name'], player_id)
        self.view.display_success(result)
        input("\n[Press Enter to continue...]")
