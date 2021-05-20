import unittest
import wordcount

class testCaseTrue(unittest.TestCase): 
    def test_true(self):
        self.assertEqual (wordcount.wordCount("The Quick Brown Fox Jumped Over the Lazy Dog"), 9)
    
    def test_true2(self):
        self.assertEqual (wordcount.wordCount("Hello World"), 2)
    
    def test_true3(self):
        self.assertEqual (wordcount.wordCount(""), 0)

class testCaseFalse(unittest.TestCase):
    def test_false(self):
        self.assertEqual (wordcount.wordCount("The Quick Brown Fox Jumped Over the Lazy Dog"), 4)

    def test_false2(self):
        self.assertEqual (wordcount.wordCount("Hello World"), 9)

    def test_false3(self):
        self.assertEqual (wordcount.wordCount(""), 1)


if __name__ == "__main__":
    unittest.main()
