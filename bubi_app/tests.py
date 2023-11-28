import unittest
from unittest.mock import MagicMock
from .management.commands.run_telegram_bot import start, star_wars_characters, help_command, echo_all


class TestBot(unittest.TestCase):

    def test_start(self):
        message = MagicMock()
        message.chat.id = 891710861
        start(message)

    def test_help(self):
        message = MagicMock()
        message.chat.id = 891710861
        help_command(message)

    def test_SW(self):
        message = MagicMock()
        message.chat.id = 891710861
        star_wars_characters(message)

    def test_echo_all(self):
        message = MagicMock()
        message.chat.id = 891710861
        message.text = "Hello"
        echo_all(message)


if __name__ == '__main__':
    unittest.main()