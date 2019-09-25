
import random
import os

## Clase Jugador
class Jugador(object):

	def __init__(self, name, tipo, numPensado, numPropuesto, res, minNum, maxNum):
		super(Jugador, self).__init__()
		self.name = name
		self.tipo = tipo
		self.numPensado = numPensado
		self.numPropuesto = numPropuesto 
		self.res = res
		self.minNum = minNum
		self.maxNum = maxNum

	#def pensarNumero(self):
		#self.numPensado = int(input("[+] %s piense e introduzca un numero: " % self.name))

	def proponerNumero(self):
		
		if(self.tipo == "Humano"):
			return int(input("[+] %s introduzca un numero: " % self.name))
		else:

			if ( (self.res == 'Mayor') or (self.res == 'mayor') ):
				if (self.numPropuesto > self.minNum):
					self.minNum = self.numPropuesto + 1
			elif ( (self.res == 'Menor') or (self.res == 'menor') ):
				if (self.numPropuesto < self.maxNum):
					self.maxNum = self.numPropuesto - 1

			self.numPropuesto = random.randint(self.minNum, self.maxNum)

			print("El número que has pensado es el %d" %self.numPropuesto)

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
			return input("Mayor/Menor/Correcto?: ")

## Clase Partida
class Partida(object):

	def __init__(self, jugador1, jugador2):
		super(Partida, self).__init__()
		self.j1 = jugador1
		self.j2 = jugador2

	def jugar(self):

		numIntentosJ1 = 0;
		numIntentosJ2 = 0;

		print("Bueno, %s, estoy pensando en un número entre 1 y 100. Intenta adivinarlo." %self.j1.name)

		while (self.j2.comprNumero(self.j1.proponerNumero()) == False):
			numIntentosJ1 += 1
		
		print("[+] ¡Buen trabajo, %s ¡Has adivinado mi número en %d intentos! Es tu turno." % (self.j1.name, numIntentosJ1))

		#self.j2.pensarNumero()
		
		while ( (self.j2.res != 'Correcto') or (self.j2.res != 'correcto') ):
			self.j2.res = self.j1.comprNumero(self.j2.proponerNumero())
			print(self.j2.res)
			numIntentosJ2 += 1
		
		print("[+] La partida ha finalizado.")
		print("[+] Numero intentos: ")
		print("\t- %s: %d" % (self.j1.name, numIntentosJ1))
		print("\t- Yo: %d\n" %numIntentosJ2)

		if (numIntentosJ1 > numIntentosJ2):
			return input("[+] Yo gano. He acertado en %d intentos. Quieres seguir jugando? [S/N]: " % numIntentosJ2)
		elif (numIntentosJ1 < numIntentosJ2):
			return input("[+] Tu ganas. Has acertado en %d intentos. Quieres seguir jugando? [S/N]: " % numIntentosJ1)
		else: 
			print("[+] Empate. Quieres seguir jugando? [S/N]: ")
		

def main():
	
	os.system("clear");
	print("[+] Bienvenido")
	name = str(input("\t[+] !Hola¡ ¿Como te llamas?: "))
	j1 = Jugador(name, "Humano", 0, 0, ' ', 0, 10)
	j2 = Jugador("BuggedBot", "Maquina", random.randint(1, 10), 0 , ' ', 0, 10)

	# Evito pasar numero intentos por argumento pork el valor de ambos es de 0 al inicio
	p = Partida(j1, j2)
	p.jugar()

	'''
	while(p.jugar() == 'S'):
		if(input("Deseas cambiarte de nombre? [S/N]: ") == 'S'):
			name = input("Introduzca el nuevo nombre: ")
			j1 = Jugador(name, "Humano", 0)
			p.jugar()
		else:
			p.jugar()
	'''

if __name__ == '__main__':
	main()