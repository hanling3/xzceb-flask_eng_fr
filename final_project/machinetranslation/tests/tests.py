import unittest
from ./translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour', 'Translate "Hello" to French')
    
    def test_french_to_english(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello', 'Translate "Bonjour" to English')

if __name__ == '__main__':
    unittest.main()