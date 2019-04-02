from json import dumps
from flask import Flask, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return 'Home Page'


@app.route('/hello/')
def hello():
    return dumps({
        'code': 200,
        'status': 'OK',
        'response': 'Hello World!'
    })


@app.route('/info')
def info():
    print(request.environ)
    print(request.cookies)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
