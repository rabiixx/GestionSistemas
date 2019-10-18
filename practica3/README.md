# Pratica 3 - Gestion de Sistema Informaticos

### Prerequisitos

Version Python 3.X

Required Packages: 

```
pip install flask.py
```
```
pip install json2html 
```

## Compilacion

Ejercutar
```
pyhton3 flaskdb.py
```

## Informacion

* About: muestra una breve descripcion sobre la aplicacion web
* /tablas: muestra el nombre de las tablas de la base de datos
* /tablas/nombretabla: muestra todos los campos de una tabla
* /tablas/nombretabla/info: muestra el numero de registros de la tabla

* Se han añadido alguna platilla html con la intencion de merorar el aspecto visual. Dichas plantillas se encuentran en el directorio templates(html) asi como static/css(css).

* Se ha incluido el plugin json2html que convierte un archivo json en codigo html. De esta forma el resultado de la consulta se muestra de una forma mas amigable para el usuario

* Se ha intentando ser limpio y evitar codigo repetido o innecesario, aun asi, nunca antes habia trabajado con python y puede que haya cosas innecesarias.



## Autor

* **Ruben Cherif Narvaez** - 99rubenche@gmail.com - [rabiixx](https://github.com/rabiixx)
