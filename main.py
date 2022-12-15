from flask import Flask, render_template, request, redirect, session
import json
import mysql.connector

app = Flask(__name__)

login_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="abc123",
    database="sample"
)


def check_cred(uname, pword):
    cursor = login_db.cursor()
    cursor.execute("SELECT * FROM sample_table;")
    if (uname, pword) in cursor:
        print('credentials approved login successful')
        return 'sucess'
    else:
        return 'error'
#str because booleans cant be processed by JSON and ajax to be posted

@app.route('/')
def index():
    return render_template('index.html')
#renders from templates folder

@app.route('/processUserInfo/<string:userInfo>', methods=['POST'])
def processUserInfo(userInfo):
    userinfo = json.loads(userInfo)
    print(f"\nRECEIVED DATA, PROCESSING CREDENTIALS OF USER\n ------------------------------------")
    return check_cred(userinfo.get('name'), userinfo.get('pass'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
#change port in regards to whatever is most accessible on your router
