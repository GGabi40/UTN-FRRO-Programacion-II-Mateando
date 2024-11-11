from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import current_user
from .models import Usuario, Carrito
from . import db


main = Blueprint('main', __name__)

from flask_login import login_user

@main.route('/validarCredenciales', methods=['POST'])
def validar_credenciales():
    try:
        email = request.json.get('email')
        password = request.json.get('password')

        usuario = Usuario.query.filter_by(email=email).first()

        if usuario and usuario.check_password(password):
            return jsonify({'success': True})
        else:
            return jsonify({'success': False, 'message': 'Email o contraseña incorrectos'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})



@main.route('/iniciarSesion', methods=['GET', 'POST'])
def iniciarSesion():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        usuario = Usuario.query.filter_by(email=email).first()
        
        if usuario and usuario.check_password(password):
            login_user(usuario)  # Usa este método para loguear al usuario
            flash("Inicio de sesión exitoso", "success")
            
            carrito = Carrito.query.filter_by(id_usuario=current_user.id_usuario).first()
            
            if not carrito:
                nuevoCarrito: Carrito = Carrito (
                    id_usuario = usuario.id_usuario,
                    total = 0
                )
            
                db.session.add(nuevoCarrito)
                db.session.commit()
                
            return redirect(url_for('dashboard' if usuario.es_admin else 'index'))
        else:
            flash("Email o contraseña incorrectos", "danger")
    
    return redirect(url_for("index"))



from flask_login import logout_user

@main.route('/logout')
def logout():
    logout_user()  # Cierra la sesión del usuario
    flash("Cierre de sesión exitoso", "info")
    return redirect(url_for('index'))
