
import random 

## Clase Jugador
class Jugador(object):

	def __init__(self, name, tipo, numPensado):
		super(Jugador, self).__init__()
		self.arg = arg
		self.name = "name"
		self.tipo = tipo
		self.numPensado = numPensado

	def pensarNumero(self):
		if(self.tipo == "Humano"):
			self.numpensado = int(input("[+] Piense y introduzca un numero: "))

	def proponerNumero(self):
		if(self.tipo == "Humano"):
			numPropuesto = int(input("Introduzca un numero: "))
		else:
			numPropuesto = random.randint(1, 101)

	def comprNumero(self, num):
		if (self.numPensado > num):
			print("El numero es mayor")
			return False
		elif (self.numPensado < num):
			print("El numero es menor")
			return False
		else:
			print("Has acertado el numero!")
			return True


## Clase Partida
class Partida(object):

	def __init__(self, jugador1, jugador2):
		super(Partida, self).__init__()
		self.arg = arg
		self.jugador1 = jugador1
		self.jugador2 = jugador2
		self.numIntentosJ1 = 0
		self.numIntentosJ2 = 0

	def jugar(self):



		
		self.j1.pensarNumero()
		while(True):
			if(j2.comprNumero(j1.proponerNumero() == False)):
				numIntentosJ1 += 1
			else:
				print("El jugador numero 1 ha ganado!")
				break

		self.j2.pensarNumero()
		while(True):
			if(j2.comprNumero(j1.proponerNumero() == False)):
				numIntentosJ1 += 1
			else:
				print("El jugador numero 1 ha ganado!")
				break

		if(numIntentosJ1 > numIntentosJ2):
			print("El jugador 1 ha ganado la partida")
		elif(numIntentosJ1 < numIntentosJ2):
			print("El jugador 1 ha ganado la partida")
		else 
			print("Empate")
		

def main():
	
	print("Jugador1: ")
	name = str(input("\tIndica un nombre para el jugador 1: "))
	tipo = str(input("\tIndica maquina/humano : "))
	j1 = Jugador(name, tipo, random.randint(1, 101))
	
	print("Jugador2: ")
	name = str(input("\tIndica un nombre: "))
	tipo = str(input("\tIndica maquina/humano : "))
	j2 = Jugador(name, tipo, random.randint(1, 101))

	# Evito pasar numero intentos por argumento pork el valor de ambos es de 0 al inicio
	p = Partida(j1, j2, 0, 0)


if __name__ == '__main__':
	main()