from openai import OpenAI

with open("key.txt","r") as file:
    key = file.read().strip()

client = OpenAI(
    api_key=key
)

def chat_w_gpt(prompt):
    try:
        response = client.chat.completions.create(
            model = "gpt-4",
            store = True,
            messages = [{"role": "system", "content": "You are a Korean teacher that'll have a conversation on given topic at a given speaking level. Please go one sentence at a time."} ,
                        {"role": "user", "content": prompt}]
        )
    
        return(response.choices[0].message.content.strip())
    except Exception as e:
        return(f"There was an error: {e}")



if __name__ == "__main__":
    while True:
        print("Enter level of fluency and what type of conversation you'd like to have")
        user_input = input("User: ")
        if user_input.lower() in ["quit","exit","bye"]:
            break
        
        response = chat_w_gpt(user_input)
        print(f"GPT: {response}")
        