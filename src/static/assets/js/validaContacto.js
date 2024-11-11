document.addEventListener('DOMContentLoaded', () => {
    const formulario = document.querySelector('#formularioContacto');

    formulario.addEventListener('submit', validaInformacion);
})

const validaInformacion = (e) => {
    e.preventDefault();

    const caracteresValidosText = /^[a-zA-Z\s]+$/;

    const name = document.getElementById("name").value;
    const surname = document.getElementById("surname").value;
    const email = document.getElementById("mail").value;
    const mensaje = document.getElementById("mensaje").value;

    const nombreValidado = verificaNombre(name.trim(), caracteresValidosText);
    const apellidoValidado = verificaApellido(surname.trim(), caracteresValidosText);
    const emailValidado = verficaEmail(email.trim());
    const mensajeValidado = verficaMensaje(mensaje.trim());

    if (nombreValidado && apellidoValidado && emailValidado && mensajeValidado) {
        Swal.fire({
            icon: 'success',
            title: '¡Listo!',
            text: 'Hemos recibido su mensaje.',
            confirmButtonText: 'Aceptar'
        }).then((result) => {
            if (result.isConfirmed) {
                e.target.submit();
            }
        });
    }
}


const verficaMensaje = (msj) => {
    if (msj == '' || msj == ' ' || msj.length < 10) {
        mensajeError('Mensaje', 'El Mensaje debe tener al menos 10 caracteres.');
        return false;
    }

    ocultarError('Mensaje')
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


// Mensaje:
function mensajeError(id, msj) {
    const elemento = document.getElementById(`error${id}`);

    elemento.style.color = 'red';
    elemento.textContent = msj;
}

function ocultarError(id) {
    const elemento = document.getElementById(`error${id}`);
    elemento.textContent = '';
}