from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<center>Hello World! <br /> run flask with docker"