import unittest
import unittest.mock
from main import TicTacGame


class TestEvens(unittest.TestCase):

    def test_check_winner(self):
        game = TicTacGame()
        for i in [1, -1]:
            game.board = [i, i, i, 0, 0, 0, 0, 0, 0]
            self.assertEqual(game.check_winner(), i)
            game.board = [0, 0, 0, i, i, i, 0, 0, 0]
            self.assertEqual(game.check_winner(), i)
            game.board = [0, 0, 0, 0, 0, 0, i, i, i]
            self.assertEqual(game.check_winner(), i)
            game.board = [i, 0, 0, i, 0, 0, i, 0, 0]
            self.assertEqual(game.check_winner(), i)
            game.board = [0, i, 0, 0, i, 0, 0, i, 0]
            self.assertEqual(game.check_winner(), i)
            game.board = [0, 0, i, 0, 0, i, 0, 0, i]
            self.assertEqual(game.check_winner(), i)
            game.board = [i, 0, 0, 0, i, 0, 0, 0, i]
            self.assertEqual(game.check_winner(), i)
            game.board = [0, 0, i, 0, i, 0, i, 0, 0]
            self.assertEqual(game.check_winner(), i)

    def test_validate_input(self):
        game = TicTacGame()
        game.board = [0 for i in range(9)]
        for i in ["a", 22, "ad", 7, 8, 4, 0, 9, 2, "asddadasdad"]:
            self.assertEqual(game.validate_input(i), type(i) == int and i > 0 and i <= 9)

    def test_test_game(self):
    	game = TicTacGame()
    	game.test_game()
