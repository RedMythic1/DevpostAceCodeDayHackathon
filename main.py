import openai

api1 = "sk-"
api2 ="tsozY7yFhMibo1"
api3 = "vlfYodT3BlbkFJkMz"
api4 = "fctEUhj7dH4ryjYVX"

openai.api_key = api1+api2+api3+api4

print(openai.Completion.create(
  model="ft-g6dcs8KWwliZ77Bq3zgOlfsB",
  prompt="is '10', the right answer to: '9+1'",
  max_tokens=7,
  temperature=0
))
