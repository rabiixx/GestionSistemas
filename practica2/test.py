'''
Supongamos que tenemos un fichero divisas.txt en el que tenemos un listado del dinero que tenemos en distintas divisas:

USD, 1000
EUR, 1500
GBP, 1300

Utilizando la API que https://exchangeratesapi.io/ ofrece con los valores de cambio, deberéis crear un programa que al ejecutarse,
añada una nueva línea al fichero ahorros.txt con la fecha y el valor total de los ahorros en euros según el cambio en ese momento.
El fichero ahorros.txt tendrá la estructura

2019-09-01, 4520
2019-09-02, 4535
...

El programa definirá al menos una clase ExchangeAPIClient que gestionará la conexión con la API y la conversión de los valores de las divisas.

Deberéis subir el código a vuestro repositorio de github y colocar aquí el enlace a la carpeta. Añadid un archivo README.md a la carpeta en el que describiréis brevemente vuestro enfoque
'''


from urllib.request import urlopen
import json


def get_rates():
	api_url = 'https://api.exchangeratesapi.io/latest'
	response = urlopen(api_url)
	print(response)
	rates = json.loads(response.read())
	print(rates)
	return rates['rates']

def convert(cantidad, de='EUR', a='USD'):
	rates = get_rates()
	return rates['USD'] * cantidad


with open("divisdad.txt")

cantidad_en_euros = 100
cantidad_en_dolares = convert(cantidad_en_euros)
print('{} euros son {} dólares'.format(cantidad_en_euros, cantidad_en_dolares))

'''
{'rates': 
	{'CAD': 1.4636, 
	'HKD': 8.6413, 
	'ISK': 137.0, 
	'PHP': 57.375, 
	'DKK': 7.4668, 
	'HUF': 332.89, 
	'CZK': 25.913, 
	'AUD': 1.6243, 
	'RON': 4.7456, 
	'SEK': 10.7113, 
	'IDR': 15502.67, 
	'INR': 78.2925, 
	'BRL': 4.5956, 
	'RUB': 70.3933, 
	'HRK': 7.4008, 
	'JPY': 119.11, 
	'THB': 33.636, 
	'CHF': 1.0942, 
	'SGD': 1.5176, 
	'PLN': 4.3575, 
	'BGN': 1.9558, 
	'TRY': 6.2894, 
	'CNY': 7.8207, 
	'NOK': 9.9423, 
	'NZD': 1.7579, 
	'ZAR': 16.3991, 
	'USD': 1.103, 
	'MXN': 21.4558, 
	'ILS': 3.8837, 
	'GBP': 0.8823, 
	'KRW': 1311.24, 
	'MYR': 4.5995 }, 
'base': 'EUR', 
'date': '2019-09-20'}
'''