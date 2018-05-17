from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello Natalie! You look great today! Have a wonderful weekend</h1>"
