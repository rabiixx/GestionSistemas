'''

n = 5

a = []

for i in range(n):
	el = input('Elemento: ')
	a.append(el)

print(a)
'''

# split(): convierte un string en vector

'''
lista = input("Introduce String: ")

print("El String introducido es: ", lista)

lista2 = lista.split()

print("Nuevo String: ", lista2)

'''

lista = 'A B C D'

print('Lista original: ', lista)

lista2 = lista.split()

print('String split: ',  lista2)

','.join(lista2)

print("String join ',':", lista2)