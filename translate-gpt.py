from openai import OpenAI
import pyaudio
import whisper
import numpy as np

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

first_run = True

#loading whisper model
whisper_mod = whisper.load_model("base")

#initalizing parameters: 
#RATE (num of samples collected per sec), CHUNK (num of frames in buffer)
RATE = 16000
CHUNK = 1024

p = pyaudio.PyAudio

stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True, frames_per_buffer=CHUNK)

if __name__ == "__main__":
    while True:
        if first_run:
             print("Enter level of fluency and what type of conversation you'd like to have")
             first_run = False
        
        audio_data = stream.read(CHUNK, exception_on_overflow=False)
        
        #normalizing the audio file by 32768 as 16 bit can range from -32,767 to 32,767
        audio_np = np.frombuffer(audio_data, dtype=np.int16).astype(np.float32) / 32768.0
        
        res = whisper_mod.transcribe(audio_np, language="ko")
     
        user_input = input(f"User: {res['text']}")
        if user_input.lower() in ["quit","exit","bye"]:
            stream.stop_stream()
            stream.close()
            p.terminate()
            break
        
        response = chat_w_gpt(user_input)
        print(f"GPT: {response}")
        