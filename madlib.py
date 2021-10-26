from flask import Flask, render_template, request, redirect,url_for
import mysql.connector
import boto3
import json
import random

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
# Set environment variables to be used for database connection.
rds_instance = rdsResponse.get('DBInstances')[0]['Endpoint']['Address']
db_name = rdsResponse.get('DBInstances')[0]['DBName']
database_secret = json.loads(response['SecretString'])
db_uname = database_secret['username']
db_cred = database_secret['password']

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():   
    qresults = []
    allResults = []
    if request.method == "POST":
        return redirect(url_for("results"))
    if request.method == "GET" and len(allResults) == 0:
        # When the user selects the AUTOFILL button on the form, the invoked GET method will connect to the database and execute the appropriate queries to fill the form.

        # Establish the database connection       
        conn = mysql.connector.connect( user = db_uname, 
                                        password = db_cred, 
                                        host = rds_instance, 
                                        database = db_name )
        # Establish database cursor to allow for querying
        cursor = conn.cursor()

        # Begin query execution
        cursor.execute('SELECT adj_word from Adjectives')
        for i in cursor:       
            result = i
            qresults += result
        random.shuffle(qresults)
        allResults.append(qresults[1])
        allResults.append(qresults[3])

        # Flushes out previous queries
        qresults = []
        # Begin query execution
        cursor.execute('SELECT bird_name from Birds')
        for i in cursor: 
            result = i
            qresults += result
        random.shuffle(qresults)
        allResults.append(qresults[1])

        # Flushes out previous queries
        qresults = []
        # Begin query execution
        cursor.execute('SELECT room_name from Rooms')
        for i in cursor: 
            result = i
            qresults += result
        random.shuffle(qresults)
        allResults.append(qresults[1])

        # Flushes out previous queries
        qresults = []
        # Begin query execution
        cursor.execute('SELECT verb_word from Verbs')
        for i in cursor: 
            result = i
            qresults += result
        random.shuffle(qresults)
        allResults.append(qresults[1])
        allResults.append(qresults[20])

        # Flushes out previous queries
        qresults = []
        # Begin query execution
        cursor.execute('SELECT fName_name from FirstNames')
        for i in cursor: 
            result = i
            qresults += result
        random.shuffle(qresults)
        allResults.append(qresults[1])

        # Flushes out previous queries
        qresults = []
        # Begin query execution
        cursor.execute('SELECT word_noun from Nouns')
        for i in cursor: 
            result = i
            qresults += result
        random.shuffle(qresults)
        allResults.append(qresults[1])

        # Flushes out previous queries
        qresults = []
        # Begin query execution
        cursor.execute('SELECT liquid_name from Liquids')
        for i in cursor: 
            result = i
            qresults += result
        random.shuffle(qresults)
        allResults.append(qresults[1])

        # Flushes out previous queries
        qresults = []
        # Begin query execution
        cursor.execute('SELECT bPart_name from BodyParts')
        for i in cursor: 
            result = i
            qresults += result
        random.shuffle(qresults)
        allResults.append(qresults[1])

        # Flushes out previous queries
        qresults = []
        # Begin query execution
        cursor.execute('SELECT word_noun from Nouns')
        for i in cursor: 
            result = i
            qresults += result
        random.shuffle(qresults)
        allResults.append(qresults[1])

        # Flushes out previous queries
        qresults = []
        # Begin query execution
        cursor.execute('SELECT verb_word from Verbs')
        for i in cursor: 
            result = i
            qresults += result
        random.shuffle(qresults)
        allResults.append(qresults[1])

        # Flushes out previous queries
        qresults = []
        # Begin query execution
        cursor.execute('SELECT word_noun from Nouns')
        for i in cursor: 
            result = i
            qresults += result
        
        # Randomize selections and assign to values
        random.shuffle(qresults)
        allResults.append(qresults[1])
        print("All of the results:")
        print(allResults)
        adjRes = allResults[0]
        adj2Res = allResults[1]
        birdRes = allResults[2]
        roomRes = allResults[3]
        pverbRes = allResults[4]
        verb1Res = allResults[5]
        nameRes = allResults[6]
        noun1Res = allResults[7]
        liqRes = allResults[8]
        bpRes = allResults[9]
        plnRes = allResults[10]
        vingRes = allResults[11]
        noun2Res = allResults[12]



        # Close the cursor used to query the database
        cursor.close()
        # Close the connection to the database
        conn.close()
        return render_template("index.html", 
                                adjRes = adjRes,
                                adj2Res = adj2Res,
                                birdRes = birdRes,
                                roomRes = roomRes,
                                pverbRes = pverbRes,
                                verb1Res = verb1Res,
                                nameRes = nameRes,
                                noun1Res = noun1Res,
                                liqRes = liqRes,
                                bpRes = bpRes,
                                plnRes = plnRes,
                                vingRes = vingRes,
                                noun2Res = noun2Res)
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