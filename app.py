from flask import Flask, request

app = Flask(__name__)

users = {
    "admin": "admin123"
}

@app.route('/')
def home():
    return '''
    <form method="POST" action="/login">
        Username: <input name="username"><br>
        Password: <input name="password"><br>
        <input type="submit">
    </form>
    '''

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        return "Login Successful"
    else:
        return "Invalid Credentials"

if __name__ == '__main__':
    app.run(debug=True)