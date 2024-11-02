from src import crear_app, db
from typing import List, Tuple, Any
from flask import render_template, request, Response, redirect, url_for

from src.models import *
from src.routes import main


app = crear_app()
app.register_blueprint(main)

@app.route('/database')
def database():
    init_db()
    return "Base de datos creada correctamente."

""" Crea BBDDs """
def create_db():
    db.drop_all()
    db.create_all()

""" VER DONDE PONER """

""" Método de inicialización de nuestra BBDD """
def init_db():
    create_db()
    
    # user admin app
    admin = Usuario(
        nombre = 'admin',
        apellido = '1',
        email = 'admin@mateando.com',
        es_admin = True,
        telefono = '3415555555',
        direccion = 'Cordoba 1234'
    )
    admin.set_password("123")
    db.session.add(admin)
    db.session.commit()

"""  """




# Rutas:

# PRUEBA --- Si es Admin
@app.route('/dashboard')
def dashboard():
    return render_template('auth/dashboard.html')
# ----


""" MOSTRAR A GIULIANNO """

""" Agregar un nuevo Usuario """
@app.route('/add', methods=["POST"])
def add_contact() -> Response | str:
    name: str = request.form["name"]
    apellido: str = request.form["surname"]
    email: str = request.form["email"]
    telefono: str = request.form["tel"]
    direccion: str = request.form["direccion"]
    password: str = request.form["password"]
	
    nuevo_Usuario: Usuario = Usuario(nombre=name, apellido=apellido, email=email, telefono=telefono, direccion=direccion)
    nuevo_Usuario.set_password(password)

    db.session.add(nuevo_Usuario)
    db.session.commit()

    return redirect(url_for("index"))


@app.route('/addProducto', methods=["POST"])
def add_producto() -> Response | str:
    nombre: str = request.form['nombre']
    precio: str = request.form['precio']
    image_url: str = request.form['image_url']
    id_categoria: str = request.form['categoria']
    
    nuevo_Producto: Productos = Productos(nombre=nombre, precio=float(precio), image_url=image_url, id_categoria=int(id_categoria))
    try:
        db.session.add(nuevo_Producto)
        db.session.commit()
        print("Producto agregado exitosamente")
    except Exception as e:
        db.session.rollback()
        print(f"Error al agregar el producto: {e}")

    return redirect(url_for("dashboard"))


@app.route('/')
def index():
    productos: List[Tuple[Any]] = Productos.query.all()
    return render_template("index.html", productos=productos)


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