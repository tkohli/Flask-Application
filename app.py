from flask import Flask,request
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

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)