import speech_recognition as sr
from functools import partial
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

def record_audio(time:int = 10):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        messagebox.showinfo("Recording", "Please start speaking...")
        try:
            audio_text = r.listen(source,timeout=time)
            transcribed = r.recognize_google(audio_text)
            messagebox.showinfo("Result", f"Did you say: {transcribed}")
        except sr.UnknownValueError:
            messagebox.showwarning("Recognition Failed", "Sorry, I did not understand that.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

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

