from openai import OpenAI

#create sep file that'll store api key and add to gitignore
#which api_key will read from

with open("key.txt","r") as file:
    key = file.read()

client = OpenAI(
  api_key=key
)

def chat_w_gpt(prompt):
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        store = True,
        messages = [{"role": "system", "content": "You are a Korean teacher that'll have a conversation on given topic at a given speaking level. Please go one sentence at a time."} ,
                    {"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content.strip()



if __name__ == "__main__":
    while True:
        user_input = input("User: ")
        if user_input.lower() in ["quit","exit","bye"]:
            break
        
        print("Enter level of fluency and what type of conversation you'd like to have")
        response = chat_w_gpt(user_input)
        print(f"GPT: {response}")
        