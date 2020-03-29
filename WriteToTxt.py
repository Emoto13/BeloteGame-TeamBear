from write_to_txt_helpers import format_team_names, format_output_for_first_and_last_rounds, \
    format_middle_round_output, \
    format_game_end_output


class WriteToTxt:

    def __init__(self):
        self.chars_before_vertical_separator = 0
        self.chars_after_vertical_separator = 0
        self.current_points_team1 = 0
        self.current_points_team2 = 0
        self.horizontal_separator_length = 0
        self.file = open('result.txt', 'w')

    def set_properties(self, team_names):
        self.horizontal_separator_length = len(team_names) - 1
        self.chars_before_vertical_separator = team_names.index("|")
        self.chars_after_vertical_separator = len(team_names) - self.chars_before_vertical_separator - 1

    def setting_up_txt_teams(self, team1, team2):
        team_names = f'    {team1.team_name}    |    {team2.team_name}    \n'
        self.set_properties(team_names)
        self.file.write(format_team_names(team_names, self.horizontal_separator_length))

    def write_results(self, team1_points, team2_points, round_id):
        if round_id == 1:
            self.write_first_round_results(team1_points, team2_points)
        else:
            self.write_round_results(team1_points, team2_points)

    def write_first_round_results(self, team1_points, team2_points):
        output = format_output_for_first_and_last_rounds(
            team1_points, self.chars_before_vertical_separator,
            team2_points, self.chars_after_vertical_separator)

        self.file.write(output)

        self.set_teams_current_points(team1_points, team2_points)

    def write_round_results(self, team1_points, team2_points):
        new_points_team1 = abs(self.current_points_team1 - team1_points)
        new_points_team2 = abs(self.current_points_team2 - team2_points)

        output = format_middle_round_output(
            self.current_points_team1, new_points_team1, self.chars_before_vertical_separator,
            self.current_points_team2, new_points_team2, self.chars_after_vertical_separator)

        self.file.write(output)

        self.set_teams_current_points(team1_points, team2_points)

    def write_game_end_output(self, team1_points, team2_points):
        self.set_teams_current_points(team1_points, team2_points)

        self.file.write(
            format_output_for_first_and_last_rounds(self.current_points_team1, self.chars_before_vertical_separator,
                                                    self.current_points_team2, self.chars_after_vertical_separator))

        game_end_output = format_game_end_output(self.current_points_team1, self.chars_before_vertical_separator,
                                                 self.current_points_team2, self.chars_after_vertical_separator,
                                                 self.horizontal_separator_length)

        self.file.write(game_end_output)

    def set_teams_current_points(self, team1_points, team2_points):
        self.current_points_team1 = team1_points
        self.current_points_team2 = team2_points


def main():
    pass


if __name__ == '__main__':
    main()
