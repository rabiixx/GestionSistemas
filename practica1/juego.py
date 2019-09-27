
import random
import signal
import sys
import os
import time


# Captura la señal SIGINT (CTR+C para los amigos)
def signal_handler(sig, frame):
	
	print("\n[+] Has pulsado CTR+C!, adios.")
	sys.exit(0)
	

## Clase Jugador
class Jugador(object):

	def __init__(self, name, tipo, numPensado, numPropuesto, res, minNum, maxNum):
		super(Jugador, self).__init__()
		self.name = name 					# Nombre del jugador
		self.tipo = tipo					# Tipo de jugador: Humano/Maquina
		self.numPensado = numPensado		# Numero pensado por el jugador
		self.numPropuesto = numPropuesto 	# Numero propuesto por el jugador
		self.res = res 						# Almacena si el numero propuesto es mayor, menor o correcto
		self.minNum = minNum				# Minimo corrrespondiente al intervalo de generacion de numero aleatorios
		self.maxNum = maxNum				# Maximo corrrespondiente al intervalo de generacion de numero aleatorios


     # Metodo proponerNumero
     # Si el jugador es humano, se le pregunta al jugador que numero quiere introducir
     # si no, se acota el intervalo y se genera un nuevo aleatorio pertenciente al intervalo acotado
     # @return el numero propuesto por el usuario o el genrado aleatoriamente 
	def proponerNumero(self):
		
		if(self.tipo == "Humano"):
			return int(input("[+] %s introduzca un numero: " % self.name))
		else:
			# Acotacion del intervalo de generacion de numero aleatorios
			if ( self.res.lower() == 'mayor' ):
				if (self.numPropuesto >= self.minNum):
					self.minNum = self.numPropuesto + 1
			elif ( self.res.lower() == 'menor' ):
				if (self.numPropuesto <= self.maxNum):
					self.maxNum = self.numPropuesto - 1

			# Control de ValueError: [x, y] ^ x > y
			try:
				self.numPropuesto = random.randint(self.minNum, self.maxNum)
			except ValueError:
				print("[+] Te ha has equivocado.")

			print("[+] El número que has pensado es el %d" %self.numPropuesto)

	# Metodo comprNumero
	# Si es una maquina se comprueba si el numero num es mayor, menor o correcto
	# Humano: se le indica que el mismo introduzca si es mayor, menor o correcto para que el bot
	# pueda acotar el intervalo de generacion de numeros aleatorios
	# @return bot: si ha acaertado el numero True, si no, False
	# @return humano: numero mayor/menor/correcto
	def comprNumero(self, num):
		
		if (self.tipo == 'Maquina'):
			if (self.numPensado > num):
				print("[+] El numero pensado es mayor")
				return False
			elif (self.numPensado < num):
				print("[+] El numero pensado es menor")
				return False
			else:
				print("[+] %s Has acertado el numero!" % self.name)
				return True
		else:
			return input("[+] Mayor/Menor/Correcto?: ")


## Clase Partida
class Partida(object):

	def __init__(self, jugador1, jugador2):
		super(Partida, self).__init__()
		self.j1 = jugador1
		self.j2 = jugador2

	def jugar(self):

		numIntentosJ1 = 1;
		numIntentosJ2 = 1;

		print("[+] Bueno, %s, estoy pensando en un número entre 1 y 100. Intenta adivinarlo." %self.j1.name)

		while (self.j2.comprNumero(self.j1.proponerNumero()) == False):
			numIntentosJ1 += 1
		
		print("[+] ¡Buen trabajo, %s ¡Has adivinado mi número en %d intentos! Es tu turno." % (self.j1.name, numIntentosJ1))
		
		while ( (self.j2.res.lower() != "correcto") ):
			self.j2.res = self.j1.comprNumero(self.j2.proponerNumero())
			if(self.j2.minNum < self.j2.maxNum):	# ValueError Handling
				numIntentosJ2 += 1

		print("[+] La partida ha finalizado.")

		file = open("historial.db", "a")
		file.write('{}: {} - {}: {}\n'.format(self.j1.name, numIntentosJ1, self.j2.name, numIntentosJ2) )
		file.close()

		print("[+] Numero intentos: ")
		print("\t- %s: %d" % (self.j1.name, numIntentosJ1))
		print("\t- Yo: %d\n" %numIntentosJ2)

		if (numIntentosJ1 > numIntentosJ2):
			return input("[+] Yo gano. He acertado en %d intentos. Quieres seguir jugando? [S/N]: " % numIntentosJ2)
		elif (numIntentosJ1 < numIntentosJ2):
			return input("[+] Tu ganas. Has acertado en %d intentos. Quieres seguir jugando? [S/N]: " % numIntentosJ1)
		else: 
			return input("[+] Empate. Quieres seguir jugando? [S/N]: ")
		

def main():
	
	os.system("clear");

	print("[+] Bienvenido")
	name = str(input("[+] !Hola¡ ¿Como te llamas?: "))
	random.seed(time.time())

	j1 = Jugador(name, "Humano", 0, 0, ' ', 0, 100)
	j2 = Jugador("BuggedBot", "Maquina", random.randint(1, 10), 0 , ' ', 0, 100)

	p = Partida(j1, j2)
	restart = p.jugar()

	while( restart.lower().startswith('s') ):
		if ( input("[+] Deseas cambiarte de nombre? [S/N]: ").lower().startswith('s') ):
			random.seed(time.time())
			name = input("[+] Introduzca el nuevo nombre: ")
			j1 = Jugador(name, "Humano", 0, 0, ' ', 0, 10)
			j2 = Jugador("BuggedBot", "Maquina", random.randint(1, 100), 0 , ' ', 0, 100)
			p = Partida(j1, j2)
			restart = p.jugar()
		else:
			random.seed(time.time())
			j1 = Jugador(name, "Humano", 0, 0, ' ', 0, 10)
			j2 = Jugador("BuggedBot", "Maquina", random.randint(1, 100), 0 , ' ', 0, 100)
			p = Partida(j1, j2)
			restart = p.jugar()

if __name__ == '__main__':
	signal.signal(signal.SIGINT, signal_handler)
	main()
	

