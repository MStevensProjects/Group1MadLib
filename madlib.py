from flask import Flask, render_template, request, redirect,url_for

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():   
    if request.method == "POST":
        adjective1 = request.form["adj1"]
        adjective2 = request.form["adj2"]
        bird = request.form["bird"]
        pastverb = request.form["pastverb"]
        room = request.form["roominhouse"]
        pastverb = request.form["pastverb"]
        verb1 = request.form["verb"]
        relName = request.form["relName"]
        noun1 = request.form["noun"]
        liquid = request.form["liquid"]
        bodypart = request.form["body"]
        plnoun = request.form["plnoun"]
        verbing = request.form["verbing"]
        noun2 = request.form["noun2"]
        print(adjective1, adjective2, bird, pastverb, room, verb1, relName, noun1, liquid, bodypart, plnoun, verbing, noun2)
        return redirect(url_for("results"))

    else: 
        return render_template('index.html')
@app.route("/results", methods=["GET","POST"])
def toResults():
    return render_template('results.html')
