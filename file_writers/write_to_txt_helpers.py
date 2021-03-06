def format_team_names(team_names, horizontal_separator_length):
    horizontal_separator = format_horizontal_separator(horizontal_separator_length)
    return f'{team_names}{horizontal_separator}'


def format_output_for_first_and_last_rounds(team1_points, chars_before, team2_points, chars_after):
    team1_output = format_output_for_first_and_last_rounds_team1(team1_points, chars_before)
    team2_output = format_output_for_first_and_last_rounds_team2(team2_points, chars_after)
    return f'{team1_output}{team2_output}'


def format_middle_round_output(team1_current_points, team1_new_points, chars_before,
                               team2_current_points, team2_new_points, chars_after):
    team1_output = format_output_team1(team1_current_points, team1_new_points, chars_before)
    team2_output = format_output_team2(team2_current_points, team2_new_points, chars_after)
    return f'{team1_output}{team2_output}'


def format_game_end_output(team1_wins, chars_before, team2_wins, chars_after, horizontal_separator_length):
    horizontal_separator = format_horizontal_separator(horizontal_separator_length)
    winner_output = format_winner_output(team1_wins, chars_before,team2_wins, chars_after)
    return f'{horizontal_separator}{winner_output}{horizontal_separator}'


def format_horizontal_separator(horizontal_separator_length):
    horizontal_separator = '=' * horizontal_separator_length
    return f'{horizontal_separator}\n'


def format_output_for_first_and_last_rounds_team1(points, chars):
    spaces = ' ' * (chars - len(str(points)))
    return f'{points}{spaces}|'


def format_output_for_first_and_last_rounds_team2(points, chars):
    spaces = ' ' * (chars - len(str(points)) - 1)
    return f'{points}{spaces}\n'


def format_output_team1(current_points, points, chars):
    result = f'{current_points} + {points}'
    spaces_len = chars - len(result)
    spaces = ' ' * spaces_len
    return f'{result}{spaces}|'


def format_output_team2(current_points, points, chars):
    result = f'{current_points} + {points}'
    spaces_len = chars - len(result) - 1
    spaces = ' ' * spaces_len
    return f'{result}{spaces}\n'


def format_winner_output(team1_wins, chars_before, team2_wins, chars_after):
    return handle_winner_output(team1_wins, chars_before, team2_wins, chars_after)


def handle_winner_output(team1_wins, chars_before, team2_wins, chars_after):
    output_team1 = f'({team1_wins})'.center(chars_before)
    output_team2 = f'({team2_wins})'.center(chars_after - 1)
    return f'{output_team1}|{output_team2}\n'



