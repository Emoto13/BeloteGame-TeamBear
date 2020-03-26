import unittest
from Player import Player


class TestPlayerClass(unittest.TestCase):

    def test_if_constructor_sets_attributes_correctly(self):
        name = 'Niki'
        hand = ['7s', '8d', '9s', '10c', 'Qd', 'Qh', 'As', 'Ah']
        player = Player(name=name, hand=hand)
        self.assertEqual(player.name, name)
        self.assertEqual(player.hand, hand)

    def test_check_if_hand_contains_belots_works_with_belots(self):
        player = Player()
        player.check_if_hand_contains_belots(['Qs', 'Ks'])

        self.assertEqual(player.points, 20)
        self.assertEqual(player.belots, [['Qs', 'Ks']])

    def test_check_if_hand_contains_multiple_belots(self):
        player = Player()
        player.check_if_hand_contains_belots(['Qs', 'Ks', 'Qh', 'Kh'])

        self.assertEqual(player.points, 40)
        self.assertEqual(player.belots, [['Qs', 'Ks'], ['Qh', 'Kh']])

    def test_check_if_hand_has_zero_belots(self):
        pl = Player()
        pl.check_if_hand_contains_belots(['7s', '8d', '9s', '10c', 'Qd', 'Qh', 'As', 'Ah'])

        self.assertEqual(pl.points, 0)
        self.assertEqual(pl.belots, [])

    def test_check_if_hand_contains_carre_finds_low_carre_and_adds_points(self):
        player = Player()
        res = player.check_if_hand_contains_carres({'7s', '8d', 'Qs', 'Qc', 'Qd', 'Qh', 'As', 'Ah'})

        exp = {'7s', '8d', 'As', 'Ah'}

        self.assertEqual(res, exp)
        self.assertEqual(player.points, 100)
        self.assertEqual(player.carres, [['Qs', 'Qc', 'Qd', 'Qh']])

    def test_check_if_hand_contains_carre_finds_two_highest_carre_and_adds_points(self):
        pl = Player()

        res = pl.check_if_hand_contains_carres({'9s', '9c', '9d', '9h', 'Js', 'Jh', 'Jc', 'Jd'})
        exp = set()

        self.assertEqual(res, exp)
        self.assertEqual(pl.points, 350)
        self.assertEqual(pl.carres, [['9s', '9c', '9d', '9h'], ['Js', 'Jc', 'Jd', 'Jh']])

    def test_check_if_hand_contains_carre_works_with_zero_carre(self):
        pl = Player()
        res = pl.check_if_hand_contains_carres({'8s', '9c', '10d', 'Jh', 'Qs', 'Kh', 'Ac', 'Ad'})
        exp = {'8s', '9c', '10d', 'Jh', 'Qs', 'Kh', 'Ac', 'Ad'}

        self.assertEqual(res, exp)
        self.assertEqual(pl.points, 0)
        self.assertEqual(pl.carres, [])

    # add edge cases to this test
    def test_if_check_if_hand_contains_quintes_works_correctly(self):
        pass

    # add edge cases to this test
    def test_if_check_if_hand_contains_quartes_works_correctly(self):
        pass

    # add edge cases to this test
    def test_if_check_if_hand_contains_trieces_works_correctly(self):
        pass

    # add edge cases to this test
    def test_if_get_announcements_works_correctly(self):
        pass

    # add edge cases to this test
    def test_if_best_declaration_works_correctly(self):
        pass

    # add edge cases to this test
    def test_if_get_points_works_correctly(self):
        pass

    # add edge cases to this test
    def test_if_to_json_works_correctly(self):
        pass


if __name__ == '__main__':
    unittest.main()
