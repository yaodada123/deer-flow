from openai import OpenAI

client = OpenAI(
    api_key="sk-api-YwF9T6SUdZ8iLvsfZu_7UBfGYSSAAW0LNxtHTVd82XNobhwROi2_L8mbxsJvYHwgeS7N8vE5cl9qAZ5lpFubHk3bcolwmBDVN2UjffoQ9or1Qoa0jpCMkvw",
    base_url="https://api.minimaxi.com/v1"
)

response = client.chat.completions.create(
    model="MiniMax-M2.1",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "你好"},
    ],
    extra_body={"reasoning_split": True},
)

print(response.choices[0].message.content)