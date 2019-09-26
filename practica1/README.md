# Pratica 1 - Gestion de Sistema Informaticos

### Prerequisitos

Version Python 3.X

## Compilacion

Ejercutar
```
pyhton3 nombreprograma.py
```
Eliminar divisas.txt
```
make divisas
```
Eliminar ahorros.txt
```
make ahorros
```
Eliminar divisas.txt y ahorros.txt
```
make clean
```

## Informacion

* Senales: he añadido un handler de la senal SIGINT(CTR+C) con el objetivo de capturarla y cerrar el programa de forma adecuada

* He intentado capturar los errores(error handling): por ejemplo si se diera el caso de que el usuario respondiera de forma inadecuada al la pregunta si el numero de pensada
es mayor o menor o correcto al numero propuesto por la maquina, el numero que generaria la funcion 'random.ranint(min, max)' devoveria un error puesto que se pudiera dar el caso de que el intervalo fuera x > y o y < x. En este caso de captura la señal mediante el tipo de error 'ValueError', y se le avisa al usuario.

* Se ha intentando ser limpio y evitar codigo repetido o innecesario, aun asi, nunca antes habia trabajado con python y puede que haya cosas innecesarias.

* Se ha intentado seguir la estructura de clase, atributos y metodos propuesta en clase con el fin de facilitar la correcion, tal vez eso haya collaborado en que ciertas cosas resulten un tanto curisosas pero tienen su causa justificada.

## Autor

* **Ruben Cherif Narvaez** - 99rubenche@gmail.com - [rabiixx](https://github.com/rabiixx)
