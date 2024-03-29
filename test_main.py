import unittest
from unittest.mock import patch
import main

class TestGetSecretNumber(unittest.TestCase):

    @patch('main.random.randint', return_value=42)
    def test_get_secret_number(self, mock_randint):
        secret_number = main.get_secret_number()
        self.assertEqual(secret_number, 42)

class TestGetPlayerName(unittest.TestCase):

    @patch('builtins.input', return_value='John')
    def test_get_player_name_valid_input(self, mock_input):
        player_name = main.get_player_name()
        self.assertEqual(player_name, 'John')

    @patch('builtins.input', side_effect=['', 'Jane'])
    def test_get_player_name_empty_input_then_valid_input(self, mock_input):
        player_name = main.get_player_name()
        self.assertEqual(player_name, '')

        player_name = main.get_player_name()
        self.assertEqual(player_name, 'Jane')

class TestPlayerGuess(unittest.TestCase):

    @patch('builtins.input', side_effect=['10'])
    def test_player_guess_valid_input(self, mock_input):
        guess = main.player_guess('Test')
        self.assertEqual(guess, 10)

    @patch('builtins.input', side_effect=['abc', '10'])
    def test_player_guess_invalid_input(self, mock_input):
        guess = main.player_guess('Test')
        self.assertEqual(guess, 10)

class TestEvaluateGuess(unittest.TestCase):

    def test_evaluate_guess_low(self):
        attempts = []
        result = main.evaluate_guess(10, 50, attempts)
        self.assertFalse(result)
        self.assertIn(10, attempts)
    
    def test_evaluate_guess_high(self):
        attempts = []
        result = main.evaluate_guess(80, 50, attempts)
        self.assertFalse(result)
        self.assertIn(80, attempts)

    def test_evaluate_guess_correct(self):
        attempts = []
        result = main.evaluate_guess(50, 50, attempts)
        self.assertTrue(result)
        self.assertIn(50, attempts)

class TestPlayerTurn(unittest.TestCase):

    @patch('main.player_guess', return_value=50)
    @patch('main.evaluate_guess', return_value=True)
    def test_player_turn(self, mock_evaluate_guess, mock_player_guess):
        attempts = []
        result = main.player_turn('Test', 50, attempts)
        self.assertTrue(result)
        mock_player_guess.assert_called_once_with('Test')
        mock_evaluate_guess.assert_called_once_with(50, 50, attempts)

class TestComputerTurnSmart(unittest.TestCase):

    @patch('main.computer_smart_guess', return_value=50)
    def test_computer_turn_smart(self, mock_computer_smart_guess):
        attempts = []
        secret_number = 50
        result = main.computer_turn_smart(secret_number, attempts)
        self.assertTrue(result)
        self.assertIn(50, attempts)
        mock_computer_smart_guess.assert_called_once_with(1, 100)

class TestComputerSmartGuess(unittest.TestCase):

    def test_computer_smart_guess(self):
        min_num = 1
        max_num = 100
        guess = main.computer_smart_guess(min_num, max_num)
        self.assertTrue(min_num <= guess <= max_num)

class TestGuessNumber(unittest.TestCase):

    @patch('builtins.input', side_effect=['Test', 'no'])
    @patch('main.get_secret_number', return_value=50)
    @patch('main.player_turn', return_value=True)
    @patch('main.computer_turn_smart', return_value=False)
    def test_guess_number(self, mock_computer_turn_smart, mock_player_turn, mock_get_secret_number, mock_input):
        main.guess_number()
        mock_get_secret_number.assert_called_once()
        mock_player_turn.assert_called_once_with('Test', 50, [])
        mock_computer_turn_smart.assert_not_called()

if __name__ == '__main__':
    unittest.main()
