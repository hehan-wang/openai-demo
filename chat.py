import openai

# 设置 OpenAI API 密钥可以给大家免费提供一个调用api中转的key，支持3.5和4.0。额度不多测试是够了。
# openai.api_key = "sk-NYsoG3VBKDiTuvdtC969F95aFc4f45379aD3854a93602327"
# openai.api_base="https://key.wenwen-ai.com/v1"

# openai.api_base="https://proxy.hehanwang.com/v1"
# openai.api_key="sk-xxx"

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)
