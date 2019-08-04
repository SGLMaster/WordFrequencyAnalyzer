import unittest
import pronouncing
import syllables

import src.inflection as infl

class TestInflection(unittest.TestCase):
    def test_ing(self):
        """
        Test the functionality for inflecting the present participle which adds the suffix "-ing" to a word
        """
        # Regular verbs
        self.assertEqual(infl.inflect_ing("eat"), "eating")
        self.assertEqual(infl.inflect_ing("speak"), "speaking")
        self.assertEqual(infl.inflect_ing("cook"), "cooking")
        self.assertEqual(infl.inflect_ing("start"), "starting")
        self.assertEqual(infl.inflect_ing("do"), "doing")
        self.assertEqual(infl.inflect_ing("stay"), "staying")
        self.assertEqual(infl.inflect_ing("fix"), "fixing")
        self.assertEqual(infl.inflect_ing("try"), "trying")
        self.assertEqual(infl.inflect_ing("text"), "texting")

        # Verbs ending with -e (with the exception of verbs ending in -ee and -ie)
        self.assertEqual(infl.inflect_ing("hope"), "hoping")
        self.assertEqual(infl.inflect_ing("ride"), "riding")
        self.assertEqual(infl.inflect_ing("make"), "making")
        self.assertEqual(infl.inflect_ing("write"), "writing")

        # Verbs ending with -ee
        self.assertEqual(infl.inflect_ing("agree"), "agreeing")
        self.assertEqual(infl.inflect_ing("flee"), "fleeing")
        self.assertEqual(infl.inflect_ing("see"), "seeing")

        # Verbs ending with -ie
        self.assertEqual(infl.inflect_ing("die"), "dying")

        # Verbs ending with one vowel and one consonant (with the exception of w, x, and y)

        # For one syllable verbs
        self.assertEqual(infl.inflect_ing("jog"), "jogging")
        self.assertEqual(infl.inflect_ing("sit"), "sitting")
        self.assertEqual(infl.inflect_ing("run"), "running")
        self.assertEqual(infl.inflect_ing("stop"), "stopping")
        self.assertEqual(infl.inflect_ing("box"), "boxing")
        self.assertEqual(infl.inflect_ing("plow"), "plowing")
        self.assertEqual(infl.inflect_ing("pay"), "paying")

        # For two syllable verbs
        # Stressed in the first syllable
        self.assertEqual(infl.inflect_ing("answer"), "answering")
        self.assertEqual(infl.inflect_ing("offer"), "offering")
        self.assertEqual(infl.inflect_ing("listen"), "listening")
        self.assertEqual(infl.inflect_ing("visit"), "visiting")
        # Stressed in the second syllable
        self.assertEqual(infl.inflect_ing("admit"), "admitting")
        self.assertEqual(infl.inflect_ing("prefer"), "preferring")
        self.assertEqual(infl.inflect_ing("begin"), "beginning")

    def test_present(self):
        """
        Test the functionality for inflecting the present tense which adds the suffix "-s" or "-es" to a word
        """
        # Normal plural inflection
        self.assertEqual(infl.inflect_plural("text"), "texts")

        # Sibilant ending words
        self.assertEqual(infl.inflect_plural("bus"), "buses")
        self.assertEqual(infl.inflect_plural("miss"), "misses")
        self.assertEqual(infl.inflect_plural("wish"), "wishes")
        self.assertEqual(infl.inflect_plural("watch"), "watches")
        self.assertEqual(infl.inflect_plural("fox"), "foxes")

        # Word endings -y consonant
        self.assertEqual(infl.inflect_plural("party"), "parties")
        self.assertEqual(infl.inflect_plural("study"), "studies")
        self.assertEqual(infl.inflect_plural("cry"), "cries")

        # Word endings -y vowel
        self.assertEqual(infl.inflect_plural("buy"), "buys")
        self.assertEqual(infl.inflect_plural("play"), "plays")

    def test_past(self):
        """
        Test the functionality for inflecting the past tense which adds the suffix "-ed" to a word
        """
        # Words endings '-e'
        self.assertEqual(infl.inflect_past("provide"), "provided")

        # Word endings -y consonant
        self.assertEqual(infl.inflect_past("try"), "tried")

        # Word endings -y vowel
        self.assertEqual(infl.inflect_past("play"), "played")

        # Verbs ending with one vowel and one consonant (with the exception of w, x, and y)

        # For one syllable words
        self.assertEqual(infl.inflect_past("stop"), "stopped")
        self.assertEqual(infl.inflect_past("wait"), "waited")

        # For two syllable words
        # Stressed in the first syllable
        self.assertEqual(infl.inflect_past("visit"), "visited")

        # Stressed in the second syllable
        self.assertEqual(infl.inflect_past("prefer"), "preferred")

    def test_er(self):
        """
        Test the functionality for inflecting the tense which adds the suffix "-er" to a word
        """
        # Words endings '-e'
        self.assertEqual(infl.inflect_er("provide"), "provider")

        # Word endings -y consonant
        self.assertEqual(infl.inflect_er("happy"), "happier")

        # Word endings -y vowel
        self.assertEqual(infl.inflect_er("buy"), "buyer")

        # Verbs ending with one vowel and one consonant (with the exception of w, x, and y)

        # For one syllable words
        self.assertEqual(infl.inflect_er("fat"), "fatter")
        self.assertEqual(infl.inflect_er("wet"), "wetter")
        self.assertEqual(infl.inflect_er("wait"), "waiter")
        self.assertEqual(infl.inflect_er("eat"), "eater")

        # For two syllable words
        # Stressed in the first syllable
        
        # Stressed in the second syllable
        self.assertEqual(infl.inflect_er("prefer"), "preferrer")

if __name__ == '__main__':
    unittest.main()