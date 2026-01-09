from openai import OpenAI

client = OpenAI(
    api_key="sk-api-YwF9T6SUdZ8iLvsfZu_7UBfGYSSAAW0LNxtHTVd82XNobhwROi2_L8mbxsJvYHwgeS7N8vE5cl9qAZ5lpFubHk3bcolwmBDVN2UjffoQ9or1Qoa0jpCMkvw",
    base_url="https://api.minimaxi.com/v1"
)

# 测试 1：单个 system 消息
print("=== Test 1: Single system message ===")
try:
    response = client.chat.completions.create(
        model="MiniMax-M2.1",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "你好"},
        ],
    )
    print("✅ Success:", response.choices[0].message.content[:50])
except Exception as e:
    print("❌ Error:", str(e)[:200])

# 测试 2：多个 system 消息
print("\n=== Test 2: Multiple system messages ===")
try:
    response = client.chat.completions.create(
        model="MiniMax-M2.1",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "system", "content": "Additional instructions."},
            {"role": "user", "content": "你好"},
        ],
    )
    print("✅ Success:", response.choices[0].message.content[:50])
except Exception as e:
    print("❌ Error:", str(e)[:200])

# 测试 3：带 tools 参数
print("\n=== Test 3: With tools ===")
try:
    response = client.chat.completions.create(
        model="MiniMax-M2.1",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "你好"},
        ],
        tools=[
            {
                "type": "function",
                "function": {
                    "name": "test_tool",
                    "description": "Test tool",
                    "parameters": {
                        "type": "object",
                        "properties": {},
                    }
                }
            }
        ]
    )
    print("✅ Success:", response.choices[0].message.content[:50] if response.choices[0].message.content else "No content")
except Exception as e:
    print("❌ Error:", str(e)[:200])

# 测试 4：system 消息在 tools 之后
print("\n=== Test 4: System message with tools (appended) ===")
try:
    response = client.chat.completions.create(
        model="MiniMax-M2.1",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "system", "content": "Use tools when needed."},
            {"role": "user", "content": "你好"},
        ],
        tools=[
            {
                "type": "function",
                "function": {
                    "name": "test_tool",
                    "description": "Test tool",
                    "parameters": {
                        "type": "object",
                        "properties": {},
                    }
                }
            }
        ]
    )
    print("✅ Success:", response.choices[0].message.content[:50] if response.choices[0].message.content else "No content")
except Exception as e:
    print("❌ Error:", str(e)[:200])
