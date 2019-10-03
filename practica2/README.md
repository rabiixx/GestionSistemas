# Pratica 1 - Gestion de Sistema Informaticos

### Prerequisitos

Version Python 3.X

## Compilacion

Ejercutar
```
pyhton3 nombreprograma.py
```
o
```
make all
```

Eliminar divisas.txt
```
make divisas
```
o 

```
make clean
```

## Informacion

* El fichero ahorros.txt se crea automaticamente al ejecutarse el programa, por tanto, no es necesario que el fichero exista previamente a la ejecucion. 

* En el caso del fichero divisas.txt es extrictamente necesario para la correcta ejecucion del programa, por ello, si el fichero no existe se captura el error y se avisa de que el fichero.txt no existe.

* Se ha intentando ser limpio y evitar codigo repetido o innecesario, aun asi, nunca antes habia trabajado con python y puede que haya cosas innecesarias.

* Se han añadido un interfaz de linea de comandos haciendo uso del paquete [Click](https://click.palletsprojects.com/en/7.x/). Las opciones del programa pueden	ser consultadas mediante:
```
python3 moneyExachange.py --help
```
Las siguiente opciones han sido añadidas:
  --ifilename TEXT  Name of the input file.
  --ofilename TEXT  Name of the output file.
  --borrar INTEGER  Clears the output file.
  --help            Show this message and exit.

## Autor

* **Ruben Cherif Narvaez** - 99rubenche@gmail.com - [rabiixx](https://github.com/rabiixx)