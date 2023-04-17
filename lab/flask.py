from flask import Flask

app = Flask(__name__)

@app.route('/')

def print_message():
    return 'this is a message you\'re reading'
