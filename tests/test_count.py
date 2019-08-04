import unittest

from src.counter import regular_count
from src.counter import inflection_count

class TestCount(unittest.TestCase):
    def test_regular_count(self):
        """
        Test that it can count the appearances of a particular word without any inflection in the file test_count.txt.
        """
        word = "text"
        fileTmp = open(".\\tests\\test_count.txt", 'r')

        self.assertEqual(regular_count(word, fileTmp), 10)
    
    def test_inflection_count(self):
        """
        Test that it can count the appearances of a particular word without any inflection in the file test_count.txt.
        """
        word = "text"
        fileTmp = open(".\\tests\\test_count.txt", 'r')

        self.assertEqual(inflection_count(word, fileTmp), 14)

if __name__ == '__main__':
    unittest.main()