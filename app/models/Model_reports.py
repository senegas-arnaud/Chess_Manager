import json
from pathlib import Path


class Model_reports:

    def __init__(self):
        self.tournaments_file = Path(r'Data\tournament_data.json')
        self.players_file = Path(r'Data\player_data.json')

    def load_tournaments(self):
        if self.tournaments_file.exists():
            with open(self.tournaments_file, 'r', encoding='utf-8') as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return []
        return []

    def load_players(self):
        if self.players_file.exists():
            with open(self.players_file, 'r', encoding='utf-8') as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return []
        return []

    def get_tournament_by_index(self, tournaments, index):
        if 1 <= index <= len(tournaments):
            return tournaments[index - 1]
        return None

    def get_player_name(self, player_id, all_players):
        for player in all_players:
            if player['national_id'] == player_id:
                return f"{player['name']} {player['surname']}"
        return "Unknown Player"
