from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello  <img src='Screenshot 2021-05-17 at 5.24.02 PM.png" alt="Trulli'>"
