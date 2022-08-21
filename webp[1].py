import json
from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route("/")

def hello_world():
    return "Hello world"

@app.route("/time")

def  istime():
    return datetime.now().strftime("%H:%M:%S")

if __name__ == "__main__":
    app.run(debug=True)
