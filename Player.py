import sys

class Player:

	def __init__(self,name,hand):
		self.name = name
		self.hand = hand
		self.belots = []
		self.carres = []
		self.quintes = []
		self.quartets = []
		self.trieces = []
		self.points = 0



	# def set_hand(self):
	# 	self.set_declarations()

	# def set_declarations(self):
	# 	self.check_if_hand_contains_belots(self.hand)


	def check_if_hand_contains_belots(self):
		
		belots = [['Qs','Ks'],['Qh','Kh'],['Qd','Kd'],['Qc','Kc']]

		for belot in belots:
			if set(belot).issubset(set(self.hand)):
				self.belots.append(belot)
				self.points += 20


	def check_if_hand_contains_higher_declarations(self):
		copy_hand = self.hand


	def check_if_hand_contains_carres(self,copy_hand):
		
		carres = [['10s','10c','10d','10h'],['Qs','Qc','Qd','Qh'],['Ks','Kc','Kd','Kh'],['As','Ac','Ad','Ah'],['9s','9c','9d','9h'],['Js','Jc','Jd','Jh']]
		state_for_carre_points = 0  #resolves how much points to give according to "carres" list above
		for carre in carres:
			if set(carre).issubset(set(copy_hand)):
				self.carres.append(carre)
				copy_hand = [x for x in copy_hand if x not in carre]  #removes the combination form the copy_hand
				if state_for_carre_points <= 3:
					self.points += 100
				if state_for_carre_points == 4:
					self.points += 150
				if state_for_carre_points == 5:
					self.points += 200
			state_for_carre_points += 1
		return copy_hand









def main():
	pass




if __name__ == '__main__':
	main()