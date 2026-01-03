from app.models.Model_player_info import Model_player_info
from app.views.View_player_info import View_player_info


class Controller_player_info:

    def __init__(self):
        self.view = View_player_info()

    def add_player(self):
        data = self.view.player_info()
        player = Model_player_info(data[0], data[1], data[2], data[3])

        errors = player.check_player_info()
        if errors:
            for error in errors:
                self.view.display_error(error)
        else:
            result = player.add_player_data()
            self.view.display_success(result)
