from deep_translator import MyMemoryTranslator

def translate_to_french(text):
    translator = MyMemoryTranslator(source='en-US', target='fr-FR')
    translation = translator.translate(text)
    return translation

def translate_to_english(text):
    translator = MyMemoryTranslator(source='fr-FR', target='en-US')
    translation = translator.translate(text)
    return translation

# Example usage:
english_text = "Hello, what's your name?"
translated_to_french = translate_to_french(english_text)
print("English to French:", translated_to_french)

french_text = "Bonjour, quel est votre nom?"
translated_to_english = translate_to_english(french_text)
print("French to English:", translated_to_english)
