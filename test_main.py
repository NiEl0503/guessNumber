import unittest
from unittest.mock import patch
import main

class TestGetSecretNumber(unittest.TestCase):

    @patch('main.random.randint', return_value=42)
    def test_get_secret_number(self, mock_randint):
        secret_number = main.get_secret_number()
        self.assertEqual(secret_number, 42)

class TestPlayerGuess(unittest.TestCase):

    @patch('builtins.input', side_effect=['10'])
    def test_player_guess_valid_input(self, mock_input):
        guess = main.player_guess('Test')
        self.assertEqual(guess, 10)

    @patch('builtins.input', side_effect=['abc', '10'])
    def test_player_guess_invalid_input(self, mock_input):
        guess = main.player_guess('Test')
        self.assertEqual(guess, 10)

if __name__ == '__main__':
    unittest.main()
