
from guess_the_number import guess_game
import guess_the_number
from random import randint
from unittest import mock
from unittest.mock import MagicMock


def input_mock(s: str):
    """helper function to replace the built-in function input()"""
    r = randint(1, 100)
    print("guessing", r)
    return str(r)

def test_guess():
    guess_the_number.input = input_mock  # BAD
    with mock.patch("guess_the_number.randint", MagicMock(return_value=42):  # GOOD
        guess_game()
