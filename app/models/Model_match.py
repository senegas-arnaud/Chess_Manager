import json
from pathlib import Path
from datetime import datetime
import random


class Model_match:

    def __init__(self):
        self.file = Path(r'Data\tournament_data.json')

    def load_tournament_data(self):
        if self.file.exists():
            with open(self.file, 'r', encoding='utf-8') as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return []
        return []

    def save_tournament_data(self, tournaments):
        with open(self.file, 'w', encoding='utf-8') as f:
            json.dump(tournaments, f, ensure_ascii=False, indent=4)

    def get_tournament_by_name(self, tournament_name):
        tournaments = self.load_tournament_data()
        for tournament in tournaments:
            if tournament['name'] == tournament_name:
                return tournament
        return None

    def first_round(self, tournament_name):
        tournaments = self.load_tournament_data()

        for tournament in tournaments:
            if tournament['name'] == tournament_name:
                players = tournament['players'][:]
                random.shuffle(players)

                matches = []
                for i in range(0, len(players), 2):
                    player1_id = players[i]
                    player2_id = players[i + 1]

                    match = [[player1_id, 0], [player2_id, 0]]
                    matches.append(match)

                new_round = {
                    "name": "Round 1",
                    "start_time": datetime.now().isoformat(),
                    "end_time": None,
                    "matches": matches
                }

                if 'round_history' not in tournament:
                    tournament['round_history'] = []

                tournament['round_history'].append(new_round)
                tournament['current_round'] = 1

                if 'player_scores' not in tournament:
                    tournament['player_scores'] = {}

                for player_id in tournament['players']:
                    if player_id not in tournament['player_scores']:
                        tournament['player_scores'][player_id] = 0

                tournament['status'] = "in progress"
                self.save_tournament_data(tournaments)

                return matches

        return None

    def sort_players_by_score(self, tournament):
        player_scores = tournament.get('player_scores', {})

        sorted_players = sorted(
            tournament['players'],
            key=lambda player_id: player_scores.get(player_id, 0),
            reverse=True
        )

        return sorted_players

    def already_played_matches(self, tournament, player1_id, player2_id):
        for round_data in tournament.get('round_history', []):
            for match in round_data.get('matches', []):
                match_player1 = match[0][0]
                match_player2 = match[1][0]

                if (match_player1 == player1_id and match_player2 == player2_id) or \
                   (match_player1 == player2_id and match_player2 == player1_id):
                    return True

        return False

    def next_round_matches(self, tournament_name):
        tournaments = self.load_tournament_data()

        for tournament in tournaments:
            if tournament['name'] == tournament_name:
                sorted_players = self.sort_players_by_score(tournament)

                matches = []
                used = set()

                for player in sorted_players:
                    if player in used:
                        continue

                    opponent = None
                    for potential_opponent in sorted_players:
                        if potential_opponent not in used and not self.already_played_matches(
                                tournament, player, potential_opponent) and potential_opponent != player:
                            opponent = potential_opponent
                            break

                    # Make rematch if necessary
                    if not opponent:
                        for potential_opponent in sorted_players:
                            if potential_opponent != player and potential_opponent not in used:
                                opponent = potential_opponent
                                break

                    if opponent:
                        match = [[player, 0], [opponent, 0]]
                        matches.append(match)
                        used.add(player)
                        used.add(opponent)

                current_round = tournament.get('current_round', 0)
                new_round = {
                    "name": f"Round {current_round + 1}",
                    "start_time": datetime.now().isoformat(),
                    "end_time": None,
                    "matches": matches
                }

                tournament['round_history'].append(new_round)
                tournament['current_round'] = current_round + 1

                self.save_tournament_data(tournaments)

                return matches

        return None

    def update_match_result(self, tournament_name, round_index, match_index, result):
        tournaments = self.load_tournament_data()

        for tournament in tournaments:
            if tournament['name'] == tournament_name:
                round_data = tournament['round_history'][round_index]
                match = round_data['matches'][match_index]

                player1_id = match[0][0]
                player2_id = match[1][0]

                old_score1 = match[0][1]
                old_score2 = match[1][1]

                if result == "1":
                    match[0][1] = 1
                    match[1][1] = 0
                elif result == "2":
                    match[0][1] = 0
                    match[1][1] = 1
                elif result == "3":
                    match[0][1] = 0.5
                    match[1][1] = 0.5

                tournament['player_scores'][player1_id] -= old_score1
                tournament['player_scores'][player1_id] += match[0][1]

                tournament['player_scores'][player2_id] -= old_score2
                tournament['player_scores'][player2_id] += match[1][1]

                self.save_tournament_data(tournaments)

                if self.is_round_complete(round_data):
                    self.end_round(tournament_name)

                    current_round = tournament['current_round']
                    max_rounds = tournament.get('max_rounds', 4)

                    if current_round >= max_rounds:
                        self.finish_tournament(tournament_name)

                return True

        return False

    def is_round_complete(self, round_data):
        for match in round_data['matches']:
            if match[0][1] == 0 and match[1][1] == 0:
                return False
        return True

    def end_round(self, tournament_name):
        tournaments = self.load_tournament_data()

        for tournament in tournaments:
            if tournament['name'] == tournament_name:
                round_index = tournament['current_round'] - 1
                round_data = tournament['round_history'][round_index]

                if all(not (scores[0][1] == 0 and scores[1][1] == 0) for scores in round_data['matches']):
                    round_data['end_time'] = datetime.now().isoformat()
                    self.save_tournament_data(tournaments)
                    return True

        return False

    def finish_tournament(self, tournament_name):
        tournaments = self.load_tournament_data()

        for tournament in tournaments:
            if tournament['name'] == tournament_name:
                tournament['status'] = "done"

                player_scores = tournament.get('player_scores', {})

                if player_scores:
                    max_score = max(player_scores.values())

                    winners = [
                        player_id for player_id, score in player_scores.items()
                        if score == max_score
                    ]

                    tournament['winner'] = winners

                else:
                    tournament['winner'] = None

                self.save_tournament_data(tournaments)

                return True

        return False
