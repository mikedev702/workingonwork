#bullshitapi.py

import json
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return json.dumps({'quote':'get it bitch'})

app.run()
