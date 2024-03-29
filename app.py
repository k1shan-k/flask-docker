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
    port = int(os.environ.get('PORT',5000))
    app.run(host="0.0.0.0",port=port,debug=True)
