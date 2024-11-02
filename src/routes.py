from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from .models import Usuario
from . import db


main = Blueprint('main', __name__)


@main.route('/iniciarSesion', methods=['GET', 'POST'])
def iniciarSesion():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Buscar el usuario por su email
        usuario = Usuario.query.filter_by(email=email).first()
        
        # Verificar la contraseña
        if usuario and usuario.check_password(password):
            # Guardar el usuario en la sesión
            session['id_usuario'] = usuario.id_usuario
            session['nombre'] = usuario.nombre
            
            if usuario.es_admin:
                return redirect(url_for('dashboard'))
            
            flash("Inicio de sesión exitoso", "success")
            return redirect(url_for('index'))
        else:
            flash("Email o contraseña incorrectos", "danger")
    
    return render_template('index.html')


@main.route('/logout')
def logout():
    # Limpiar la sesión
    session.pop('id_usuario', None)
    session.pop('nombre', None)
    flash("Cierre de sesión exitoso", "info")
    return redirect(url_for('index'))