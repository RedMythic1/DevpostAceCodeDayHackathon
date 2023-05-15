import openai
import flask
import json
import string
import random

import hashlib

api1 = "sk-"
api2 ="tsozY7yFhMibo1"
api3 = "vlfYodT3BlbkFJkMz"
api4 = "fctEUhj7dH4ryjYVX"

all_chars = string.ascii_letters + string.digits + string.punctuation

openai.api_key = api1+api2+api3+api4

def get_adj(rating) -> str:
    if rating >= 35:
        return 'hard'
    return 'easy'

def quickhash(string: str) -> str:
    a = hashlib.new('sha512')
    a.update(string.encode())
    return a.hexdigest()

import flask_socketio

from db import Database

import logging

matches = {}
users = Database('users/')

app = flask.Flask(__name__, template_folder='./templates', static_folder='./static')
app.config['SECRET_KEY'] = 'qwegxuqwgebn8uyiqwgaHEIUSQWEBGSARDN7Y3WQUSHNG4BIEODYCNCHWEIDASTYRUDIJHnmG&YUSgb76yUFV^TYU&wsipjedwqoimhjmnuitg77YUbgNUYgbnygNUgINUgBNYuigbbnuiybBGNyGHN(I*UNhB*BGHUIGVUNHNIUGBYTUIBIIIUbhjgbiuBHIU)'
sio = flask_socketio.SocketIO(app)

logging.getLogger('werkzeug').setLevel(1000)

@app.before_request
def bfro():
    print(flask.session, 'd', flask.request.method, flask.request.path)
    pass

@app.route('/')
def index():
    print(flask.session)
    return flask.render_template('index.html')

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    print(flask.session)
    if flask.request.method == 'GET':
        return flask.render_template('signup.html')
    
    if flask.request.form['username'] in users.keys():
        flask.flash('User already exists!')
        return flask.redirect('/signup')

    users[flask.request.form['username']] = {
        'password': quickhash(flask.request.form['password']),
        'rating': 0,
        'pfp': 'http://placekitten.com/g/80/80',
        'status': 'lobby',
        'username': flask.request.form['username']
    }
    flask.session['user'] = flask.request.form['username']
    return "signed up"
    #return flask.redirect('/')

def generate_question(topic, rating):
    ques = openai.Completion.create(
         model='text-davinci-003',
         prompt='make a ' + get_adj(rating) + 'question about ' + topic,
         max_tokens=200,
         temperature=1
     )
    ques = ques['choices'][0]['text'].replace('\n', '') #type: ignore
    return ques

@sio.on('connect')
def connect(*_):
    users[flask.session['user']]['socket'] = flask.request.sid #type: ignore
    users[flask.session['user']]['status'] = 'lobby' if users[flask.session['user']]['status'] == 'unavailable' else users[flask.session["user"]]['status']

@sio.on('find_match')
def find_match(data):
    print(data)
    cat = data['category']
    stat = "waiting-" + cat
    for name, user in zip(users.keys(), users.values()):
        if user['rating'] in range(users[flask.session['user']]['rating'] - 10, users[flask.session['user']]['rating'] + 10) and user['status'] == stat and name != flask.session['user']: #type: ignore
            q = ''.join([random.choice(string.ascii_lowercase+string.ascii_uppercase) for _ in range(10)])
            matches[q] = {
                'category': cat,
                'vs': f'{flask.session["user"]}|||||vs|||||{name}',
                'points': {
                    flask.session['user']: 0,
                    name: 0
                }
            }
            flask_socketio.emit('match_found', {
                'session': q
            }, to=[flask.request.sid, user['socket']]) #type: ignore
            return
    flask_socketio.emit('match_fail')

@sio.on('disconnect')
def disconnect():
    users[flask.session['user']]['status'] = 'unavailable'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'GET':
        print('someone wants to ologin in')
        return flask.render_template('login.html')
    if flask.request.form['username'] not in users.keys():
        print(flask.session)
        print('person no existo')
        return flask.redirect('/signup')

    if quickhash(flask.request.form['password']) == users[flask.request.form['username']]['password']:
        print('person existo weo sendo demo to-o ')
        flask.session['user'] = flask.request.form['username']
        return flask.redirect('/')
    else:
        flask.flash('Incorrect Password!')
        return flask.redirect('/login')


@app.route('/matchmaking')
def matchmaking():
    try:
        users[flask.session['user']]['status'] = 'waiting-' + flask.request.args['category']
    except KeyError as e:
        print(e)
        return flask.redirect('/login')
    return flask.render_template('matchmaking.html')

@app.route("/vs")
def vs():
    x = 0
    opp = matches[flask.request.args['match']]['vs'].split('|||||vs|||||')
    for x in opp:
        if flask.session['user'] != x:
            opp = x
    print(opp)
    ques = openai.Completion.create(
         model='text-davinci-003',
         prompt='make a ' + get_adj(users[flask.session["user"]]['rating']) + 'question about ' + matches[flask.request.args['match']]['category'],
         max_tokens=200,
         temperature=1
     )
    ques = ques['choices'][0]['text'].replace('\n', '') #type: ignore
    return flask.render_template('Vs.html', acc=users[flask.session['user']], opp=users[opp], fq=ques, category=matches[flask.request.args['match']]['category'])

@sio.on('answer')
def handle_message(data):
    print(data)

@sio.on('name')
def handle_message(data):
    print(data)

@sio.on('timeout')
def timeout(data):
    ans = data['answer']
    ques = data['question']
    c = openai.Completion.create(
        model='text-davinci-003',
        prompt=f'Give only a number between 1 and 10 specifying how good the answer, "{ans}" is to the question, "{ques}".',
        max_tokens=3,
        temperature=0
    )
    c = c['choices'][0]['text'].replace('\n', '') #type: ignore
    c = int(c)
    matches[data['match']]['points'][flask.session['user']] += c
    opp_u = matches[data['match']]['points'].keys()
    for k in opp_u:
        if k != flask.session['user']:
            opp_u = k
    matches[data['match']]['points'][flask.session['username']] += c
    resolved = {
        'me': matches[data['match']][flask.session['username']],
        'opp': matches[data['match']][opp_u]
    }
    flask_socketio.emit('update_match', {
        'points': resolved,
        'question': generate_question(matches[data['match']]['category'], users[flask.session["user"]]['rating'])
    })

if __name__ == '__main__':
    sio.run(app, debug=True, host='0.0.0.0')
