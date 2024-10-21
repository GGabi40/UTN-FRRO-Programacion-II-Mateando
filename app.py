# Es el archivo principal donde definirás las rutas, 
# la conexión a la base de datos y el manejo de las vistas.
from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route('/')

def index():
    return render_template('/index.html')


if __name__=='__main__':
    app.run(debug=True)