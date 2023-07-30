import unittest
from translator_package.translator_package.translator import translate_to_french, translate_to_english

class TestTranslator(unittest.TestCase):
    def test_translate_to_french(self):
        # Test case
        english_text = "Hello, what's your name?"
        expected_translation = "Bonjour, quel est votre nom?"

        # Perform the translation
        actual_translation = translate_to_french(english_text)

        # Assertion
        self.assertEqual(actual_translation, expected_translation)

    def test_translate_to_english(self):
        # Test case
        french_text = "Bonjour, quel est votre nom?"
        expected_translation = "Hello, what's your name?"

        # Perform the translation
        actual_translation = translate_to_english(french_text)

        # Assertion
        self.assertEqual(actual_translation, expected_translation)

if __name__ == '__main__':
    unittest.main()
