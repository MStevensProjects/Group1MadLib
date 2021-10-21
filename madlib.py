from flask import Flask, render_template, request, redirect,url_for

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():   
    if request.method == "POST":
        return redirect(url_for("results"))

    else: 
        return render_template('index.html')

@app.route("/results", methods=["GET","POST"])
# Returns the user input to the results form for the madlib to be read by the user.
def toResults():
    return render_template('results.html',
                            adjective1 = request.form["adj1"], 
                            adjective2 = request.form["adj2"], 
                            bird = request.form["bird"], 
                            room = request.form["roominhouse"], 
                            pastverb = request.form["pastverb"], 
                            verb1 = request.form["verb"], 
                            relName = request.form["relName"], 
                            noun1 = request.form["noun"], 
                            liquid = request.form["liquid"], 
                            bodypart = request.form["body"], 
                            plnoun = request.form["plnoun"], 
                            verbing = request.form["verbing"], 
                            noun2 = request.form["noun2"]
                        )
if __name__ == "__main__":
    app.debug = True
    app.run()