import sys
from Player import Player
from Team import Team
from Round import Round
from Game import Game
from WriteToTxt import WriteToTxt


def input_data():
    # team1 = input('Team 1 name: ')
    # team2 = input('Team 2 name: ')
    team1 = 'Mechkite'
    team2 = 'Kotkite'
    teams = [team1,team2]

    # players_team1 = input(f'"{team1}" players: ')
    # players_team2 = input(f'"{team2}" players: ')
    # players_team1 = players_team1.split(',')
    # players_team2 = players_team2.split(',')
    players_team1 = ['Marto','Rado']
    players_team2 = ['Gosho','Pesho']
    players = players_team1 + players_team2
    
    data = [teams,players]

    return data

def check_for_match_end(team1_points, team2_points):
    if team1_points == 2 or team2_points == 2:
        return False
    return True

def main():
    game_id = 1

    teams, players = input_data()

    player1 = Player(players[0])
    player2 = Player(players[1])
    team1 = Team(teams[0], player1, player2)

    player3 = Player(players[2])
    player4 = Player(players[3])
    team2 = Team(teams[1], player3, player4)

    w = WriteToTxt(team1, team2)
 
    while check_for_match_end(team1.games_won, team2.games_won): 
        g = Game(game_id, team1, team2, w)
        g.play_game()
        game_id += 1


if __name__ == '__main__':
    main()