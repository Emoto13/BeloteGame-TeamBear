import unittest
from file_writers.write_to_txt_helpers import format_team_names, format_output_for_first_and_last_rounds, format_middle_round_output, \
 format_game_end_output, format_horizontal_separator, format_output_for_first_and_last_rounds_team1, \
 format_output_for_first_and_last_rounds_team2, format_output_team1, format_output_team2, \
 handle_winner_output




class TestWriteToTxtClass(unittest.TestCase):

    # player1 = Player(name='Marto')
    # player2 = Player(name='Rado')
    # team1 = Team(team_name='Mechetata', player1=player1, player2=player2)

    # player3 = Player(name='Gosho')
    # player4 = Player(name='Pesho')
    # team2 = Team(team_name='Kotetata', player1=player3, player2=player4)
    # w = WriteToTxt(team1,team2)

    # def test_if_constructor_creates_result_file_and_writes_teams_as_expected(self):
    #     self.w.file.close()
    #     with open('result.txt', 'r') as f:
    #         content = f.read()

    #     exp = '    Mechetata    |    Kotetata    \n==================================\n'

    #     self.assertEqual(content,exp)


    def test_if_format_team_names_works_as_expected(self):
        team_names = f'    Mechetata    |    Kotetata    \n'
        horizontal_separator_length = len(team_names) - 1
        exp = '    Mechetata    |    Kotetata    \n==================================\n'

        res = format_team_names(team_names,horizontal_separator_length)

        self.assertEqual(res,exp)

    def test_if_format_output_for_first_and_last_rounds_team1_works_as_expected(self):
        team_names = f'    Mechetata    |    Kotetata    \n'
        chars_before_vertical_separator = team_names.index("|")
        team1_current_points = 20

        exp = '20               |'

        res = format_output_for_first_and_last_rounds_team1(team1_current_points, chars_before_vertical_separator)

        self.assertEqual(res,exp)

    def test_if_format_output_for_first_and_last_rounds_team2_works_as_expected(self):
        team_names = f'    Mechetata    |    Kotetata    \n'
        chars_before_vertical_separator = team_names.index("|")
        chars_after_vertical_separator = len(team_names) - chars_before_vertical_separator - 1
        team2_current_points = 120

        exp = '120             \n'

        res = format_output_for_first_and_last_rounds_team2(team2_current_points, chars_after_vertical_separator)

        self.assertEqual(res,exp)

    def test_if_format_output_for_first_and_last_rounds_works_as_expected(self):
        team_names = f'    Mechetata    |    Kotetata    \n'
        chars_before_vertical_separator = team_names.index("|")
        chars_after_vertical_separator = len(team_names) - chars_before_vertical_separator - 1
        team1_points = 20 
        team2_points = 120
        exp = '20               |120             \n'

        res = format_output_for_first_and_last_rounds(team1_points, chars_before_vertical_separator, 
                                                    team2_points, chars_after_vertical_separator)

        self.assertEqual(res,exp)

    def test_if_format_output_team1_works_as_expected(self):
        team_names = f'    Mechetata    |    Kotetata    \n'
        chars_before_vertical_separator = team_names.index("|")
        team1_current_points = 20
        team1_new_points = 40

        exp ='20 + 40          |'

        res = format_output_team1(team1_current_points, team1_new_points, chars_before_vertical_separator)

        self.assertEqual(res,exp)

    def test_if_format_output_team2_works_as_expceted(self):
        team_names = f'    Mechetata    |    Kotetata    \n'
        chars_before_vertical_separator = team_names.index("|")
        chars_after_vertical_separator = len(team_names) - chars_before_vertical_separator - 1
        team2_current_points = 120
        team2_new_points = 150

        exp ='120 + 150       \n'

        res = format_output_team2(team2_current_points, team2_new_points, chars_after_vertical_separator)

        self.assertEqual(res,exp)

    def test_if_format_middle_round_output_works_as_expected(self):
        team_names = f'    Mechetata    |    Kotetata    \n'
        chars_before_vertical_separator = team_names.index("|")
        chars_after_vertical_separator = len(team_names) - chars_before_vertical_separator - 1
        team1_current_points = 20
        team1_new_points = 40 
        team2_current_points = 120
        team2_new_points = 150

        exp = '20 + 40          |120 + 150       \n'

        res = format_middle_round_output(team1_current_points, team1_new_points, chars_before_vertical_separator,
                               team2_current_points, team2_new_points, chars_after_vertical_separator)

        self.assertEqual(res,exp)

    def test_if_format_horizontal_separator_works_as_expected(self):
        team_names = f'    Mechetata    |    Kotetata    \n'
        horizontal_separator_length = len(team_names) - 1

        exp = '==================================\n'

        res = format_horizontal_separator(horizontal_separator_length)
        
        self.assertEqual(res,exp)

    def test_if_handle_winner_output_works_as_expected(self):
        team_names = f'    Mechetata    |    Kotetata    \n'
        chars_before_vertical_separator = team_names.index("|")
        chars_after_vertical_separator = len(team_names) - chars_before_vertical_separator - 1
        team1_wins = 2
        team2_wins = 1

        exp = '       (2)       |      (1)       \n'

        res = handle_winner_output(team1_wins, chars_before_vertical_separator, team2_wins, chars_after_vertical_separator)

        self.assertEqual(res,exp)

    def test_if_format_game_end_output_works_as_expected(self):
        team_names = f'    Mechetata    |    Kotetata    \n'
        horizontal_separator_length = len(team_names) - 1
        chars_before_vertical_separator = team_names.index("|")
        chars_after_vertical_separator = len(team_names) - chars_before_vertical_separator - 1
        team1_wins = 2
        team2_wins = 1

        exp = '==================================\n       (2)       |      (1)       \n==================================\n'

        res = format_game_end_output(team1_wins, chars_before_vertical_separator, 
                                    team2_wins, chars_after_vertical_separator, 
                                    horizontal_separator_length)
        self.assertEqual(res,exp)


if __name__ == '__main__':
    unittest.main()