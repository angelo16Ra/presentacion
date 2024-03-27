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
            <title>Los Avengers - Iron Man</title>
            <style>
              body {
                  font-family: Arial, sans-serif;
                  margin: 0;
                  padding: 0;
                  background-color: #f0f0f0;
                  text-align: center;
              }
              .container {
                  max-width: 800px;
                  margin: 0 auto;
                  padding: 20px;
                  background-color: #fff;
                  border-radius: 10px;
                  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
              }
              h1 {
                  color: #333;
              }
              p {
                  color: #555;
                  line-height: 1.6;
              }
              img {
                  max-width: 100%;
                  height: auto;
                  border-radius: 5px;
                  margin-bottom: 20px;
              }
            </style>
        </head>
        <body>
          <div class="container">
              <h1>Iron Man - Tony Stark</h1>
              <img src="https://i.pinimg.com/564x/46/99/f6/4699f6ecd0109cffb82decd8d937ab72.jpg" alt="Foto de Iron Man">
              <p>
                  <strong>Nombre:</strong> Tony Stark<br>
                  <strong>Alias:</strong> Iron Man<br>
                  <strong>Descripción:</strong> Iron Man es un superhéroe que aparece en los cómics estadounidenses publicados por Marvel Comics. El personaje fue creado por el escritor y editor Stan Lee en colaboración con el guionista Larry Lieber. Los artistas Don Heck y Jack Kirby fueron los encargados de su diseño.
                  <strong>Nombre del estudiante:</strong> Angelo Rodriguez Altez<br>
                  <strong>Correo:</strong> i2226467@continental.edu.pe<br>
              </p>
          </div>
       </body>
       </html>
      '''
if __name__ == "__main__":
       app,run(debug=True)
