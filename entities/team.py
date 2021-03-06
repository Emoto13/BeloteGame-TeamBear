from entities.player import Player
from utils import best_announcement


class Team:

    def __init__(self, team_name='Team', player1: Player = None, player2: Player = None):
        self.team_name = team_name
        self.player1 = player1
        self.player2 = player2
        self.team_points = 0
        self.games_won = 0

    def best_announcement(self):
        return best_announcement(self.player1, self.player2)

    def clear_announcements(self):
        self.player1.clear_announcements()
        self.player2.clear_announcements()

    def set_points_for_team(self):
        self.team_points += self.player1.set_points() + self.player2.set_points()

    def clear_points(self):
        self.team_points = 0

    def clear_scoring_for_round(self):
        self.player1.clear_scoring_for_round()
        self.player2.clear_scoring_for_round()

    def to_dict(self):
        dicts = {
                self.player1.name: self.player1.to_dict(),
                self.player2.name: self.player2.to_dict()
        }
        return dicts


def main():
    player1 = Player(name='Gosho', hand=['Jd', 'Kd', 'Qd', '10c', 'Ah'])
    player2 = Player(name='Pesho')
    player2.set_hand(['Jc', 'Kc', 'Qh', '10s', 'Ad'])
    tm = Team('Mechkite', player1, player2)
    # print(tm.best_announcement())


if __name__ == '__main__':
    main()
