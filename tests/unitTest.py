import unittest
import os
from ../src.loader import SlackDataLoader

class TestSlackDataLoader(unittest.TestCase):

    def setUp(self):
        # Path to the test Slack exported data folder
        test_data_path = 'path/to/TestSlackExportedData'
        self.loader = SlackDataLoader(test_data_path)

    def test_get_channels(self):
        # Test if channels are loaded correctly
        channels = self.loader.get_channels()
        self.assertIsNotNone(channels)
        self.assertIsInstance(channels, list)
        self.assertGreater(len(channels), 0)

    def test_get_users(self):
        # Test if users are loaded correctly
        users = self.loader.get_users()
        self.assertIsNotNone(users)
        self.assertIsInstance(users, list)
        self.assertGreater(len(users), 0)

    # Add more tests as needed for other methods in SlackDataLoader


if __name__ == '__main__':
    unittest.main()
