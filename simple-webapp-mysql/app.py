from flask import Flask
from flask import render_template
import socket
import mysql.connector
import os

app = Flask(__name__)

DB_Host = os.environ.get('DB_Host') or "mysql"
DB_Database = os.environ.get('DB_Database') or "mysql"
DB_User = os.environ.get('DB_User') 
DB_Password = os.environ.get('DB_Password') 
SUCCESS_IMAGE_URL = os.environ.get('SUCCESS_IMAGE_URL') #or "https://finalprojs3bucket.s3.amazonaws.com/success.jpg"
FAILURE_IMAGE_URL = os.environ.get('FAILURE_IMAGE_URL') #or "https://finalprojs3bucket.s3.amazonaws.com/failed.png"

@app.route("/")
def main():
    db_connect_result = False
    err_message = ""
    try:
        mysql.connector.connect(host=DB_Host, database=DB_Database, user=DB_User, password=DB_Password)
        color = '#39b54b'
        db_connect_result = True
    except Exception as e:
        color = '#ff3f3f'
        err_message = str(e)

    return render_template('hello.html', debug="Environment Variables: DB_Host=" + (os.environ.get('DB_Host') or "Not Set") + "; DB_Database=" + (os.environ.get('DB_Database')  or "Not Set") + "; DB_User=" + (os.environ.get('DB_User')  or "Not Set") + "; DB_Password=" + (os.environ.get('DB_Password')  or "Not Set") + "; " + err_message, db_connect_result=db_connect_result, name=socket.gethostname(), color=color, SUCCESS_IMAGE_URL=SUCCESS_IMAGE_URL, FAILURE_IMAGE_URL=FAILURE_IMAGE_URL )

@app.route("/debug")
def debug():
    color = '#2196f3'
    return render_template('hello.html', debug="Environment Variables: DB_Host=" + (os.environ.get('DB_Host') or "Not Set") + "; DB_Database=" + (os.environ.get('DB_Database')  or "Not Set") + "; DB_User=" + (os.environ.get('DB_User')  or "Not Set") + "; DB_Password=" + (os.environ.get('DB_Password')  or "Not Set"), color=color)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81)
