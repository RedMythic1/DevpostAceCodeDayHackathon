import openai
import flask

api1 = "sk-"
api2 ="tsozY7yFhMibo1"
api3 = "vlfYodT3BlbkFJkMz"
api4 = "fctEUhj7dH4ryjYVX"


openai.api_key = api1+api2+api3+api4

type_of_question = input("What do you want your questions to be about (e.g. Geometry, Geography, Math, Science, English)?\n")
quantity = 10
x=0
questions = []

def answer(input, question):
	answer = openai.Completion.create(
        model='text-davinci-003',
        prompt=f'Is {input} the correct answer for the question {question}',
        max_tokens=100,
        temperature=0.45889275666273764600234782215884776266574859619140625232323224982794857386287356397041
    )
	return answer

while x<int(quantity):
    question = openai.Completion.create(
        model='text-davinci-003',
        prompt=f'Make a test question about {type_of_question}',
        max_tokens=100,
        temperature=0.45889275666273764600234782215884776266574859619140625232323224982794857386287356397041
    )
    questions.append(question['choices'][0]['text'].replace('\n',''))
    x+=1
    
x=0
input1 = input(f'{questions[x]}')
x+=1
input2 = input(f'{questions[x]}')
x+=1
input3 = input(f'{questions[x]}')
x+=1
input4 = input(f'{questions[x]}')
x+=1
input5 = input(f'{questions[x]}')
x+=1 
input6 = input(f'{questions[x]}')
x+=1
input7 = input(f'{questions[x]}')
x+=1
input8 = input(f'{questions[x]}')
x+=1
input9 = input(f'{questions[x]}')
x+=1
input10 = input(f'{questions[x]}')


    
    
app = flask.Flask(__name__, template_folder='.')

@app.route('/')
def index():
    return flask.render_template('index.html')


app.run('0.0.0.0', 80)
