from openai import OpenAI
from os import getenv
from config import access_openai_api as openrouter_api_key
# gets API Key from environment variable OPENAI_API_KEY

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=openrouter_api_key,
)

completion = client.chat.completions.create(
  extra_headers={
    #"HTTP-Referer": $YOUR_SITE_URL, # Optional, for including your app on openrouter.ai rankings.
    #"X-Title": $YOUR_APP_NAME, # Optional. Shows in rankings on openrouter.ai.
  },
  model="meta-llama/llama-3-8b-instruct:free",
  messages=[
    {
      "role": "user",
      "content": "Say something about today's weather.",
    },
  ],
)
print(completion.choices[0].message.content)