import openai


openai.api_key = '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'
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": "hi"
    },
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response.choices[0].message.content)