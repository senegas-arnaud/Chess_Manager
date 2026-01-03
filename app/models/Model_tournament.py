import json
from pathlib import Path
from datetime import datetime
import re


class Model_tournament:

    def __init__(self, name, location, beginning_date, ending_date, remarks):
        self.tournament_name = name
        self.tournament_location = location
        self.tournament_beginning_date = beginning_date
        self.tournament_ending_date = ending_date
        self.tournament_max_rounds = 4
        self.current_round = 0
        self.round_history = []
        self.players = []
        self.remarks = remarks
        self.file = Path(r'Data\tournament_data.json')

    def load_tournament_data(self):
        if Path(self.file).exists():
            with open(self.file, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                    return data
                except json.JSONDecodeError:
                    return []
        else:
            return []

    def save_tournament_data(self):
        tournaments = self.load_tournament_data()

        new_tournament_data = {
            "name": self.tournament_name,
            "location": self.tournament_location,
            "beginning_date": self.tournament_beginning_date,
            "ending_date": self.tournament_ending_date,
            "max_rounds": self.tournament_max_rounds,
            "current_round": self.current_round,
            "round_history": self.round_history,
            "players": self.players,
            "remarks": self.remarks
        }

        tournaments.append(new_tournament_data)

        with open(self.file, 'w', encoding='utf-8') as f:
            json.dump(tournaments, f, ensure_ascii=False, indent=4)

        return f"✅ Tournament '{self.tournament_name}' has been successfully created and saved."

    def validate_beginning_date_format(self):
        try:
            datetime.strptime(self.tournament_beginning_date, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def validate_ending_date_format(self):
        try:
            datetime.strptime(self.tournament_ending_date, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def validate_name(self):
        if not (0 < len(self.tournament_name.strip()) < 20):
            return False
        pattern = r'^[a-zA-ZÀ-ÿ0-9\s\-\',\.]+$'
        return bool(re.match(pattern, self.tournament_name.strip()))

    def validate_location(self):
        if not (0 < len(self.tournament_location.strip()) < 100):
            return False
        pattern = r'^[a-zA-ZÀ-ÿ0-9\s\-\',\.]+$'
        return bool(re.match(pattern, self.tournament_location.strip()))

    def validate_remarks(self):
        if len(self.remarks.strip()) == 0:
            return True

        if len(self.remarks.strip()) > 100:
            return False

        pattern = r'^[a-zA-ZÀ-ÿ\s\-\']+$'
        return bool(re.match(pattern, self.remarks.strip()))

    def validate_tournament_info(self):
        errors = []
        if not self.validate_name():
            errors.append("❌ Name must contain only letters and be between 1-20 characters. ❌")
        if not self.validate_location():
            errors.append("❌ Location must contain only numbers and letters and be between 1-100 characters. ❌")
        if not self.validate_remarks():
            errors.append("❌ Remarks must contain only letters and be between 1-100 characters. ❌")
        if not self.validate_beginning_date_format():
            errors.append("❌ Date format is invalid. Use YYYY-MM-DD. ❌")
        else:
            begin_date = datetime.strptime(self.tournament_beginning_date, "%Y-%m-%d")
            if begin_date < datetime.now():
                errors.append("❌ Tournament cannot start in the past. ❌")
        if not self.validate_ending_date_format():
            errors.append("❌ Date format is invalid. Use YYYY-MM-DD. ❌")
        else:
            end_date = datetime.strptime(self.tournament_ending_date, "%Y-%m-%d")
            if end_date < begin_date:
                errors.append("❌ Tournament should end after is beginning. ❌")

        player = self.load_tournament_data()
        if any(n["name"] == self.tournament_name for n in player):
            errors.append(f"❌ A tournament with the name {self.tournament_name} already exist. ❌")
        return errors
