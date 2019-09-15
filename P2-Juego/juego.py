
import random

## Clase Jugador
class Jugador(object):

	def __init__(self, name, tipo, numPensado):
		super(Jugador, self).__init__()
		self.name = name
		self.tipo = tipo
		self.numPensado = numPensado

	def pensarNumero(self):
		if(self.tipo == "Humano"):
			self.numPensado = int(input("[+] %s piense e introduzca un numero: " % self.name))

	def proponerNumero(self):
		if(self.tipo == "Humano"):
			return int(input("[+] %s introduzca un numero: " % self.name))
		else:
			return random.randint(1, 10)

	def comprNumero(self, num):
		if (self.numPensado > num):
			print("[+] El numero pensado es mayor")
			return False
		elif (self.numPensado < num):
			print("[+] El numero pensado es menor")
			return False
		else:
			print("[+] Has acertado el numero!" % self.name)
			return True


## Clase Partida
class Partida(object):

	def __init__(self, jugador1, jugador2):
		super(Partida, self).__init__()
		self.j1 = jugador1
		self.j2 = jugador2
		self.numIntentosJ1 = 0
		self.numIntentosJ2 = 0

	def jugar(self):

		self.j1.pensarNumero()
		while (True):
			if (self.j1.comprNumero(self.j2.proponerNumero()) == False):
				self.numIntentosJ2 += 1
			else:
				print("[+] %s ha realizado %d intentos." % ( self.j2.name, self.numIntentosJ2))
				break

		self.j2.pensarNumero()
		while (True):
			if (self.j2.comprNumero(self.j1.proponerNumero()) == False):
				self.numIntentosJ1 += 1
			else:
				print("[+] %s ha realizado %d intentos." % (self.j1.name, self.numIntentosJ1))
				break

		print("[+] La partida ha finalizado.")
		if (self.numIntentosJ1 > self.numIntentosJ2):
			print("[+] %s ha ganado la partida" % self.j2.name)
		elif (self.numIntentosJ1 < self.numIntentosJ2):
			print("[+] El jugador 1 ha ganado la partida" % self.j1.name)
		else: 
			print("[+] Empate")
		

def main():
	
	print("[+] Jugador 1: ")
	name = str(input("\t- Indica un nombre para el jugador 1: "))
	tipo = str(input("\t- Indica maquina/humano : "))
	j1 = Jugador(name, tipo, random.randint(1, 10))

	print("Jugador 2: ")
	name = str(input("\t- Indica un nombre: "))
	tipo = str(input("\t- Indica maquina/humano : "))
	j2 = Jugador(name, tipo, random.randint(1, 10))

	# Evito pasar numero intentos por argumento pork el valor de ambos es de 0 al inicio
	p = Partida(j1, j2)

	p.jugar()


if __name__ == '__main__':
	main()