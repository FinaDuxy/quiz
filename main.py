from flask import Flask, render_template
from random import randint

app = Flask(__name__)

@app.route('/')
def main():
    number1 = randint(1, 6)
    number2 = randint(1, 6)
    return render_template('index.html', result1=number1, result2=number2)

@app.route('/stat')
def stat():
    return render_template('stat.html', numbers=range(10, 110, 10))

app.run(debug=True)
