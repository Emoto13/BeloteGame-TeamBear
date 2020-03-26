from Player import Player
from announcements import quintes, quartes, trieces, power_of_cards

class Team:

	def __init__(self, teamname = 'Team', player1 = None, player2 = None):
		self.teamname = teamname
		self.player1 = player1
		self.player2 = player2

	def get_best_declaration(self):
		p1_best_anou = self.player1.best_announcement()
		p2_best_anou = self.player2.best_announcement()
		if len(p1_best_anou) > len(p2_best_anou):
			return p1_best_anou
		elif len(p1_best_anou) == len(p2_best_anou):
			return Team.check_highest_card(p1_best_anou, p2_best_anou)
		else:
			return p2_best_anou

	@staticmethod
	def check_highest_card(p1_best_anou, p2_best_anou):
		p1_higest_card = power_of_cards[p1_best_anou[-1][:-1]]  #gets the power of the card and converts it to int so we can ><
		p2_higest_card = power_of_cards[p2_best_anou[-1][:-1]]  
		if p1_higest_card > p2_higest_card:
			return p1_best_anou
		else:
			return p2_best_anou

def main():
	player1 = Player(name = 'Gosho')
	player2 = Player(name = 'Pesho')
	player1.set_hand(['10s', '10c', 'Kh', 'Qh', '10d', '10h', 'Ah'])
	player2.set_hand(['10s', '10c', 'Kc', 'Qc', '10d', '10h', 'Jc'])
	tm = Team('Mechkite', player1, player2)
	tm.get_best_declaration()
	# print(tm.player2.best_announcement())

if __name__ == '__main__':
	main()