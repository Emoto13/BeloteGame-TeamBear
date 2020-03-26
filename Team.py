from Player import Player
from power_of_cards import power_of_cards
import json
from utils import format_json


class Team:

    def __init__(self, team_name='Team', player1=None, player2=None):
        self.team_name = team_name
        self.player1 = player1
        self.player2 = player2

    def get_best_declaration(self):
        player1_best_announcement = self.player1.best_announcement()
        player2_best_announcement = self.player2.best_announcement()

        if len(player1_best_announcement) == len(player2_best_announcement):
            return Team.check_highest_card(player1_best_announcement, player2_best_announcement)

        if len(player1_best_announcement) > len(player2_best_announcement):
            return player1_best_announcement
        return player2_best_announcement

    @staticmethod
    def check_highest_card(player1_best_announcement, player2_best_announcement):
        # gets the power of the card and converts it to int so we can >=<
        player1_highest_card = power_of_cards[player1_best_announcement[-1][:-1]]
        player2_highest_card = power_of_cards[player2_best_announcement[-1][:-1]]

        if player1_highest_card > player2_highest_card:
            return player1_best_announcement
        return player2_best_announcement

    def to_dict(self):
        dicts = {
            self.player1.name: self.player1.to_dict(),
            self.player2.name: self.player2.to_dict()
        }

        return dicts

    def to_json(self):
        dicts = {self.team_name: {
            self.player1.name: self.player1.to_dict(),
        },
            self.player2.name: self.player2.to_dict()
        }
        json_repr = json.dumps(dicts, indent=4)
        return format_json(json_repr)


def main():
    player1 = Player(name='Gosho')
    player2 = Player(name='Pesho')
    player1.set_hand(['10s', '10c', 'Kh', 'Qh', '10d', '10h', 'Ah'])
    player2.set_hand(['10s', '10c', 'Kc', 'Qc', '10d', '10h', 'Jc'])
    tm = Team('Mechkite', player1, player2)


if __name__ == '__main__':
    main()
