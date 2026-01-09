from app.models.Model_reports import Model_reports
from app.views.View_reports import View_reports


class Controller_reports:

    def __init__(self):
        self.model = Model_reports()
        self.view = View_reports()

    def show_tournament_reports(self):
        while True:
            tournaments = self.model.load_tournaments()

            choice = self.view.display_tournaments_list(tournaments)

            if choice is None:
                break

            selected_tournament = self.model.get_tournament_by_index(tournaments, choice)

            if not selected_tournament:
                self.view.display_error("Invalid tournament selection!")
                input("\n[Press Enter to going back...]")
                continue

            all_players = self.model.load_players()

            self.view.display_tournament_report(selected_tournament, all_players)
