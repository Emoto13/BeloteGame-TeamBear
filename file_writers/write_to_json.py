from file_writers.pretty_json import prettyjson
from utils import format_json


class WriteToJSON:
    def __init__(self):
        self.games = {}

    def add_game(self, game_id, dicts):
        self.games[game_id] = dicts

    def to_json(self):
        json_repr = prettyjson(self.games)
        json_repr = format_json(json_repr)
        return json_repr

    def __del__(self):
        with open('data.json', 'w') as file:
            file.write(self.to_json())
