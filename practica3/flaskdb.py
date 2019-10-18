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
	c.execute(query)
	res = c.fetchall()

	jsonfile = json.dumps(res)	
	
	return json2html.convert(json = jsonfile)

@app.route("/tablas/<nombre_de_tabla>/info/")
def query3(nombre_de_tabla):
	conn = sqlite3.connect("ejemplo.db") 
	c = conn.cursor() 
	
	query1 = "SELECT * FROM '" + str(nombre_de_tabla) + "'"
	c.execute(query1)
	res = c.fetchall()
	
	lineas = len(res)
	columnas = len(res[0])
	num_reg = lineas * columnas
	
	query2 = "SELECT group_concat(name, ' | ') FROM  pragma_table_info('" + nombre_de_tabla + "')"
	c.execute(query2)
	res = c.fetchall()
	
	aux1 = "Numero de registros: " + str(num_reg)
	aux2 = "Numero de lineas: " + str(lineas)
	aux3 = "Numero de columnas: " + str(columnas)
	jsonfile = json.dumps(res)

	return (json2html.convert(json = aux1)) + (json2html.convert(json = aux2)) + (json2html.convert(json = aux3)) + json2html.convert(json = jsonfile)  

if __name__ == "__main__":
	app.run()

