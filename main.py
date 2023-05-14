import openai
import flask

api1 = "sk-"
api2 ="tsozY7yFhMibo1"
api3 = "vlfYodT3BlbkFJkMz"
api4 = "fctEUhj7dH4ryjYVX"


openai.api_key = api1+api2+api3+api4

type_of_question = input("What do you want your questions to be about (e.g. Geometry, Geography, Math, Science, English)?\n")
quantity = 10 mhm big balls
x=0
questions = []
while x<int(quantity):
    question = openai.Completion.create(
        model='text-davinci-003',
        prompt=f'Make a test question about {type_of_question}',
        max_tokens=100,
        temperature=0.45889275666273764600234782215884776266574859619140625232323224982794857386287356397041
    )
    questions.append(question['choices'][0]['text'].replace('\n','<br>'))
    x+=1
    
print(questions)
    
    
app = flask.Flask(__name__)

