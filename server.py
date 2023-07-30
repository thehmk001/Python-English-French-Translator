from flask import Flask, request, jsonify
from translator_package.translator_package.translator import translate_to_french, translate_to_english
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/translate/to_french', methods=['POST'])
def translate_to_french_endpoint():
    data = request.get_json()
    english_text = data.get('text')
    if english_text is None:
        return jsonify({"error": "Text to translate is missing."}), 400

    translated_text = translate_to_french(english_text)
    return jsonify({"translation": translated_text})

@app.route('/translate/to_english', methods=['POST'])
def translate_to_english_endpoint():
    data = request.get_json()
    french_text = data.get('text')
    if french_text is None:
        return jsonify({"error": "Text to translate is missing."}), 400

    translated_text = translate_to_english(french_text)
    return jsonify({"translation": translated_text})

if __name__ == '__main__':
    app.run(debug=True)
