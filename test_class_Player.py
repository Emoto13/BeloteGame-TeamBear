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
    def test_if_check_if_hand_contains_quintes_works_correctly_when_there_is_a_quinte(self):
        player = Player()
        res = player.check_if_hand_contains_quintes({'10h', 'Jh', 'Qh', 'Kh', 'Ah'})
        exp = set()

        self.assertEqual(res, exp)
        self.assertEqual(player.quintes, [['10h', 'Jh', 'Qh', 'Kh', 'Ah']])

    def test_if_check_if_hand_contains_quintes_works_correctly_when_there_is_no_quinte(self):
        player = Player()
        res = player.check_if_hand_contains_quintes({'10h', 'Jh', 'Qc', 'Kc', 'As'})
        exp = {'10h', 'Jh', 'Qc', 'Kc', 'As'}

        self.assertEqual(res, exp)
        self.assertEqual(player.quintes, [])

    # add edge cases to this test
    def test_if_check_if_hand_contains_quartes_works_correctly_when_there_is_a_quarte(self):
        player = Player()
        res = player.check_if_hand_contains_quartes({'10c', 'Jc', 'Qc', 'Kc'})
        exp = set()

        self.assertEqual(res, exp)
        self.assertEqual(player.quartes, [['10c', 'Jc', 'Qc', 'Kc']])

    def test_if_check_if_hand_contains_quartes_works_correctly_when_there_is_not_quarte(self):
        player = Player()
        res = player.check_if_hand_contains_quartes({'10c', 'Jc', 'Qc', 'Kh'})
        exp = {'10c', 'Jc', 'Qc', 'Kh'}

        self.assertEqual(res, exp)
        self.assertEqual(player.quartes, [])

    def test_if_check_if_hand_contains_quartes_works_correctly_when_there_are_multiple_quartes(self):
        player = Player()
        res = player.check_if_hand_contains_quartes({'10c', 'Jc', 'Qc', 'Kc', '10h', 'Jh', 'Qh', 'Kh'})
        exp = set()

        self.assertEqual(res, exp)
        self.assertEqual(player.quartes, [['10c', 'Jc', 'Qc', 'Kc'], ['10h', 'Jh', 'Qh', 'Kh']])

    # add edge cases to this test
    def test_if_check_if_hand_contains_trieces_works_correctly_when_there_is_a_triece(self):
        player = Player()
        res = player.check_if_hand_contains_trieces({'10c', 'Jc', 'Qc'})
        exp = set()

        self.assertEqual(res, exp)
        self.assertEqual(player.trieces, [['10c', 'Jc', 'Qc']])

    def test_if_check_if_hand_contains_trieces_works_correctly_when_there_is_not_triece(self):
        player = Player()
        res = player.check_if_hand_contains_trieces({'10c', 'Jc', 'Qh', 'Kh'})
        exp = {'10c', 'Jc', 'Qh', 'Kh'}

        self.assertEqual(res, exp)
        self.assertEqual(player.trieces, [])

    def test_if_check_if_hand_contains_trieces_works_correctly_when_there_are_multiple_trieces_triece(self):
        player = Player()
        res = player.check_if_hand_contains_trieces({'10c', 'Jc', 'Qc', 'Jh', 'Qh', 'Kh'})
        exp = set()

        self.assertEqual(res, exp)
        self.assertEqual(player.trieces, [['Jh', 'Qh', 'Kh'], ['10c', 'Jc', 'Qc']])

    # add edge cases to this test
    def test_if_get_announcements_works_correctly_when_there_are_different_announcements(self):
        player = Player()
        player.set_hand(['10c', 'Jc', 'Qc', '10h', 'Jh', 'Qh', 'Kh'])
        res = ['belot', 'quarte', 'triece']

        self.assertEqual(res, player.get_announcements())

    def test_if_get_announcements_works_correctly_when_there_are_announcements_of_same_type(self):
        player = Player()
        player.set_hand(['10c', 'Jc', 'Qc', 'Jh', 'Qh', 'Kh'])
        res = ['belot', 'triece', 'triece']

        self.assertEqual(res, player.get_announcements())

    # add edge cases to this test
    def test_if_best_declaration_works_correctly_when_all_announcements_are_different(self):
        player = Player()
        player.set_hand((['10c', 'Jc', 'Qc', 'Kc', 'Qh', 'Kh', 'Ah']))
        res = ['10c', 'Jc', 'Qc', 'Kc']
        self.assertEqual(res, player.best_announcement())

    def test_if_best_declaration_works_correctly_when_there_are_announcements_of_the_same_type(self):
        player = Player()
        player.set_hand((['10c', 'Jc', 'Qc', 'Kc', 'Jh', 'Qh', 'Kh', 'Ah']))
        res = ['Jh', 'Qh', 'Kh', 'Ah']

        self.assertEqual(res, player.best_announcement())

        # add edge cases to this test
    def test_if_clear_points_works_correctly(self):
        player = Player()
        player.set_hand(['10c', 'Jc', 'Qc', 'Kc', 'Jh', 'Qh', 'Kh', 'Ah'])
        player.clear_announcements()
        res = ['belot', 'belot']
        self.assertEqual(res, player.get_announcements())

    # add edge cases to this test
    def test_if_get_points_works_correctly(self):
        player = Player()
        player.set_hand(['10c', 'Jc', 'Qc', 'Kc', 'Jh', 'Qh', 'Kh', 'Ah'])
        points = 140
        self.assertEqual(points, player.get_points())

    # add edge cases to this test
    def test_if_to_json_works_correctly(self):
        pass


if __name__ == '__main__':
    unittest.main()
