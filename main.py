from flask import Flask
import json
import time
from random import randint


app = Flask(__name__)

@app.route('/')
def home():
    #\ time
    T = time.localtime()
    current_time = time.strftime("%Y-%m-%d %H:%M:%S",T)

    #\ random number
    Num2guess = 3
    guessvalue = [randint(0, 9) for i in range(Num2guess)]

    result = {
        "ID":"0651d23da32da1f32a1s2dfa",
        'Date': current_time,
        "Guess Number":  guessvalue,
        "Probability": 0
    }

    return json.dumps(result, indent=4), {'Content-Type': 'application/json'}


if __name__ == '__main__':
    app.run(debug=True)