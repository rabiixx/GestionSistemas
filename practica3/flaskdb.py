import sqlite3 
from flask import Flask


app = Flask(__name__)
@app.route("/")
def connect_db():
	conn = sqlite3.connect("ejemplo.db") 
	c = conn.cursor() 
	query = ("SELECT * FROM USER_TABLES")
	c.execute(query)
	res = c.fetchall()
	json.dumps(res)


