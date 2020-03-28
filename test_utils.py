import unittest
import json
from utils import format_json, best_announcement, check_highest_card


class TestUtils(unittest.TestCase):
    def test_if_format_json_works_correctly(self):
        dicts = {
            "cards": ['7h', '8c', '9d', '10s', 'Jh', 'Qh', 'Kh'],
            "announcements": ['belot', 'triece'],
            "points": 40}

        exp = "{\n    \"cards\": [\"7h\", \"8c\", \"9d\", \"10s\", \"Jh\", \"Qh\", \"Kh\"],\n    \"announcements\": [" \
              "\"belot\", \"triece\"]," \
              "\n    \"points\": 40\n}"

        json_repr = json.dumps(dicts, indent=4)
        json_repr = format_json(json_repr)
        self.assertEqual(exp, json_repr)

    def test_if_best_announcement_works_when_there_are_no_announcements(self):
        pass

    def test_if_best_announcement_works_for_announcements_with_different_length(self):
        pass

    def test_if_best_announcement_works_for_player_announcements_with_the_same_length(self):
        pass

    def test_if_best_announcement_works_for_team_announcements_with_the_same_length(self):
        pass

    def test_if_check_highest_card_works_for_player_announcements_with_the_same_length(self):
        pass
