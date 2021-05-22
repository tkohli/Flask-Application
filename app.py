from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Index'

@app.route('/hello')
def hello():
    return 'Hello, World'



@app.route('/hello/<name>')
def hello2(name=None):
    return render_template('hello.html', name=name)