import openai
import flask

api1 = "sk-"
api2 ="tsozY7yFhMibo1"
api3 = "vlfYodT3BlbkFJkMz"
api4 = "fctEUhj7dH4ryjYVX"


openai.api_key = api1+api2+api3+api4

type_of_question = input("What do you want your questions to be about (e.g. Geography, Science, English, History)?\n")
quantity = 10
x=0
questions = []

def answer(input, question):
	answer = openai.Completion.create(
        model='text-davinci-003',
        prompt=f'Is {input} the correct answer for the question {question}',
        max_tokens=100,
        temperature=0.1
    )
	return answer

while x<int(quantity):
    question = openai.Completion.create(
        model='text-davinci-003',
        prompt=f'Make a test question about {type_of_question}',
        max_tokens=100,
        temperature=.7
    )
    questions.append(question['choices'][0]['text'].replace('\n',''))
    x+=1
    
x=0
input1 = input(f'{questions[x]}\n')
x+=1
input2 = input(f'{questions[x]}\n')
x+=1
input3 = input(f'{questions[x]}\n')
x+=1
input4 = input(f'{questions[x]}\n')
x+=1
input5 = input(f'{questions[x]}\n')
x+=1 
input6 = input(f'{questions[x]}\n')
x+=1
input7 = input(f'{questions[x]}\n')
x+=1
input8 = input(f'{questions[x]}\n')
x+=1
input9 = input(f'{questions[x]}\n')
x+=1
input10 = input(f'{questions[x]}\n')
x=0
answer1 = answer(input1, questions[x])
print(answer1['choices'][0]['text'].replace('\n',''))
x+=1
answer2 = answer(input2, questions[x])
print(answer2['choices'][0]['text'].replace('\n',''))
x+=1
answer3 = answer(input3, questions[x])
print(answer3['choices'][0]['text'].replace('\n',''))
x+=1
answer4 = answer(input4, questions[x])
print(answer4['choices'][0]['text'].replace('\n',''))
x+=1
answer5 = answer(input5, questions[x])
print(answer5['choices'][0]['text'].replace('\n',''))
x+=1
answer6 = answer(input6, questions[x])
print(answer6['choices'][0]['text'].replace('\n',''))
x+=1
answer7 = answer(input7, questions[x])
print(answer7['choices'][0]['text'].replace('\n',''))
x+=1
answer8 = answer(input8, questions[x])
print(answer8['choices'][0]['text'].replace('\n',''))
x+=1
answer9 = answer(input9, questions[x])
print(answer9['choices'][0]['text'].replace('\n',''))
x+=1
answer10 = answer(input10, questions[x])
print(answer10['choices'][0]['text'].replace('\n',''))

import flask_socketio    

app = flask.Flask(__name__, template_folder='/template')
sio = flask_socketio.SocketIO

@app.route('/')
def index():
    return flask.render_template('index.html')




app.run('0.0.0.0', 80)
