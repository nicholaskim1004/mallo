import os
import sys
import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr

# Suppress macOS warnings
sys.stderr = open(os.devnull, 'w')

def record(start:bool):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        messagebox.showinfo("Recording", "Please start speaking...")
        try:
            audio_text = r.listen(source,stream=start)
            transcribed = r.recognize_google(audio_text)
            messagebox.showinfo("Result", f"Did you say: {transcribed}")
        except sr.UnknownValueError:
            messagebox.showwarning("Recognition Failed", "Sorry, I did not understand that.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

root = tk.Tk()
root.title('Speech Recorder')
button = tk.Button(root, text='Record', width=25, command=record(True))
button.pack(pady=10)
button = tk.Button(root, text='Stop',width=25,command=record(False))
button.pack(pady=10)
root.mainloop()
