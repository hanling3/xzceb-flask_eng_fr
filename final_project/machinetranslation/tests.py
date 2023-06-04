import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_english_to_french_1(self):
        self.assertEqual(english_to_french('Hi'), 'Bonjour')
    
    def test_english_to_french_2(self):
        self.assertNotEqual(english_to_french('Hello'), 'Hello')
    
    def test_french_to_english_3(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
    
    def test_french_to_english_4(self):
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour')

if __name__ == '__main__':
    unittest.main()