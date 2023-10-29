from test_data import sudoku_boards
from sudoku import *


def test_sudoku_validity():
    """ Function correctly checks if sudoku board is a valid one (29/10/2023) """

    for board_num, sudoku_board in enumerate(sudoku_boards):
        expected_validity = sudoku_board["is_valid"]
        board = sudoku_board["board"]
        result, error_message = validate_sudoku_board(board)
        try:
            assert result == expected_validity
        except AssertionError:
            if expected_validity:
                print(
                    f"Test failed. Error for test data board number {board_num + 1}: {str(error_message)}")
            else:
                print(
                    f"Test failed. Sudoku board number {board_num + 1} is valid but was expected to be invalid.")
            raise
