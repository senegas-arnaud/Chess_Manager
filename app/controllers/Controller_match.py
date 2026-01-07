from app.models.Model_match import Model_match
from app.views.View_match import View_match
from app.models.Model_player_info import Model_player_info


class Controller_match:

    def __init__(self):
        self.model = Model_match()
        self.view = View_match()
        self.player_model = Model_player_info()

    def start_tournament(self, tournament):

        if len(tournament['players']) == 0 or len(tournament['players']) % 2 != 0:
            self.view.display_error_even_players()
            return

        if not self.view.display_tournament_start_confirmation(tournament):
            return

        matches = self.model.first_round(tournament['name'])

        if matches:
            self.view.display_success(f"✅ Round 1 created successfully with {len(matches)} matches!")
            input("\n[Press Enter to continue...]")

            self.manage_current_round(tournament['name'])
        else:
            self.view.display_error("❌ Failed to create Round 1.")
            input("\n[Press Enter to continue...]")

    def manage_current_round(self, tournament_name):
        while True:
            tournament = self.model.get_tournament_by_name(tournament_name)

            if not tournament:
                self.view.display_error("Tournament not found!")
                input("\n[Press Enter to continue...]")
                return

            current_round = tournament.get('current_round', 0)
            if current_round == 0:
                self.view.display_info("No round started yet.")
                input("\n[Press Enter to continue...]")
                return

            round_index = current_round - 1
            round_data = tournament['round_history'][round_index]

            all_players = self.player_model.load_player_data()

            self.view.display_round_matches(tournament, round_data, all_players)

            choice = self.view.display_round_menu(tournament)

            if choice == "1":
                self.enter_match_results(tournament, round_data, round_index, all_players)

            elif choice == "2":
                max_rounds = tournament.get('max_rounds', 4)

                if current_round < max_rounds:
                    if self.check_all_results_entered(round_data):
                        self.create_next_round(tournament_name)
                    else:
                        self.view.display_error("❌ Please enter all match results before proceeding.")
                        input("\n[Press Enter to continue...]")
                else:
                    self.view.display_tournament_standings(tournament, all_players)

            elif choice == "3":
                break

    def enter_match_results(self, tournament, round_data, round_index, all_players):
        num_matches = len(round_data['matches'])

        match_number = self.view.select_match_to_update(num_matches)

        if match_number is None or match_number == 0:
            return

        match_index = match_number - 1

        players_dict = {p['national_id']: p for p in all_players}

        match = round_data['matches'][match_index]
        player1_id = match[0][0]
        player2_id = match[1][0]

        player1 = players_dict.get(player1_id, {})
        player2 = players_dict.get(player2_id, {})

        player1_name = f"{player1.get('name', '?')} {player1.get('surname', '?')}"
        player2_name = f"{player2.get('name', '?')} {player2.get('surname', '?')}"

        result = self.view.ask_match_result(player1_name, player2_name)

        if result == "0":
            return

        success = self.model.update_match_result(
            tournament['name'],
            round_index,
            match_index,
            result
        )

        if success:
            self.view.display_success("✅ Match result saved successfully!")
            input("\n[Press Enter to continue...]")
        else:
            self.view.display_error("❌ Failed to save result.")
            input("\n[Press Enter to continue...]")

    def check_all_results_entered(self, round_data):
        for match in round_data['matches']:
            score1 = match[0][1]
            score2 = match[1][1]

            if score1 == 0 and score2 == 0:
                return False

        return True

    def create_next_round(self, tournament_name):
        matches = self.model.next_round_matches(tournament_name)

        if matches:
            tournament = self.model.get_tournament_by_name(tournament_name)
            current_round = tournament.get('current_round', 0)

            self.view.display_success(f"✅ Round {current_round} created successfully with {len(matches)} matches!")
            input("\n[Press Enter to continue...]")
        else:
            self.view.display_error("❌ Failed to create next round.")
            input("\n[Press Enter to continue...]")
