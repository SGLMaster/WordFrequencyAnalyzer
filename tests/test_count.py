import unittest

from src.counter import regular_count
from src.counter import inflection_count
from src.counter import multiple_files_count

class TestCount(unittest.TestCase):
    def test_regular_count(self):
        """
        Test that it can count the appearances of a particular word without any inflection in the file test_count.txt.
        """
        word = "text"
        fileTmp = open(".\\tests\\test_count.txt", 'r')

        self.assertEqual(regular_count(word, fileTmp), 12)
    
    def test_inflection_count(self):
        """
        Test that it can count the appearances of a particular word without any inflection in the file test_count.txt.
        """
        word = "text"
        fileTmp = open(".\\tests\\test_count.txt", 'r')

        self.assertEqual(inflection_count(word, fileTmp), 18)

    def test_multiple_files_count(self):
        """
        Test that it can count the appearances of a particular word without any inflection in several files.
        """
        word = "text"
        file1 = open(".\\tests\\test_count.txt", 'r')
        file2 = open(".\\tests\\test_count_2.txt", 'r')

        files_list = [file1, file2]

        self.assertEqual(multiple_files_count(word, files_list), 14)

if __name__ == '__main__':
    unittest.main()