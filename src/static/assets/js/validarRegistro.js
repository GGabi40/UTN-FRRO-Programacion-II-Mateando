document.addEventListener('DOMContentLoaded', () => {
    const formulario = document.getElementById('formulario');
    formulario.addEventListener('submit', validaRegistro);

})

const validaRegistro = (e) => {
    e.preventDefault();
    
    const caracteresValidosText = /^[a-zA-Z\s]+$/;

    const name = document.getElementById("name").value;
    const surname = document.getElementById("surname").value;
    const email = document.getElementById("email").value;
    const direccion = document.getElementById("direccion").value;
    const telefono = document.getElementById('tel').value;
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("passwordConfirm").value;

    const nombreValidado = verificaNombre(name.trim(), caracteresValidosText);
    const apellidoValidado = verificaApellido(surname.trim(), caracteresValidosText);
    const emailValidado = verficaEmail(email.trim());
    const telefonoValidado = verificaTelefono(telefono.trim());
    const direccionValidada = verficaDireccion(direccion.trim());
    const passswordValidada = verificaPass(password.trim(), confirmPassword.trim());


    if (nombreValidado && apellidoValidado && emailValidado && telefonoValidado && direccionValidada && passswordValidada) {
        e.target.submit();
    } else {
        alert('Verifique sus datos...');
    }
}

const verificaPass = (passOriginal, passConfirm) => {
    if (passOriginal == '' || passOriginal == ' ' || passOriginal.length < 3) {
        mensajeError('Password', 'La contraseña debe posser al menos 2 caracteres.');
        return false;
    }

    if (passOriginal != passConfirm) {
        mensajeError('ConfirmacionPassword', 'Las contraseñas deben coincidir.')
        return false;
    }

    ocultarError('Password');
    ocultarError('ConfirmacionPassword');
    return true;
}


const verficaEmail = (email) => {
    if(email.includes('@') && email.includes('.com')) {
        ocultarError('Email')
        return true;
    } else {
        mensajeError('Email', 'Introduce un email válido.');
        return false;
    }
}

const verificaTelefono = (telefono) => {
    if (telefono == '' || telefono == ' ' || telefono.length < 6) {
        mensajeError('Telefono', 'El telefono debe tener al menos 6 caracteres.');
        return false;
    }

    ocultarError('Telefono')
    return true;
}


const verficaDireccion = (direccion) => {
    if (direccion == '' || direccion == ' ' || direccion.length < 2) {
        mensajeError('Direccion', 'La dirección debe tener al menos 2 caracteres.');
        return false;
    }

    // Expresión regular para aceptar solo letras, números y espacios
    const validos = /^[a-zA-Z0-9\s]+$/;

    if (!(validos.test(direccion))) {
        mensajeError('Direccion', 'La dirección debe poseer solamente letras y números.');
        return false;
    }

    ocultarError('Direccion');
    return true;
}


const verificaApellido = (apellido, validos) => {
    if (apellido == '' || apellido == ' ' || apellido.length < 2) {
        mensajeError('Apellido', 'El apellido debe tener al menos 2 caracteres.');
        return false;
    }

    if(!(validos.test(apellido))) {
        mensajeError('Apellido', 'El apellido debe poseer solamente letras.');
        return false;
    }

    ocultarError('Apellido')
    return true;
}


const verificaNombre = (nombre, validos) => {
    if (nombre == '' || nombre == ' ' || nombre.length < 2) {
        mensajeError('Nombre', 'El nombre debe tener al menos 2 caracteres.');
        return false;
    }

    if(!(validos.test(nombre))) {
        mensajeError('Nombre', 'El nombre debe poseer solamente letras.');
        return false;
    }

    ocultarError('Nombre')
    return true;
}



/* Mensaje de error: */
function mensajeError(id, msj) {
    const elemento = document.getElementById(`error${id}`);


    elemento.textContent = msj;
}

function ocultarError(id) {
    const elemento = document.getElementById(`error${id}`);
    elemento.textContent = '';
}