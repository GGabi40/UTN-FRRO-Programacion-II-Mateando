from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from flask_login import login_required, current_user, LoginManager
from .models import Usuario, Carrito
from . import db


main = Blueprint('main', __name__)


from flask_login import login_user

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
    
    return render_template('index.html')



from flask_login import logout_user

@main.route('/logout')
def logout():
    logout_user()  # Cierra la sesión del usuario
    flash("Cierre de sesión exitoso", "info")
    return redirect(url_for('index'))
