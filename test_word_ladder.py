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

class TestFind(unittetst.TestCase):
    def test_pattern_builder:
        word = test
        for i in range(len(word)):
            testlist += word[:i] + "." + word[i + 1:]


class TestBuild(unittest.TestCase):
    def test_search_pattern(self):
        self.assertNotEqual(True, re.search('.old','gold'))
        self.assertEqual(None, re.search('.olg','gold'))
    def test_build_



if __name__ == "__main__":
    unittest.main()
