from deep_translator import MyMemoryTranslator

def translate_to_french(text):
    translator = MyMemoryTranslator(source='en-US', target='fr-FR')
    translation = translator.translate(text)
    return translation

def translate_to_english(text):
    translator = MyMemoryTranslator(source='fr-FR', target='en-US')
    translation = translator.translate(text)
    return translation
