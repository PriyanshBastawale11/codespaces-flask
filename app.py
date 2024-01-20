from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")

@app.route("/Hello")
def Hello():
    return "hello"

@app.route("/name")
def name():
    return "Priyansh"

@app.route("/age")
def age():
    return "19"

@app.route("/city")
def city():
    return "nagpur"



