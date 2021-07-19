from flask import *
app = Flask(__name__)
@app.route('/')
def log():
    return render_template('login.html')

@app.route('/login', methods =['POST'])
def login():
    uname = request.form['username']
    password = request.form['userpass']
    if uname == 'thando' and password == '1234':
        return 'Welcome %s' % uname + request.method
    else:
        return 'Error in logging in' + request.method

if __name__ == '__main__':

    app.run(debug=True)
