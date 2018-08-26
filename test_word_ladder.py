import unittest
import word_ladder
import re

class TestSame(unittest.TestCase):

    def test_zip_iter(self):
        testlist = [(c,t) for (c,t) in zip('gold', 'goad')]
        self.assertEqual([('g','g'),('o','o'),('l','a'),('d','d')], testlist)
    def test_same(self):
        same = word_ladder.same('gold','goad')
        self.assertEqual(3,same)
        same = word_ladder.same('tree', 'been')
        self.assertNotEqual(2,same)

class TestFind(unittest.TestCase):
    def test_pattern_builder(self):
        testlist = []
        word = 'gold'
        for i in range(len(word)):
            testlist += [word[:i] + "." + word[i + 1:]]
        self.assertEqual(testlist,['.old','g.ld','go.d','gol.'])


class TestBuild(unittest.TestCase):
    def test_search_pattern(self):
        self.assertNotEqual(True, re.search('.old','gold'))
        self.assertEqual(None, re.search('.olg','gold'))

class TestMain(unittest.TestCase):
    def test_nofilefound(self):
        self.assertRaises(FileNotFoundError, open('test.txt'))
    def test_process_dictionary(self):
        file = open('dictionary.txt')
        start='gold'
        lines = file.readlines()
        for line in lines:
            word = line.rstrip()
        self.assertEqual(len(word),len(start))
    def wrong_filetype(self):
        fname = input("Enter dictionary name: ")#dictionary file name
        while fname[-4:] != '.txt':
            fname = input("Dictionary must be .txt file : ")
        





if __name__ == "__main__":
    unittest.main()
