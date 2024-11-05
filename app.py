from src import crear_app, db
from typing import List, Tuple, Any
from flask import render_template, request, Response, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user, LoginManager
from flask_mail import Mail, Message

from src.models import *
from src.routes import main


app = crear_app()
app.register_blueprint(main)

# Inicializa Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# Redireccionar a la página de login si no está autenticado
login_manager.login_view = "login"  # Vista de login

# Función para cargar el usuario a partir de su ID
@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

# Configuración para el servidor SMTP de Gmail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'mateando.ando6@gmail.com'  # Correo
app.config['MAIL_PASSWORD'] = 'mjou dvrc ctuw fcld'  # Contraseña
app.config['MAIL_DEFAULT_SENDER'] = 'mateando.ando6@gmail.com'  # Remitente del correo


mail = Mail(app)


#CREACIÓN DE BASE DE DATOS

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

# PRUEBA 
# Solo entra si es_Admin = True
@app.route('/dashboard')
@login_required  # Asegura que solo los usuarios autenticados puedan acceder
def dashboard():
    # Verifica si el usuario es administrador
    if not current_user.es_admin:  # Asumiendo que 'es_admin' es un atributo booleano en el modelo Usuario
        print("No tienes permiso para acceder a esta página.") 
        return redirect(url_for('index'))  # Redirige al Inicio

    productos: List[Tuple[Any]] = Producto.query.all()
    return render_template("auth/dashboard.html", productos=productos) #Solo llega a esta línea si cumple con el atributo es_Admin
# ----


""" MOSTRAR A GIULIANNO """

""" Agregar un nuevo Usuario """
@app.route('/addUsuario', methods=["POST"])
def add_usuario() -> Response | str:
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



@app.route('/verificaEmail', methods=['POST'])
def verificaEmail():
    email = request.json.get('email')
    usuario = Usuario.query.filter_by(email=email).first()
    
    if usuario:
        return jsonify({'existe': True})
    else:
        return jsonify({'existe': False})



@app.route('/addProducto', methods=["POST"])
def add_producto() -> Response | str:
    nombre: str = request.form['nombre']
    precio: str = request.form['precio']
    image_url: str = request.form['image_url']
    id_categoria: str = request.form['categoria']
    
    nuevo_Producto: Producto = Producto(nombre=nombre, precio=float(precio), image_url=image_url, id_categoria=int(id_categoria))
    try:
        db.session.add(nuevo_Producto)
        db.session.commit()
        print("Producto agregado exitosamente")
    except Exception as e:
        #deshace cualquier cambio pendiente en la sesión de la BBDD
        db.session.rollback()
        print(f"Error al agregar el producto: {e}")

    return redirect(url_for("dashboard"))

#-------------------------------------------------------------------------------------
#AGREGADO POR JUSTI

#A TRAVÉS DE LOS BOTONES DEL DASHBOARD
#Muestra una página para editar el producto y manda como parámetro el id del producto
@app.route('/editProducto/<int:id_producto>', methods=["POST"])
def editProducto(id_producto:int):
    producto: Producto = Producto.query.get(id_producto)
    return render_template("auth/editarProducto.html", producto=producto)

#Modifica el producto seleccionado
@app.route('/editarProducto/<int:id_producto>', methods=["POST"])
def edit_producto(id_producto:int) -> Response | str:

   producto: Producto = Producto.query.get(id_producto)

   producto.nombre = request.form['nombre']
   producto.precio = request.form['precio']
   producto.image_url = request.form['image_url']
   producto.id_categoria = request.form['categoria']
   
   db.session.commit()
   return redirect(url_for("dashboard"))

#A TRAVÉS DE LOS BOTONES DEL DASHBOARD
@app.route('/eliminarProducto/<int:id_producto>', methods=["POST"])
def eliminar_producto(id_producto:int) -> Response | str:

   producto: Producto = Producto.query.get(id_producto)

   if producto:
       db.session.delete(producto)
       db.session.commit()

   return redirect(url_for("dashboard"))
   
   
#Ruta de la barra de búsqueda del header
@app.route('/buscar', methods=["GET"])
def buscar_producto():

    busqueda = request.args.get('search')  # Search es el nombre del input en el HTML

    if busqueda:
        # Realiza una búsqueda en la base de datos usando LIKE para encontrar coincidencias parciales
        productos = Producto.query.filter(Producto.nombre.ilike(f"%{busqueda}%")).all()
    else:
        productos = []  # Si no hay consulta, no devuelve resultados

    return render_template('productos.html', productos=productos, busqueda=busqueda)
    
    
@app.route('/enviarMensaje', methods=['POST'])
def enviar_mensaje():
    # Obtener datos del formulario
    nombre = request.form['name']
    apellido = request.form['surname']
    email = request.form['mail']
    mensaje = request.form['mensaje']

    # Crear el mensaje de correo
    msg = Message(
        subject="Nuevo mensaje de contacto",
        sender=app.config['MAIL_DEFAULT_SENDER'],
        recipients=['mateando.ando6@gmail.com']  # Correo del destinatario
    )
    msg.body = f"""
    Nombre: {nombre}
    Apellido: {apellido}
    Correo: {email}

    Mensaje:
    {mensaje}
    """

    try:
        # Enviar el correo
        mail.send(msg)
        print("Mensaje enviado con éxito")
    except Exception as e:
        print(e)  # Para depuración en caso de error
        print("Hubo un error al enviar el mensaje")

    return redirect('/')  # Redirecciona a la página principal


#FIN AGREGADO POR JUSTI
#--------------------------------------------------------------------------------------
@app.route('/')
def index():
    productos: List[Tuple[Any]] = Producto.query.all()
    return render_template("index.html", productos=productos)


@app.route('/contacto')
def contacto():
    return render_template('/contacto.html')


@app.route('/productos')
def productos():
    
    productos: List[Tuple[Any]] = Producto.query.all()
    return render_template('/productos.html', productos=productos)
#---------------------------------------------------------------------
#AGREGADO POR JUSTI
#Muestra los productos en la página "Productos" según la categoría que elija el cliente en el menú desplegable del nav
@app.route('/productosCat/<int:id_cat>')
def productosCat(id_cat:int):
    productos: List[Tuple[Any]] = Producto.query.filter_by(id_categoria=id_cat).all()
    return render_template('/productos.html', productos=productos)

#---------------------------------------------------------------------

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


@app.errorhandler(405)
def method_not_allowed(error):
    return render_template('errors/error405.html', error=error), 405


@app.errorhandler(500)
def internal_server():
    return render_template('errors/error500.html')

# ----


if __name__=='__main__':
    app.run(debug=True)