from . import db


class Productos(db.Model):
    __tablename__ = 'productos'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(200), nullable=True)
    
    def __repr__(self) -> str:
        return f"<Productos {self.nombre} {self.precio}>"




