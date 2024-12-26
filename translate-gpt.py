from openai import OpenAI
import pyaudio
import whisper
import numpy as np
import speech_recognition as sr

with open("key.txt","r") as file:
    key = file.read().strip()

client = OpenAI(
    api_key=key
)

def chat_w_gpt(prompt):
    try:
        response = client.chat.completions.create(
            model = "gpt-4o-mini",
            store = True,
            messages = [{"role": "system", "content": "You are a Korean teacher that'll have a conversation on given topic at a given speaking level. Please go one sentence at a time."} ,
                        {"role": "user", "content": prompt}]
        )
    
        return(response.choices[0].message.content.strip())
    except Exception as e:
        return(f"There was an error: {e}")
    
def transc_mic():
    r = sr.Recognizer()
    mic = sr.Microphone()
    try: 
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            
            transcr = r.recognize_google(audio,language="ko-KR")
            print(f"{transcr}")
            return transcr
    except sr.UnknownValueError:
        print("Sorry I didn't understand the audio")
    except sr.RequestError as e:
        print(f"Error {e}")

first_run = True

if __name__ == "__main__":
    while True:
        if first_run:
             print("Enter level of fluency and what type of conversation you'd like to have")
             first_run = False
        user_trans = transc_mic()
        if user_trans:
            user_input = input(f"User: {user_trans}")
        if user_input.lower() in ["quit","exit","bye"]:
            break
        
        response = chat_w_gpt(user_input)
        print(f"GPT: {response}")
        