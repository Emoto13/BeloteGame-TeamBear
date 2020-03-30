from Player import Player
from Team import Team
from Round import Round
from utils import is_game_won, clear_team_points, format_json
from cards import cards
from contracts import contracts
from WriteToTxt import WriteToTxt
from pretty_json import prettyjson
from WriteToJSON import WriteToJSON

import random


class Game:
    def __init__(self, game_id: int, team1: Team = None, team2: Team = None,
                 write_to_txt: WriteToTxt = None, write_to_json : WriteToJSON = None):  # takes teams
        self.game_id = f'game {game_id}'
        self.team1 = team1
        self.team2 = team2
        self.write_to_txt = write_to_txt
        self.write_to_json = write_to_json
        self.dicts = {}

    def play_game(self):
        round_id = 1

        while not is_game_won(self.team1, self.team2):
            contract = self.set_contract()

            r = Round(round_id, self.team1, self.team2, contract=contract)
            r.compare_best_announcements()

            self.write_to_txt.write_results(self.team1.team_points, self.team2.team_points, round_id)
            self.dicts[r.round_id] = r.to_dict()

            r.clear_scoring_for_round()
            round_id += 1

        self.write_to_txt.write_game_end_output(self.team1, self.team2)
        self.write_to_json.add_game(self.game_id, self.to_dict())

        clear_team_points(self.team1, self.team2)

    def set_contract(self):
        contract = random.choice(contracts)
        random.shuffle(cards)
        self.team1.player1.set_hand(cards[:8], contract)
        self.team1.player2.set_hand(cards[8:16], contract)
        self.team2.player1.set_hand(cards[16:24], contract)
        self.team2.player2.set_hand(cards[24:], contract)
        return contract

    def to_dict(self):
        return self.dicts

    def to_json(self):
        dicts = {self.game_id: self.dicts}
        json_repr = prettyjson(dicts)
        json_repr = format_json(json_repr)
        return json_repr


def main():
    player1 = Player(name='Marto')
    player2 = Player(name='Rado')
    team1 = Team(team_name='Mechetata', player1=player1, player2=player2)

    player3 = Player(name='Gosho')
    player4 = Player(name='Pesho')
    team2 = Team(team_name='Kotetata', player1=player3, player2=player4)
    w = WriteToTxt(team1, team2)
    g1 = Game(game_id=1, team1=team1, team2=team2, write_to_txt=w)
    g1.play_game()
    g1.to_json()
    g2 = Game(game_id=2, team1=team1, team2=team2, write_to_txt=w)
    g2.play_game()
    g2.to_json()
    # g3 = Game(game_id=3, team1=team1, team2=team2, write_to_txt=w)
    # g3.play_game()
    # print(team2.player1.get_announcements())
    # print(team2.player2.get_announcements())
    # print(team2.team_points)


if __name__ == '__main__':
    main()
