import unittest

import src.counter as counter


class TestCount(unittest.TestCase):
    def test_regular_count(self):
        """
        Test that it can count the appearances of a particular word without any inflection
        """
        word = "text"
        filenames = [".\\tests\\test_count.txt", ".\\tests\\test_count_2.txt"]

        self.assertEqual(counter.get_word_count(word, filenames), 14)

if __name__ == '__main__':
    unittest.main()
