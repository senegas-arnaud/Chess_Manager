from app.models.Model_match import Model_match
from app.models.Model_player_info import Model_player_info


class Controller_match:

    def __init__(self):
        self.model = Model_match()
        self.player_model = Model_player_info()
