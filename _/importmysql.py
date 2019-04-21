import mysql.connector
from flask import Flask, redirect, url_for, request, render_template

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="mangekyo77",
#   database="curiousningen",
#   auth_plugin="mysql_native_password"
# )

# mycursor = mydb.cursor()
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World’

if __name__ == '__main__':
   app.run()
