from flask import Flask, jsonify
from Parsing import *
app = Flask(__name__)

@app.route('/')
def hello_world():
    with open('Prices', 'r') as f:
        return dict(f.read())
@app.route('/<string:currency>')
def get_exact(currency):
    return get_crypto()[currency]

if __name__ == '__main__':
    app.run()
