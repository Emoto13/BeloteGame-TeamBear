import re
from constants.power_of_cards import POWER_OF_CARDS


def format_json(json):
    json = re.sub(r'": \[\s+', '": [', json)
    json = re.sub(r'"\s+\]', '"]', json)
    return json


def best_announcement(entity1, entity2):
    entity1_best_announcement = entity1.best_announcement()
    entity2_best_announcement = entity2.best_announcement()
    type_of_entity = type(entity1)

    if len(entity1_best_announcement) == len(entity2_best_announcement) != 0:
        return check_highest_card(entity1_best_announcement, entity2_best_announcement, type_of_entity)

    if len(entity1_best_announcement) > len(entity2_best_announcement):
        return entity1_best_announcement
    return entity2_best_announcement


def check_highest_card(entity1_best_announcement, entity2_best_announcement, type_of_entity):
    # gets the power of the card and converts it to int so we can >=<
    from entities.player import Player
    from entities.team import Team

    entity1_highest_card = highest_card(entity1_best_announcement)
    entity2_highest_card = highest_card(entity2_best_announcement)

    if entity1_highest_card > entity2_highest_card:
        return entity1_best_announcement
    elif entity1_highest_card < entity2_highest_card:
        return entity2_best_announcement

    if type_of_entity is Player:
        return entity1_best_announcement

    if type_of_entity is Team:
        return None


def highest_card(entity_best_announcement):
    return POWER_OF_CARDS[entity_best_announcement[-1][:-1]]


def is_game_won(team1, team2):
    team1_points = team1.team_points
    team2_points = team2.team_points

    if team1_points > 150 or team2_points > 150:
        if team1_points == team2_points:
            return False

        if team1_points > team2_points:
            team1.games_won += 1
            return True

        if team1_points < team2_points:
            team2.games_won += 1
            return True

    return False


def clear_team_points(team1, team2):
    team1.clear_points()
    team2.clear_points()


def is_match_won(team1_games_won, team2_games_won):
    if team1_games_won == 2 or team2_games_won == 2:
        return True
    return False
