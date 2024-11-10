from . import db
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin




class Categoria(db.Model):
    __tablename__ = 'categoria'
    
    id_Categoria = db.Column(db.Integer, primary_key=True)
    nombre_categoria = db.Column(db.String(50), nullable=False)



class Producto(db.Model):
    __tablename__ = 'producto'
    
    id_Producto = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(200), nullable=True)
    id_categoria = db.Column(db.Integer, db.ForeignKey('categoria.id_Categoria'))
    
    def __repr__(self) -> str:
        return f"<Productos {self.nombre} {self.precio}>"



class Producto_Carrito(db.Model):
    __tablename__ = 'producto_carrito'
    
    id_Producto_Carrito = db.Column(db.Integer, primary_key=True)
    id_carrito = db.Column(db.Integer, db.ForeignKey('carrito.id_carrito'))
    id_producto = db.Column(db.Integer, db.ForeignKey('producto.id_Producto'))
    cantidad = db.Column(db.Integer, nullable=False)
    precio_unidad = db.Column(db.Float, nullable=False)
    
    producto = db.relationship('Producto', backref='productos_carrito')



class Carrito(db.Model):
    __tablename__ = 'carrito'
    
    id_carrito = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'))
    fecha_creacion = db.Column(db.Date, default=datetime.datetime.now())
    total = db.Column(db.Float, nullable=False)


class Venta(db.Model):
    __tablename__ = 'venta'
    
    id_venta = db.Column(db.Integer, primary_key=True)
    id_carrito = db.Column(db.Integer, db.ForeignKey('carrito.id_carrito'))
    nro_factura = db.Column(db.Integer, unique=True, nullable=False)


class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuario'
    
    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    telefono = db.Column(db.String(15), nullable=False)
    direccion = db.Column(db.String(150), nullable=False)
    es_admin = db.Column(db.Boolean, nullable=False, default=False)
    password_hash = db.Column(db.String(250), nullable=False)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def get_id(self):
        return str(self.id_usuario)

    def is_authenticated(self):
        return True # Flask-Login ya lo gestiona con UserMixin

    def is_active(self):
        return True  # Esto controla si el usuario puede iniciar sesión
    
    def is_anonymous(self):
        return False  # Para usuarios no autenticados
    


