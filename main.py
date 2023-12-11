from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return '<h1>Gero Zayas Flask App</h1>'

@app.route("/about")
def about():
    return '<h1>About</h1>'
