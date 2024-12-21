import speech_recognition as sr
from functools import partial
from flask import Flask, render_template, jsonify, request


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('web-button.html')  

@app.route('/record', methods=['POST'])
def record():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            audio_text = r.listen(source, timeout=10)
            transcription = r.recognize_google(audio_text)
            return jsonify(success=True, transcription=transcription)
    except sr.UnknownValueError:
            return jsonify(success=False, error="Sorry, I couldn't understand the audio.")
    except Exception as e:
            return jsonify(success=False, error=str(e))

if __name__ == "__main__":
    app.run(debug=True)


