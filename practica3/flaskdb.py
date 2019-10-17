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
	query = "SELECT * from '" + nombre_de_tabla + "'"
	#query  = "SELECT * FROM " + str(nombre_de_tabla)
	c.execute(query)
	res = c.fetchall()
	print(res)
	print("\n----------------------------------------------------------------------\n")
	jsonfile = json.dumps(res)
	print(jsonfile)
	print("\n----------------------------------------------------------------------\n")
	item_dict = json.loads(jsonfile)
	print(item_dict)
	print("\n----------------------------------------------------------------------\n")
	print(item_dict[1])
	print("\n----------------------------------------------------------------------\n")
	for x in item_dict[0]:
		print(x)
	print("\n----------------------------------------------------------------------\n")
	return json2html.convert(json = jsonfile)

@app.route("/tablas/<nombre_de_tabla>/info/")
def query3(nombre_de_tabla):
	conn = sqlite3.connect("ejemplo.db") 
	c = conn.cursor() 
	
	query1 = "SELECT group_concat(name, ' | ') FROM  pragma_table_info('" + nombre_de_tabla + "')"
	query2 = "SELECT COUNT (*) FROM '"+ nombre_de_tabla + "'"
	
	c.execute(query1)
	res = c.fetchall()
	print(res)
	print(res[0])
	print(res[4])
	jsonfile1 = json.dumps(res)
	print(jsonfile1)

	c.execute(query2)
	res = c.fetchall()
	jsonfile2 = json.dumps(res)

	return json2html.convert(json = jsonfile1) + ( json2html.convert(json = jsonfile2))
	#return render_template("tablas.html")

if __name__ == "__main__":
	app.run()

