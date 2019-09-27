'''
con flask y sqlite3 crear un explorador de bases de datos

Listar tablas, url: /tablas
tablas nombre: tabla muestra contenido en json

pasar variables: @app.route("/<nombre variable>"): lo k pongas en la url lo añade como arg y se lo añade a lo k muestre
json.dump: devolver objeto en formato json
crear servidor que se permita explorar las tablas de la base de datos
que devuelva solo el registro correspondiente a la clave primaria

Instalar librerias: setting/project/project interpreter
'''
'''
import sqlite3 
from flask import Flask

conn = sqlite3.connect("ejemplo.db") 
c = conn.cursor() 
c.execute("SELECT * FROM Clientes;") 
print(c.fetchone())conn.close()

app = Flask(__name__)
@app.route("/")
def hello():
	return "hello world"
		'''

	# Acceso base de datos
	def db_quey(query):
		# Nos conectamos a la base de datos
		conn = sqlite3.connect(app.config['db'])
		# Creamos objeto cursor
		c = conn.cursor()
		# Se realiza la consulta indicada por el usuario
		c.execute(query)
		# Obtenemos resultados
		res = c.fetchall()
		#Mostramos resultados
		for fila in res:
			print(res)
		# Se cierra conexion con base de datos
		conn.close()

	@app.route("/")
	@app.route("/tablas")
	def tablas():
		query = ("*selec....")	
		res = db.query(query)
		return json.dumps(res)

	@app.route("/")
	@app.route("/tablas/<arg>")
	def tablas():
		query = ("*selec....")	
		res = db.query(query)
		return json.dumps(res)


	@app.route("/")
	@app.route("/tablas")
	def tablas():
		query = ("*selec....")	
		res = db.query(query)
		return json.dumps(res)


if __name__ == "__main__":
	app.run()