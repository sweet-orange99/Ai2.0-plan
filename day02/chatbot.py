import os

from dotenv import load_dotenv
from openai import APIConnectionError, APIStatusError, OpenAI

load_dotenv(override=True)

api_key = os.getenv("MINIMAX_API_KEY")
base_url = os.getenv("MINIMAX_BASE_URL")
model = os.getenv("MINIMAX_MODEL", "MiniMax-M2.7")

if not api_key:
    raise ValueError("未找到 MINIMAX_API_KEY，请检查 .env 文件")

print("Base URL:", base_url)
print("Key prefix:", api_key[:6])
print("Model:", model)

client = OpenAI(
    api_key=api_key,
    base_url=base_url,
)

try:
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "你是一名耐心、专业的 AI 学习助手。"},
            {"role": "user", "content": "请用三句话解释什么是大语言模型。"},
        ],
    )

    print("AI：")
    print(response.choices[0].message.content)

except APIConnectionError as error:
    print(f"网络连接失败：{error}")

except APIStatusError as error:
    print(f"API 调用失败，状态码：{error.status_code}")
    print("响应内容：", error.response.text)

except Exception as error:
    print(f"发生未知错误：{error}")