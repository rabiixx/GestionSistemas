con flask y sqlite3 crear un explorador de bases de datos

Listar tablas, url: /tablas
tablas nombre: tabla muestra contenido en json

pasar variables: @app.route("/<nombre variable>"): lo k pongas en la url lo añade como arg y se lo añade a lo k muestre
json.dump: devolver objeto en formato json
crear servidor que se permita explorar las tablas de la base de datos
que devuelva solo el registro correspondiente a la clave primaria