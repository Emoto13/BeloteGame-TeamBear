from Player import Player
from Team import Team
from utils import is_match_won
from Game import Game
from WriteToTxt import WriteToTxt
from WriteToJSON import WriteToJSON


def read_teams_names():
    read_team1_name = input('Team 1 name: ')
    read_team2_name = input('Team 2 name: ')
    team1_name = read_team1_name
    team2_name = read_team2_name

    return team1_name, team2_name


def read_player_names(team1_name, team2_name):
    read_players_team1_names = input(f'"{team1_name}" players: (format -> name, name) ')
    read_players_team2_names = input(f'"{team2_name}" players: (format -> name, name) ')
    team1_players_names = read_players_team1_names.split(', ')
    team2_players_names = read_players_team2_names.split(', ')

    team1_player1_name = team1_players_names[0]
    team1_player2_name = team1_players_names[1]

    team2_player1_name = team2_players_names[0]
    team2_player2_name = team2_players_names[1]

    return team1_player1_name, team1_player2_name, team2_player1_name, team2_player2_name


def main():
    teams = read_teams_names()
    players = read_player_names(teams[0], teams[1])

    player1 = Player(players[0])
    player2 = Player(players[1])
    team1 = Team(teams[0], player1, player2)

    player3 = Player(players[2])
    player4 = Player(players[3])
    team2 = Team(teams[1], player3, player4)

    write_to_txt = WriteToTxt(team1, team2)
    write_to_json = WriteToJSON()

    game_id = 1
    while not is_match_won(team1.games_won, team2.games_won):
        g = Game(game_id=game_id, team1=team1, team2=team2)
        g.play_game(write_to_txt, write_to_json)
        game_id += 1


if __name__ == '__main__':
    main()
