import sqlite3 
from flask import Flask, render_template
import json
from json2html import *

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/tablas/")
def query1():
	conn = sqlite3.connect("ejemplo.db") 
	c = conn.cursor() 
	query  = "SELECT name FROM sqlite_master WHERE TYPE = 'table'"
	c.execute(query)
	res = c.fetchall()
	jsonfile = json.dumps(res)
	
	return json2html.convert(json = jsonfile)

@app.route("/tablas/<nombre_de_tabla>/")
def query2(nombre_de_tabla):
	conn = sqlite3.connect("ejemplo.db") 
	c = conn.cursor() 
	query = "SELECT group_concat(name,' | ') from pragma_table_info("nombre_de_tabla")"
	#query  = "SELECT * FROM " + str(nombre_de_tabla)
	c.execute(query)
	res = c.fetchall()
	jsonfile = json.dumps(res)
	return json2html.convert(json = jsonfile)

@app.route("/tablas/<nombre_de_tabla>/info")
def query3(nombre_de_tabla):
	conn = sqlite3.connect("ejemplo.db") 
	c = conn.cursor() 
	query  = "SELECT " + campo + " FROM " + tabla
	c.execute(query)
	res = c.fetchall()
	jsonfile = json.dumps(res)
	return json2html.convert(json = jsonfile)
	#return render_template("tablas.html")

if __name__ == "__main__":
	app.run()

