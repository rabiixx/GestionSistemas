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

@app.route("/tablas/")
def query1(tabla):
	conn = sqlite3.connect("ejemplo.db") 
	c = conn.cursor() 
	query  = "select * from sqlite_master where type='table';"
	c.execute(query)
	res = c.fetchall()
	return json.dumps(res)

@app.route("(tablas/<tabla>/")
def query2(tabla):
	conn = sqlite3.connect("ejemplo.db") 
	c = conn.cursor() 
	query  = "SELECT * FROM " + str(tabla)
	print(query)
	#query = "SELECT * FROM Clientes"
	c.execute(query)
	res = c.fetchall()
	return json.dumps(res)
	#return render_template("tablas.html")

@app.route("(tablas/<tabla>/<campo>")
def query3(tabla, campo):
	conn = sqlite3.connect("ejemplo.db") 
	c = conn.cursor() 
	query  = "SELECT " + campo + " FROM " + tabla
	print(query)
	#query = "SELECT * FROM Clientes"
	c.execute(query)
	res = c.fetchall()
	return json.dumps(res)
	#return render_template("tablas.html")
'''
if __name__ == "__main__":
	app.run()

