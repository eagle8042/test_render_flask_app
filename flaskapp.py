from flask import Flask
from fkask import render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.htm')
