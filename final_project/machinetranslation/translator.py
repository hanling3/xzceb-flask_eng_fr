''' Translate text'''
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    ''' Translate English text to French'''
    french_text = MyMemoryTranslator(source='english', target='french').translate(english_text)
    return french_text

def french_to_english(french_text):
    ''' Translate French text to English'''
    english_text = MyMemoryTranslator(source='french', target='english').translate(french_text)
    return english_text
