import unittest
from Player import Player



class TestPlayer(unittest.TestCase):


	def test_if_Player_creation_works(self):
		pl = Player(name = 'Niki', hand = ['7s','8d','9s','10c','Jh','Qs','Kd','Ad'])


		self.assertTrue(pl)


	def test_if_set_hand_calcs_points_and_declarations_for_round(self):
		pass


	def test_if_set_declarations_calcs_declarations_for_round(self):
		pass


	def test_check_if_hand_countains_bellots_works_with_belots(self):
		pl = Player(name = 'Niki', hand = ['7s','8d','9s','10c','Jh','Qs','Ks','Ad'])

		pl.check_if_hand_contains_belots()

		self.assertEqual(pl.points,20)
		self.assertEqual(pl.belots,[['Qs','Ks']])

	def test_check_if_hand_contains_multiple_belots(self):
		pl = Player(name = 'Niki', hand = ['7s','8d','9s','10c','Qs','Qh','Ks','Kh'])

		pl.check_if_hand_contains_belots()

		self.assertEqual(pl.points,40)
		self.assertEqual(pl.belots,[['Qs','Ks'],['Qh','Kh']])

	def test_check_if_hand_has_zero_belots(self):
		pl = Player(name = 'Niki', hand = ['7s','8d','9s','10c','Qd','Qh','As','Ah'])

		pl.check_if_hand_contains_belots()

		self.assertEqual(pl.points,0)
		self.assertEqual(pl.belots,[])

	def test_check_if_hand_contains_carre_finds_low_carre_and_adds_points(self):
		pl = Player(name = 'Niki', hand = ['7s','8d','Qs','Qc','Qd','Qh','As','Ah'])
		copy_hand = ['7s','8d','Qs','Qc','Qd','Qh','As','Ah']

		res = pl.check_if_hand_contains_carres(copy_hand)

		exp = ['7s','8d','As','Ah']

		self.assertEqual(res,exp)
		self.assertEqual(pl.points,100)
		self.assertEqual(pl.carres,[['Qs','Qc','Qd','Qh']])

	def test_check_if_hand_contains_carre_finds_two_highest_carre_and_adds_points(self):
		pl = Player(name = 'Niki', hand = ['9s','9c','9d','9h','Js','Jh','Jc','Jd'])
		copy_hand = ['9s','9c','9d','9h','Js','Jh','Jc','Jd']

		res = pl.check_if_hand_contains_carres(copy_hand)
		exp = []

		self.assertEqual(res,exp)
		self.assertEqual(pl.points,350)
		self.assertEqual(pl.carres,[['9s', '9c', '9d', '9h'], ['Js', 'Jc', 'Jd', 'Jh']])
		

	def test_check_if_hand_contains_carre_works_with_zero_carre(self):
		pl = Player(name = 'Niki', hand = ['8s','9c','10d','Jh','Qs','Kh','Ac','Ad'])
		copy_hand = ['8s','9c','10d','Jh','Qs','Kh','Ac','Ad']

		res = pl.check_if_hand_contains_carres(copy_hand)
		exp = ['8s','9c','10d','Jh','Qs','Kh','Ac','Ad']

		self.assertEqual(res,exp)
		self.assertEqual(pl.points,0)
		self.assertEqual(pl.carres,[])






if __name__ == '__main__':
	unittest.main()