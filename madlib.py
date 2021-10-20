from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():   
    return render_template('index.html')
def toResults():
    return render_template('results.html')

