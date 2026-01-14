import json
from pathlib import Path
from datetime import datetime
import re


class Model_player_info:

    def __init__(self, name="", surname="", birthday="", national_id=""):
        self.player_name = name
        self.player_surname = surname
        self.player_date = birthday
        self.player_id = national_id
        self.file = Path('Data\\player_data.json')

    def check_birthday_format(self):
        try:
            datetime.strptime(self.player_date, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def check_id_format(self):
        pattern = r'^[A-Z]{2}\d{5}$'
        return bool(re.match(pattern, self.player_id))

    def check_name(self):
        if not (0 < len(self.player_name.strip()) < 30):
            return False
        pattern = r'^[a-zA-ZÀ-ÿ\s\-\']+$'
        return bool(re.match(pattern, self.player_name.strip()))

    def check_surname(self):
        if not (0 < len(self.player_surname.strip()) < 30):
            return False
        pattern = r'^[a-zA-ZÀ-ÿ\s\-\']+$'
        return bool(re.match(pattern, self.player_surname.strip()))

    def check_player_info(self):
        errors = []
        if not self.check_name():
            errors.append("❌ Name must contain only letters and be between 1-20 characters. ❌")
        if not self.check_surname():
            errors.append("❌ Surname must contain only letters and be between 1-20 characters. ❌")
        if not self.check_birthday_format():
            errors.append("❌ Date format is invalid. Use YYYY-MM-DD. ❌")
        else:
            date = datetime.strptime(self.player_date, "%Y-%m-%d")
            if date > datetime.now():
                errors.append("❌ Birthday cannot be in the future. ❌")
        if not self.check_id_format():
            errors.append("❌ National ID format is invalid. Use 2 letters followed by 5 digits. ❌")
        player = self.load_player_data()
        if any(n["national_id"] == self.player_id for n in player):
            errors.append(f"❌ An other player with ID {self.player_id} already exist. ❌")
        return errors

    def load_player_data(self):
        if Path(self.file).exists():
            try:
                with open(self.file, 'r') as file:
                    data = json.load(file)
                return data
            except json.JSONDecodeError:
                return None
        else:
            return []

    def add_player_data(self):
        errors = self.check_player_info()
        if errors:
            return "\n".join(errors)

        player = self.load_player_data()

        new_player_data = {
            "name": self.player_name,
            "surname": self.player_surname,
            "birthday": self.player_date,
            "national_id": self.player_id,
        }

        player.append(new_player_data)

        with open(self.file, 'w', encoding='utf-8') as file:
            json.dump(player, file, indent=2, ensure_ascii=False)

        return f"✅ {self.player_name} {self.player_surname} successfully added !"

    def get_sorted_players(self):
        players = self.load_player_data()

        if not players:
            return []

        sorted_players = sorted(
            players,
            key=lambda p: (p['name'].lower(), p['surname'].lower())
        )

        return sorted_players

    def update_player_data(self, old_national_id, new_name, new_surname, new_birthday, new_national_id):
        players = self.load_player_data()

        for player in players:
            if player['national_id'] == old_national_id:
                player['name'] = new_name
                player['surname'] = new_surname
                player['birthday'] = new_birthday
                player['national_id'] = new_national_id

                with open(self.file, 'w', encoding='utf-8') as f:
                    json.dump(players, f, ensure_ascii=False, indent=4)

                return "✅ Player information updated successfully! ✅"

        return "❌ Player not found. ❌"

    def get_player_by_id(self, national_id):
        players = self.load_player_data()

        for player in players:
            if player['national_id'] == national_id:
                return player

        return None
