import unittest
from src.wikipedia import Wikipedia

class TestWikipedia(unittest.TestCase):

    def test_is_title(self):
        w = Wikipedia("456hjjhj")
        self.assertTrue(w.is_title())
        w = Wikipedia("hkkjgfh")
        self.assertFalse(w.is_title())

    def test_text(self):
        w = Wikipedia("Python")
        self.assertIsNotNone(w.text())
        w = Wikipedia("456hjjhj")
        self.assertIsNone(w.text())

if __name__ == '__main__':
    unittest.main()