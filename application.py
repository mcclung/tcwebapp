from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<html><body><h1>Hello Scott McClung!</h1></body></html>\n"

@app.route("/hellorld")
def helloworld():
    return "Hellorld!\n"

