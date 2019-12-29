from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<p><center><h1>Hello World! <br /> run flask with docker</h1></p>"
