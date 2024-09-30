import json
from utils import *

from flask import Flask, Response
from flask import render_template
from flask import request


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    date = convert_date(request.form['date'])
    periods = int(request.form['periods'])
    amount = int(request.form['amount'])
    rate = float(request.form['rate'])
    status = validate_data(periods, amount, rate)
    if status == "ok":
        data = calculate(date, periods, amount, rate)
        response = Response(response=json.dumps(data), status=200, mimetype='application/json')
        return response
    else:
        data = {"error": status}
        response = Response(response=json.dumps(data), status=400, mimetype='application/json')
        return response


if __name__ == 'main':
    app.run(debug=True)
