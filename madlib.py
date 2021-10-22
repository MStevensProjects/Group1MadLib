from flask import Flask, render_template, request, redirect,url_for
import mysql.connector
import boto3
import json

# Get creds from AWS Secrets Manager
client = boto3.client("secretsmanager")
response = client.get_secret_value(
    SecretId = 'madlibsDB'
)
# Get relevant information to the associated database
rdsClient = boto3.client('rds')
rdsResponse = rdsClient.describe_db_instances(
    DBInstanceIdentifier = 'madlibsdb'
)
# Set environment variables
rds_instance = rdsResponse.get('DBInstances')[0]['Endpoint']['Address']
db_name = rdsResponse.get('DBInstances')[0]['DBName']
database_secret = json.loads(response['SecretString'])
db_uname = database_secret['username']
db_cred = database_secret['password']

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():   
    if request.method == "POST":
        return redirect(url_for("results"))
    elif request.method == "GET":
        
        conn = mysql.connector.connect( user = db_uname, 
                                password = db_cred, 
                                host = rds_instance, 
                                database = db_name )
        cursor = conn.cursor()
        query = ("SELECT word_noun FROM Nouns ORDER BY RAND() LIMIT 1")
        cursor.execute(query)
        for i in cursor:
            noun1 = i
            print(noun1[0])
        # Close the cursor used to query the database
        cursor.close()
        # Close the connection to the database
        conn.close()
        return render_template("index.html")
    else: 
        return render_template("index.html")

@app.route("/results", methods=["GET","POST"])
# Returns the user input to the results form for the madlib to be read by the user.
def toResults():
    return render_template("results.html",
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
                            noun2 = request.form["noun2"])
if __name__ == "__main__":
    app.debug = True
    app.run()