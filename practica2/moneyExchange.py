import json
import os
from urllib.request import urlopen
import click

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



@click.command()
@click.option('--ifilename', prompt='Input file', help='Name of the input file.')
@click.option('--ofilename', prompt='Output file', help='Name of the output file.')
@click.option('--borrar', default = 0, help='Clears the output file.')



def main(ifilename, ofilename, borrar):

	os.system("clear")
	#try: 
	file = open(str(ifilename), "r")
	(rates, fecha) = get_rates();
	ahorroTotal = 0.0
	#except IOError:
	print("El fichero divisas.txt no existe")

	for linea in file:
		s = linea.rstrip();
		s = s.split(', ')
		ahorroTotal += float(convert(float(s[1]), s[0]))

	file.close()
	if (clear == 1):
		file2 = open(ofilename, "w")
	else:
		file2 = open(ofilename, "a")

	file2.write('{}, {}\n'.format(fecha, ahorroTotal))
	file2.close()


if __name__ == "__main__":
	main()

