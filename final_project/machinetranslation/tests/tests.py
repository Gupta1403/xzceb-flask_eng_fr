import unittest

from translator import englishtofrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishtofrench(''),None)
        self.assertEqual(englishtofrench("hello"),"Bonjour")
        self.assertEqual(englishtofrench("welcome"),"Bienvenue")
        self.assertEqual(englishtofrench("love"),"Amour")

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish(''),None)
        self.assertEqual(frenchToEnglish("Bonjour"),"Hello")
        self.assertEqual(frenchToEnglish("Bienvenue"),"Welcome")
        self.assertEqual(frenchToEnglish("Amour"),"Love")

unittest.main()