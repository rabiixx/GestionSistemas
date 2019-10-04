import sqlite3 
from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route("/")
def home():
	return render_template("home.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/<tabla>")
def connect_db():
	conn = sqlite3.connect("ejemplo.db") 
	c = conn.cursor() 
	query  = "SELECT * FROM {}".format(tabla)
	#query = "SELECT * FROM Clientes"
	c.execute(query)
	res = c.fetchall()
	return json.dumps(res)
	#return render_template("tablas.html")
'''
@app.route("/tablas/<IdCliente>")
def connect_db():
	conn = sqlite3.connect("ejemplo.db") 
	c = conn.cursor() 
	
	query = ("SELECT * FROM Clientes")
	c.execute(query)
	res = c.fetchall()
	json.dumps(res)
	return render_template("tablas.html")
'''
if __name__ == "__main__":
	app.run()

