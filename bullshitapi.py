#bullshitapi.py

import json
from flask import Flask
import random


app = Flask(__name__)

with open("tech_bull.json") as tech_bull:
    techWords =  json.load(tech_bull)


techVerbs = techWords["Verbs"]
techAdjectives = techWords["Adjectives"]
techNouns = techWords["Nouns"]

def getTechBull():
    verb = random.choice(techVerbs)
    adj = random.choice(techAdjectives)
    noun = random.choice(techNouns)
    combine = verb + " " + adj + " " + noun
    return combine



@app.route('/tech')
def index():
    techQuote = getTechBull()
    return json.dumps({'quote': techQuote})

@app.route('/tech/verb')
def techverb():
    verb = random.choice(techVerbs)
    return json.dumps({'verb': verb})

@app.route('/tech/adjective')
def techAdjective():
    Adjective = random.choice(techAdjectives)
    return json.dumps({'verb': Adjective})

@app.route('/tech/noun')
def techNoun():
    noun = random.choice(techNouns)
    return json.dumps({'noun': noun})

app.run()
