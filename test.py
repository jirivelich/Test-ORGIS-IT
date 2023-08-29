import unittest
from src.wikipedia import Wikipedia

class TestWikipedia(unittest.TestCase):

    def test_is_title(self):
        w = Wikipedia("cs","rum")
        self.assertTrue(w.is_title())
        w = Wikipedia("cs","rumbellion")
        self.assertFalse(w.is_title())

    def test_text(self):
        w = Wikipedia("cs","rum")
        self.assertIsNotNone(w.text())
        w = Wikipedia("cs","rumbellion")
        self.assertIsNone(w.text())

if __name__ == '__main__':
    unittest.main()