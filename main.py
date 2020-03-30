import sys
from Player import Player
from Team import Team
from utils import is_match_won
from Game import Game
from WriteToTxt import WriteToTxt
from WriteToJSON import WriteToJSON


def input_data():
    # team1 = input('Team 1 name: ')
    # team2 = input('Team 2 name: ')
    team1 = 'Mechkite'
    team2 = 'Kotkite'
    teams = [team1, team2]

    # players_team1 = input(f'"{team1}" players: ')
    # players_team2 = input(f'"{team2}" players: ')
    # players_team1 = players_team1.split(',')
    # players_team2 = players_team2.split(',')
    players_team1 = ['Marto', 'Rado']
    players_team2 = ['Gosho', 'Pesho']
    players = players_team1 + players_team2

    data = [teams, players]

    return data


def main():
    game_id = 1

    teams, players = input_data()

    player1 = Player(players[0])
    player2 = Player(players[1])
    team1 = Team(teams[0], player1, player2)

    player3 = Player(players[2])
    player4 = Player(players[3])
    team2 = Team(teams[1], player3, player4)

    write_to_txt = WriteToTxt(team1, team2)
    write_to_json = WriteToJSON()

    while not is_match_won(team1.games_won, team2.games_won):
        g = Game(game_id=game_id, team1=team1, team2=team2, write_to_txt=write_to_txt, write_to_json=write_to_json)
        g.play_game()
        game_id += 1


if __name__ == '__main__':
    main()
