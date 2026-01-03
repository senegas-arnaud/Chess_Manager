from app.models.Model_tournament import Model_tournament
from app.views.View_tournament import View_tournament


class Controller_tournament:
    def __init__(self):
        self.view = View_tournament()

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
