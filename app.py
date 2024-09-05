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

@app.post('/signup')
def signup():
    if request.method == 'GET':
        return 'please use POST method'
    data = request.get_json()
    return validata_signup(data)

def validata_signup(data):
    username = data['username']
    password = data['password']
    mobileno = data['mobileno']
    print(username.isalnum(), password.isalnum(), len(mobileno))
    if len(username) <3 or len(username) > 32 or not username.isalnum() or len(password)<8 or len(password) > 32 or not password.isalnum() or len(mobileno) != 10:
        return 'invalid user'
    else :
        return 'valid user & user successfully registered'


app.run(debug = True)