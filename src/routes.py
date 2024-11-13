from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import current_user
from .models import Usuario, Carrito
from . import db


main = Blueprint('main', __name__)

from flask_login import login_user

def creaCarrito(usuario):
    carrito = Carrito.query.filter_by(id_usuario=current_user.id_usuario).first()
            
    if not carrito:
        nuevoCarrito: Carrito = Carrito (
            id_usuario = usuario.id_usuario
        )

        db.session.add(nuevoCarrito)
        db.session.commit()


@main.route('/iniciarSesion', methods=['GET', 'POST'])
def iniciarSesion():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        usuario = Usuario.query.filter_by(email=email).first()
        
        if usuario and usuario.check_password(password):
            login_user(usuario)  # Usa este método para loguear al usuario
            
            # crear carrito
            creaCarrito(usuario)
                
            return redirect(url_for('dashboard' if usuario.es_admin else 'index'))
        else:
            flash("Email o contraseña incorrectos", "danger")
            return redirect(url_for('login'))
    
    return redirect(url_for("index"))



from flask_login import logout_user

@main.route('/logout')
def logout():
    logout_user()  # Cierra la sesión del usuario
    return redirect(url_for('index'))
