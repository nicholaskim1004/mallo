from openai import OpenAI

#create sep file that'll store api key and add to gitignore
#which api_key will read from

with open("key.txt","r") as file:
    key = file.read()

client = OpenAI(
  api_key=key
)

while True:
    content = input("What level of fluency are you, and what do you want to talk about?: ")
    
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
        {"role": "system", "content": "You are a Korean teacher that'll have a conversation on given topic at a given speaking level. Please go one sentence at a time."},
        {"role": "user", "content": content}
    ]
    )

    print(completion.choices[0].message)
