from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'this is index page'

@app.route('/login')
def login():
    userName = request.args.get('username')
    password = request.args.get('password')
    return login_user(userName, password)

def login_user(userName, password):
    if userName == 'siddarth07' and password == '8@HBg68st':
        return 'user is valid'
    else :
        return 'user is not a valid user'

@app.route('/signup')
def signup():
    
app.run(debug = True)