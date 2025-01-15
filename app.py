from flask import Flask, jsonify
from Parsing import *
app = Flask(__name__)

@app.route('/')
def hello_world():
    return get_crypto()
@app.route('/<string:currency>')
def main(currency):
    return get_crypto(currency)


if __name__ == '__main__':
    app.run()
