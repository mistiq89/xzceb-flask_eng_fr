import unittest
from translator import english_to_french as ef
from translator import french_to_english as fe
class Check_it(unittest.TestCase):
    def test_eng_to_fre(self):
        print("Test string null for english to french")
        self.assertEqual(ef("Null")['translations'][0]['translation'],"Null")
        print("Test string for english to french: Hello")
        self.assertEqual(ef("Hello")['translations'][0]['translation'],"Bonjour")
    def test_fre_to_eng(self):
        print("Test string null for french to english")
        self.assertEqual(fe("Null")['translations'][0]['translation'],"Null")
        print("Test string for french to english: Bonjour")
        self.assertEqual(fe("Bonjour")['translations'][0]['translation'],"Hello")
if __name__=='__main__':
    unittest.main()
