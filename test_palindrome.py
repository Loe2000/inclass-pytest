import unittest
import palindrome

class testCaseTrue(unittest.Testcase): 
    def test_true(self):
        self.assertEqual (palindrome.palindrome("racecar"), True)
    
    def test_true2(self):
        self.assertEqual (palindrome.palindrome(""), True)
    
    def test_true3(self):
        self.assertEqual (palindrome.palindrome("Words sdroW"), True)

class testCaseFalse(unittest.Testcase):
    def test_false(self):
        self.assertEqual (palindrome.palindrome("Hello World"), False)
    def test_false2(self):
        self.assertEqual (palindrome.palindrome(12345), False)
