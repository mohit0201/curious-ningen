import mysql.connector
from flask import Flask, redirect, url_for, request, render_template , send_file

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mangekyo77",
  database="curiousningen",
  auth_plugin="mysql_native_password"   
)

mycursor = mydb.cursor()
app = Flask(__name__)

@app.route('/')
def home():
    t="Registered"
    return render_template('logins.html',result=t)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login1')
def login1():
    return render_template('login.html')

@app.route('/anime')
def anime():
    return render_template('anime.html')
@app.route('/movies')
def movies():
    return render_template('movies.html')
@app.route('/TV')
def TV():
    return render_template('TV.html')

@app.route('/registered')
def registered():
    return render_template('login.html')
@app.route('/url' ,methods=['POST','GET'])
def url():
    if request.method == 'POST':
        username=request.form['usernamer']
        password=request.form['passwordr']
        email=request.form['emailr']
        sql = "INSERT INTO registration VALUES(%s, %s, %s)"
        val = (username,password,email)
        print (username)
        mycursor.execute(sql,val)
        mydb.commit()
    else:
        print ("notfound")
    return redirect(url_for('registered'))    
@app.route('/login' ,methods=['POST','GET'])
def login():
    if request.method == 'POST':
        username=request.form['usernamel']
        password=request.form['passwordl']
        mycursor.execute("SELECT * from registration")
        result=mycursor.fetchall()
        for row in result:
            if row[0]==username and row[1]==password:
                return render_template('index.html',result=username)

    # print(mycursor.fetchall())
    # for row in iter_row(mycursor):
    #     print(row[0])
        # email=request.form['emailr']
        # sql = "INSERT INTO registration VALUES(%s, %s, %s)"
        
        # val = (username,password,email)
        # print (username)
        # mycursor.execute(sql,val)
        # mydb.commit()
    # else:
    #     print ("notfound")
    return "ごめなさい！You are not a member."
if __name__ == '__main__':
    app.debug=True
    app.run()
