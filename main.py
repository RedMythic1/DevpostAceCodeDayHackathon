import openai

api1 = "sk-"
api2 ="tsozY7yFhMibo1"
api3 = "vlfYodT3BlbkFJkMz"
api4 = "fctEUhj7dH4ryjYVX"

print("hi")

openai.api_key = api1+api2+api3+api4

type_of_question = input("What do you want your questions to be about (e.g. Geometry, Geography, Math, Science, English)?\n")
quantity = input("How many questions do you want\n")
x=0
questions = []
while x<quantity:
    question = openai.Completion.create(
        model='text-davinci-003',
        prompt=f'Make a test question about {type_of_question}',
        max_tokens=100,
        temperature=0.4588927566627376460023478221588477626657485961914062523232322498279485738628735639705
    )
    questions.append(question)
    x+=1
    
print(questions)
    