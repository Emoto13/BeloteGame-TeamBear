import unittest
from Player import Player
from Team import Team
from Game import Game


class TestGameClass(unittest.TestCase):

    def test_if_constructor_sets_attributes_correctly(self):
        player1 = Player(name='Marto')
        player2 = Player(name='Rado')
        team1 = Team(team_name='Mechetata', player1=player1, player2=player2)

        player3 = Player(name='Gosho')
        player4 = Player(name='Pesho')
        team2 = Team(team_name='Kotetata', player1=player3, player2=player4)
        g = Game(game_id=1, team1=team1, team2=team2)

        self.assertEqual(g.game_id, 'game 1')
        self.assertEqual(g.team1, team1)
        self.assertEqual(g.team2, team2)


if __name__ == '__main__':
    unittest.main()
