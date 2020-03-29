import unittest
from Player import Player
from Team import Team
from Round import Round



class TestRoundClass(unittest.TestCase):

    def test_if_constructor_sets_attributes_correctly(self):
        player1 = Player(name='Marto')
        player2 = Player(name='Rado')
        team1 = Team(player1=player1, player2=player2)
        player3 = Player(name='Gosho')
        player4 = Player(name='Pesho')
        team2 = Team(player1=player1, player2=player2)
        r = Round(round_id = 1, team1 = team1, team2 = team2)

        self.assertEqual(r.id, 'round 1')
        self.assertEqual(r.team1,team1)
        self.assertEqual(r.team2,team2)

    def test_if_compare_best_announcments_works_when_all_announcements_check_out(self):
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

        r.compare_best_announcements()

        self.assertEqual(team1.player1.get_announcements(), ['belot'])
        self.assertEqual(team2.player2.get_announcements(), ['belot'])

    def test_if_compare_best_announcements_works_when_team1_has_higher_announcement(self):
        player1 = Player(name='Marto')
        player2 = Player(name='Rado')
        player1.set_hand(['Jh', 'Qh', 'Kh'])
        player2.set_hand(['9d','10d', 'Jd', 'Qd', 'Kd'])
        team1 = Team(team_name='Mechetata', player1=player1, player2=player2)

        player3 = Player(name='Gosho')
        player4 = Player(name='Pesho')
        player3.set_hand(['Jc', 'Qs', 'Ks'])
        player4.set_hand(['9c','10c', 'Js', 'Qc', 'Kc'])
        team2 = Team(team_name='Kotetata', player1=player3, player2=player4)
        r = Round(round_id=1, team1=team1, team2=team2)

        r.compare_best_announcements()
        
        self.assertEqual(team1.player1.get_announcements(),['belot','triece'])
        self.assertEqual(team1.player2.get_announcements(),['belot','quinte'])
        self.assertEqual(team2.player1.get_announcements(),['belot'])
        self.assertEqual(team2.player2.get_announcements(),['belot'])

    def test_if_compare_best_announcements_works_when_team2_has_higher_announcement(self):
        player1 = Player(name='Marto')
        player2 = Player(name='Rado')
        player1.set_hand(['Jh', 'Qh', 'Kh'])
        player2.set_hand(['10d', 'Jd', 'Qd', 'Kd'])
        team1 = Team(team_name='Mechetata', player1=player1, player2=player2)

        player3 = Player(name='Gosho')
        player4 = Player(name='Pesho')
        player3.set_hand(['Js', 'Qs', 'Ks'])
        player4.set_hand(['9c','10c', 'Jc', 'Qc', 'Kc'])
        team2 = Team(team_name='Kotetata', player1=player3, player2=player4)
        r = Round(round_id=1, team1=team1, team2=team2)

        r.compare_best_announcements()
        
        self.assertEqual(team1.player1.get_announcements(),['belot'])
        self.assertEqual(team1.player2.get_announcements(),['belot'])
        self.assertEqual(team2.player1.get_announcements(),['belot','triece'])
        self.assertEqual(team2.player2.get_announcements(),['belot','quinte'])

    def test_if_clear_announcements_for_round_works_as_expected(self):
        player1 = Player(name='Marto')
        player2 = Player(name='Rado')
        player1.set_hand(['Jh', 'Qh', 'Kh'])
        player2.set_hand(['10d', 'Jd', 'Qd', 'Kd'])
        team1 = Team(team_name='Mechetata', player1=player1, player2=player2)

        player3 = Player(name='Gosho')
        player4 = Player(name='Pesho')
        player3.set_hand(['Js', 'Qs', 'Ks'])
        player4.set_hand(['9c','10c', 'Jc', 'Qc', 'Kc'])
        team2 = Team(team_name='Kotetata', player1=player3, player2=player4)
        r = Round(round_id=1, team1=team1, team2=team2)

        r.compare_best_announcements()
        r.clear_announcements_for_round()

        self.assertEqual(team2.player1.belots, [])
        self.assertEqual(team2.player1.trieces, [])
        self.assertEqual(team2.player2.belots, [])
        self.assertEqual(team2.player2.quintes, [])


if __name__ == '__main__':
    unittest.main()