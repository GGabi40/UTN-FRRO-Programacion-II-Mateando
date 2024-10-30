from src import crear_app, db
from flask import render_template

app = crear_app()


""" class Productos(db.Model):
    __tablename__ = 'productos'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(200), nullable=True)
    
    def __repr__(self) -> str:
        return f"<Productos {self.nombre} {self.precio}>"



with app.app_context():
    db.create_all()
 """

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



# Ruta para Errores

@app.errorhandler(404)
def no_encontrado(error):
    return render_template('errors/error404.html', error=error)

@app.errorhandler(500)
def internal_server():
    return render_template('errors/error500.html')

# ----


if __name__=='__main__':
    app.run(debug=True)