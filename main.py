from flask import Flask, render_template, request, redirect, session
import json
import pwinput
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="D24$m?!tdy",
    database="pythonclub"
)


def check_cred(uname, pword):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM login_info;")
    if (uname, pword) in cursor:
        print('credentials approved login successful')
        return 'sucess'
    else:
        return 'error'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/processUserInfo/<string:userInfo>', methods=['POST'])
def processUserInfo(userInfo):
    userinfo = json.loads(userInfo)
    print(f"\nRECEIVED DATA, PROCESSING CREDENTIALS OF USER\n ------------------------------------")
    return check_cred(userinfo.get('name'), userinfo.get('pass'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
