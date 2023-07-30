from deep_translator import MyMemoryTranslator

def translate_to_french(text):
    """
    Translate the given text from English to French.

    Parameters:
        text (str): The text to be translated.

    Returns:
        str: The translated text in French.
    """
    translator = MyMemoryTranslator(source='en-US', target='fr-FR')
    translation = translator.translate(text)
    return translation

def translate_to_english(text):
    """
    Translate the given text from French to English.

    Parameters:
        text (str): The text to be translated.

    Returns:
        str: The translated text in English.
    """
    translator = MyMemoryTranslator(source='fr-FR', target='en-US')
    translation = translator.translate(text)
    return translation

if __name__ == "__main__":
    # Example usage:
    english_text = "Hello, what's your name?"
    translated_to_french = translate_to_french(english_text)
    print("English to French:", translated_to_french)

    french_text = "Bonjour, quel est votre nom?"
    translated_to_english = translate_to_english(french_text)
    print("French to English:", translated_to_english)
