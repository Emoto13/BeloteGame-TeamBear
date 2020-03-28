from Player import Player
from Team import Team
from utils import best_announcement


class Round:
    def __init__(self, round_id, team1: Team = None, team2: Team = None):
        self.id = f'round {round_id}'
        self.team1 = team1
        self.team2 = team2

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


if __name__ == '__main__':
    main()
