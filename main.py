import openai
import flask
import json
import string
import random

api1 = "sk-"
api2 ="tsozY7yFhMibo1"
api3 = "vlfYodT3BlbkFJkMz"
api4 = "fctEUhj7dH4ryjYVX"

all_chars = string.ascii_letters + string.digits + string.punctuation

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
        temperature=0
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

from db import Database

users = Database('users/')

app = flask.Flask(__name__, template_folder='./templates', static_folder='./static')
app.config['SECRET_KEY'] = 'qwegxuqwgebn8uyiqwgaHEIUSQWEBGSARDN7Y3WQUSHNG4BIEODYCNCHWEIDASTYRUDIJHnmG&YUSgb76yUFV^TYU&wsipjedwqoimhjmnuitg77YUbgNUYgbnygNUgINUgBNYuigbbnuiybBGNyGHN(I*UNhB*BGHUIGVUNHNIUG   BYTUIBIIIUbhjgbiuBHIU)'
sio = flask_socketio.SocketIO(app)

@app.route('/')
def index():
    return flask.render_template('index.html')

@sio.on('my event')
def handle_my_custom_event(jsondict):
    print('received json: ' + str(jsondict))
    diction = json.loads(jsondict)
    user_name = ''.join(random.choices(all_chars, k=10))
    


@app.route('/play', methods=['GET', 'POST'])
def play():
    return flask.render_template('searching.html')

@app.route("/vs")
def vs():
     question = openai.Completion.create(
        model='text-davinci-003',
        prompt=f'Make a test question about {type_of_question}',
        max_tokens=100,
        temperature=.7
    )
     return fask.render_template('Vs.html', user=users[flask.session['user']], question=question)
#@sio.on("timeout")
#def timeout():
    


if __name__ == '__main__':
    sio.run(app)
