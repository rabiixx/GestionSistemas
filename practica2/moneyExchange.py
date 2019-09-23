import json
import os
from urllib.request import urlopen

def get_rates():
	api_url = 'https://api.exchangeratesapi.io/latest'
	response = urlopen(api_url)
	data = json.loads(response.read())
	return [data['rates'], data['date']]

def convert(cantidad, de, a='EUR'):
	if(de == 'EUR'):
		return cantidad
	else:
		return float(rates[de] * cantidad)

os.system("clear")
try: 
	file = open("divisas.txt","r")
	(rates, fecha) = get_rates();
	ahorroTotal = 0.0
except IOError:
	print("El fichero divisas.txt no existe")

for linea in file:
	s = linea.rstrip();
	s = s.split(', ')
	ahorroTotal += float(convert(float(s[1]), s[0]))

file.close()

file2 = open("ahorros.txt", "a")
file2.write('{}, {}\n'.format(fecha, ahorroTotal))
file2.close()