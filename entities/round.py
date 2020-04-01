from file_writers.pretty_json import prettyjson
from entities.player import Player
from entities.team import Team
from utils import best_announcement, format_json
import json


class Round:
    def __init__(self, round_id: int = 1, team1: Team = None, team2: Team = None, contract='All Trumps'):
        self.round_id = f'round {round_id}'
        self.team1 = team1
        self.team2 = team2
        self.contract = contract

    def compare_best_announcements(self):
        team1_best_announcement = self.team1.best_announcement()
        team2_best_announcement = self.team2.best_announcement()

        better_announcement = best_announcement(self.team1, self.team2)

        if better_announcement is None:
            self.team1.clear_announcements()
            self.team2.clear_announcements()

        if better_announcement == team1_best_announcement:
            self.team2.clear_announcements()

        if better_announcement == team2_best_announcement:
            self.team1.clear_announcements()

        self.team1.set_points_for_team()
        self.team2.set_points_for_team()

    def clear_scoring_for_round(self):
        self.team1.clear_scoring_for_round()
        self.team2.clear_scoring_for_round()

    def to_dict(self):
        dicts = {
            "contract": self.contract,
            self.team1.team_name: self.team1.to_dict(),
            self.team2.team_name: self.team2.to_dict()
        }

        return dicts

    def to_json(self):
        dicts = {
            self.team1.team_name: self.team1.to_dict(),
            self.team2.team_name: self.team2.to_dict(),
            "contract": self.contract,

        }

        json_repr = json.dumps(dicts, indent=4)
        return format_json(json_repr)

    @classmethod
    def create_copy(cls):
        return cls


def main():
    player1 = Player(name='Marto')
    player2 = Player(name='Rado')
    player1.set_hand(['Jh', 'Qh', 'Kh'])
    player2.set_hand(['10d', 'Jd', 'Qd', 'Kd'])
    team1 = Team(team_name='Mechetata', player1=player1, player2=player2)

    player3 = Player(name='Gosho')
    player4 = Player(name='Pesho')
    player3.set_hand(['Js', 'Qs', 'Ks'])
    player4.set_hand(['10c', 'Jc', 'Qc', 'Kc'])
    team2 = Team(team_name='Kotetata', player1=player3, player2=player4)
    r = Round(round_id=1, team1=team1, team2=team2)

    print(team1.best_announcement())
    print(team2.best_announcement())
    print(r.compare_best_announcements())
    print(team1.player1.get_announcements(), team1.player2.get_announcements())

    print(prettyjson(r.to_dict()))


if __name__ == '__main__':
    main()
