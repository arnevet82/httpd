from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello Natalie! you look sexy today!!</h1>"
