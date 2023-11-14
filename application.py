import datetime
from flask import Flask

app = Flask(__name__)
now = datetime.datetime.now()
formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

@app.route("/")
def hello():
    return "<html><body><h1>Hello Scott McClung!</h1></body></html>\n"

@app.route("/hellorld")
def helloworld():
    return "Hellorld!\n"

@app.route("/test")
def test():
    return formatted_date

