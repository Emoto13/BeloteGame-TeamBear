import unittest
from entities.player import Player
from entities.team import Team


class TestTeamClass(unittest.TestCase):
    def test_if_constructor_sets_attributes_correctly(self):
        player1 = Player(name='Marto')
        player2 = Player(name='Rado')
        team = Team(player1=player1, player2=player2)

        self.assertEqual(team.team_name, 'Team')
        self.assertIs(player1, team.player1)
        self.assertIs(player2, team.player2)

    def test_if_clear_announcements_works_correctly(self):
        player1 = Player(name='Marto')
        player1.set_hand(['10h', 'Jh', 'Qh'])
        player2 = Player(name='Rado')
        player2.set_hand(['7s', '8s', '9s'])
        team = Team(player1=player1, player2=player2)
        team.clear_announcements()

        self.assertEqual(team.player1.get_announcements(), [])
        self.assertEqual(team.player2.get_announcements(), [])

    def test_if_to_dict_works_correctly(self):
        pass

    def test_if_to_json_works_correctly(self):
        pass


if __name__ == '__main__':
    unittest.main()
