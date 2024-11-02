from . import db
import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class Categoria(db.Model):
    __tablename__ = 'categoria'
    
    id_Categoria = db.Column(db.Integer, primary_key=True)
    nombre_categoria = db.Column(db.String(50), nullable=False)



class Productos(db.Model):
    __tablename__ = 'productos'
    
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
    id_producto = db.Column(db.Integer, db.ForeignKey('productos.id_Producto'))
    cantidad = db.Column(db.Integer, nullable=False)
    precio_unidad = db.Column(db.Float, nullable=False)



class Carrito(db.Model):
    __tablename__ = 'carrito'
    
    id_carrito = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'))
    fecha_creacion = db.Column(db.Date, default=datetime.datetime.now())



class Usuario(db.Model):
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
    
    

