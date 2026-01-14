from app.models.Model_player_info import Model_player_info
from app.views.View_player_info import View_player_info


class Controller_player_info:

    def __init__(self):
        self.view = View_player_info()

    def add_player(self):
        while True:
            data = self.view.player_registration()

            if data is None:
                break

            player = Model_player_info(data[0], data[1], data[2], data[3])

            errors = player.check_player_info()
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
                result = player.add_player_data()
                self.view.display_success(result)

                choice = self.view.display_secondary_menu()

                if choice == "1":
                    # Retry
                    continue
                elif choice == "2":
                    # Go back
                    break

    def list_all_players(self):
        model = Model_player_info()
        players = model.get_sorted_players()
        self.view.display_all_players(players)

    def modify_player(self):
        while True:
            model = Model_player_info()
            players = model.get_sorted_players()
            player_id = self.view.ask_player_id_to_modify(players)

            if player_id == "0" or not player_id:
                break

            current_player = model.get_player_by_id(player_id)

            if not current_player:
                self.view.display_error(f"❌ Player with ID {player_id} not found! ❌")
                choice = self.view.display_secondary_menu()

                if choice == "1":
                    continue
                elif choice == "2":
                    break
            else:
                data = self.view.player_modification_form(current_player)

                player = Model_player_info(data[0], data[1], data[2], data[3])

                errors = player.check_player_info()
                if errors:
                    for error in errors:
                        self.view.display_error(error)

                    choice = self.view.display_secondary_menu()

                    if choice == "1":
                        continue
                    elif choice == "2":
                        break
                else:
                    result = player.update_player_data(
                        current_player['national_id'],
                        data[0],
                        data[1],
                        data[2],
                        data[3]
                    )
                    self.view.display_success(result)

                    choice = self.view.display_secondary_menu()

                    if choice == "1":
                        continue
                    elif choice == "2":
                        break
