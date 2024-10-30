from flask import Flask, render_template
import os

# Config
db_path: str = 'sqlite:///' + os.path.abspath(os.path.dirname(__file__)) + '/db/db.sqlite'

app: Flask = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# -----

# Rutas:

@app.route('/')
def index():
    return render_template('/index.html')


@app.route('/contacto')
def contacto():
    return render_template('/contacto.html')


@app.route('/productos')
def productos():
    return render_template('/productos.html')


@app.route('/faq')
def faq():
    return render_template('/faq.html')


@app.route('/mateTips')
def mateTips():
    return render_template('/mateTips.html')

@app.route('/quienesSomos')
def quienesSomos():
    return render_template('/quienesSomos.html')


@app.route('/carrito')
def carrito():
    return render_template('/carrito.html')


@app.route('/recuperarContrasenia')
def recuperarContrasenia():
    return render_template('/recuperarContrasenia.html')


@app.route('/login')
def login():
    return render_template('/login.html')


@app.route('/registrarse')
def registrarse():
    return render_template('/registrarse.html')

# ----

if __name__=='__main__':
    app.run(debug=True)