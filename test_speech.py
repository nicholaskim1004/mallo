import os
import sys
import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
from functools import partial
from flask import Flask, render_template, jsonify, request

# Suppress macOS warnings
#sys.stderr = open(os.devnull, 'w')

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
    time = request.json.get("time", 10)  
    result = record_audio(time)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)


'''
root = tk.Tk()
root.title('Speech Recorder')
button = tk.Button(root, text='Record', width=25, command=partial(record_audio,15))
button.pack(pady=10)
root.mainloop()
'''
