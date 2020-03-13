from flask import render_template
from app import app

import sys
sys.path.append('../')
from get_weather_data import knmi_data

@app.route('/')
@app.route('/index')
def index():
    data = knmi_data()
    return render_template("index.html", data=data)
