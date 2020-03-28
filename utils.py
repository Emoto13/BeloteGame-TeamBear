import re
from power_of_cards import power_of_cards


def format_json(json):
    json = re.sub(r'": \[\s+', '": [', json)
    json = re.sub(r'",\s+', '", ', json)
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
    from Player import Player
    from Team import Team

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
    return power_of_cards[entity_best_announcement[-1][:-1]]


def game_end(team1_points, team2_points):
    if team1_points > 150 or team2_points > 150:
        if team1_points > team2_points:
            return team1_points
        elif team1_points == team2_points:
            return False
        elif team2_points > team1_points:
            return team2_points
    return False
