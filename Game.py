from Player import Player
from Team import Team
from Round import Round
from utils import game_end
from cards import cards
import random


class Game:
    def __init__(self, game_id: int, team1: Team = None, team2: Team = None):  # takes teams
        self.id = f'game : {game_id}'
        self.team1 = team1
        self.team2 = team2

    def play_game(self):
        round_id = 1
        while not game_end(self.team1.team_points, self.team2.team_points):

            self.set_player_hands()
            r = Round(round_id, self.team1, self.team2)
            r.compare_best_announcements()
            r.clear_announcements_for_round()
            round_id += 1

    def set_player_hands(self):
        random.shuffle(cards)
        self.team1.player1.set_hand(cards[:8])
        self.team1.player2.set_hand(cards[8:16])
        self.team2.player1.set_hand(cards[16:24])
        self.team2.player2.set_hand(cards[24:])


    # @staticmethod
    # def to_dict(current_round):
    #     dicts = {
    #         current_round.id: current_round.to_dict()
    #     }

    #     return dicts

    # def to_json(self):
    #     dicts = {self.id: {
    #         self.current_round.id: self.current_round.to_dict()
    #     }
    #     }
    #     json_repr = json.dumps(dicts, indent=4)
    #     return format_json(json_repr)


def main():
    player1 = Player(name='Marto')
    player2 = Player(name='Rado')
    team1 = Team(team_name='Mechetata', player1=player1, player2=player2)

    player3 = Player(name='Gosho')
    player4 = Player(name='Pesho')
    team2 = Team(team_name='Kotetata', player1=player3, player2=player4)
    g = Game(game_id=1, team1=team1, team2=team2)

    g.play_game()
    print(team1.team_points)
    print(team2.team_points)
    # print(team2.player1.get_announcements())
    # print(team2.player2.get_announcements())
    # print(team2.team_points)
    # print(g.to_json())


if __name__ == '__main__':
    main()
