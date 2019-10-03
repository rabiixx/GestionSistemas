from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ejemplo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.Model.metadata.reflect(db.engine)

class Clients(db.Model):
	__table__ = db.Model.metadata.tables['Clientes']
	def __repr__(self):
		return self.Nombre

Clients.query.all()

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	def __repr__(self):
		return '<User {}>'.format(self.username)

db.create_all()
db.session.commit()

u = User(username='susan', email='susan@example.com')
db.session.add(u)
db.session.commit()
u = User.query.get(1)