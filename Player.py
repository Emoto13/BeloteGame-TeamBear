from announcements import carres, quintes, quartes, trieces
from belots import belots_modes
import json
from utils import format_json


class Player:

    def __init__(self, name='Player', hand=None):  # accepts gamemode
        if hand is None:
            hand = []

        self.belots = []
        self.carres = []
        self.quintes = []
        self.quartes = []
        self.trieces = []
        self.points = 0

        self.name = name
        self.set_hand(hand)

    def set_hand(self, hand, contract='All Trumps'):
        self.hand = hand

        if contract != 'No Trumps':
            self.set_declarations(contract)

    def set_declarations(self, contract):
        self.check_if_hand_contains_belots(self.hand, contract)
        self.check_if_hand_contains_higher_announcements()

    def check_if_hand_contains_belots(self, hand, contract):
        belots = belots_modes[contract]
        for belot in belots:
            if set(belot).issubset(set(hand)):
                self.belots.append(belot)
                self.points += 20

    def check_if_hand_contains_higher_announcements(self):
        hand_set = set(self.hand)
        hand_set = self.check_if_hand_contains_carres(hand_set)
        hand_set = self.check_if_hand_contains_quintes(hand_set)
        hand_set = self.check_if_hand_contains_quartes(hand_set)
        self.check_if_hand_contains_trieces(hand_set)

    def check_if_hand_contains_carres(self, hand):
        state_for_carre_points = 0  # resolves how much points to give according to "carres" list above
        for carre in carres:
            carre_set = set(carre)
            if carre_set.issubset(hand):
                self.carres.append(carre)
                hand = hand - carre_set  # removes the combination form the copy_hand
                if state_for_carre_points <= 3:
                    self.points += 100
                if state_for_carre_points == 4:
                    self.points += 150
                if state_for_carre_points == 5:
                    self.points += 200
            state_for_carre_points += 1
        return hand

    def check_if_hand_contains_quintes(self, hand):
        for quinte in quintes:
            quinte_set = set(quinte)
            if quinte_set.issubset(hand):
                self.quintes.append(quinte)
                hand = hand - quinte_set
        return hand

    def check_if_hand_contains_quartes(self, hand):
        for quarte in quartes:
            quarte_set = set(quarte)
            if quarte_set.issubset(hand):
                self.quartes.append(quarte)
                hand = hand - quarte_set
        return hand

    def check_if_hand_contains_trieces(self, hand):
        for triece in trieces:
            triece_set = set(triece)
            if triece_set.issubset(hand):
                self.trieces.append(triece)
                hand = hand - triece_set
        return hand

    def best_announcement(self):
        if self.quintes: return self.quintes[0]
        if self.quartes: return self.quartes[0]
        if self.trieces: return self.trieces[0]
        return []

    def clear_announcements(self):
        self.quintes = []
        self.quartes = []
        self.trieces = []

    def get_announcements(self):
        announcements = []
        if self.belots: announcements.extend(['belot'] * len(self.belots))
        if self.carres: announcements.extend(['carre'] * len(self.carres))
        if self.quintes: announcements.extend(['quinte'] * len(self.quintes))
        if self.quartes: announcements.extend(['quarte'] * len(self.quartes))
        if self.trieces: announcements.extend(['triece'] * len(self.trieces))
        return announcements

    def set_points(self):
        if self.quintes: self.points += len(self.quintes) * 100
        if self.quartes: self.points += len(self.quartes) * 50
        if self.trieces: self.points += len(self.trieces) * 20
        return self.points

    def clear_scoring_for_round(self):
        self.belots = []
        self.carres = []
        self.quintes = []
        self.quartes = []
        self.trieces = []
        self.points = 0

    def to_dict(self):
        dicts = {
            "cards": self.hand,
            "announcements": self.get_announcements(),
            "points": self.points
        }

        return dicts


def main():
    player = Player(name='Ivan')
    player.set_hand(['10s', '10c', 'Kh', 'Qh', '10d', '10h', 'Ah'])
    print(player.get_announcements())


if __name__ == '__main__':
    main()
