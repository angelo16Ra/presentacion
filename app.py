from flask import Flask

app = Flask (__name__)

@app.route("/")
def portada():
      return '''
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Los Avengers</title>
        </head>
        <body>
            <h1>Personaje favorito</h1>
            <img src="https://i.pinimg.com/564x/46/99/f6/4699f6ecd0109cffb82decd8d937ab72.jpg" alt="foto de iro man">
            <p>Nombre: tony stark</p>
            <p>Iron Man es un superhéroe que aparece en los cómics estadounidenses publicados por Marvel Comics. El personaje fue creado por el escritor y editor Stan Lee en colaboración con el guionista Larry Lieber.​ Los artistas Don Heck y Jack Kirby fueron los encargados de su diseño.</p>
        </body>
        </html>
      '''
if __name__ == "__main__":
       app,run(debug=True)
