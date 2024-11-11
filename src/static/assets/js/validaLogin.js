document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');

    loginForm.addEventListener('submit', async function(event) {
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;

        // verifica si está vacío
        if (!email || !password) {
            event.preventDefault();

            Swal.fire({
                icon: 'error',
                title: 'Error',
                text: 'Por favor, complete todos los campos.'
            });
            return;
        }

        // verifica del formato del correo
        const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
        if (!emailRegex.test(email)) {
            event.preventDefault();
            Swal.fire({
                icon: 'error',
                title: 'Error',
                text: 'El correo electrónico no es válido.'
            });
            return;
        }

        // si está todo bien, enviamos al servidor para validar las credenciales
        try {

            const response = await fetch('/validarCredenciales', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ email, password })
            });
            debugger;
            const data = await response.json();

            
            console.log(response);
            console.log(data);
            
            

            if (response.ok && data.success) {
                // Si está todo bien, se permite el envío del formulario
                loginForm.submit();
            } else {
                // Si no, tira error (por ejemplo, credenciales incorrectas)
                event.preventDefault();
                Swal.fire({
                    icon: 'error',
                    title: 'Error',
                    text: data.message || 'Hubo un error al validar las credenciales.'
                });
            }
            debugger;
        } catch (error) {
            // si algo sale mal, maneja el error:
            console.error('Error al validar las credenciales:', error);
            Swal.fire({
                icon: 'error',
                title: 'Error',
                text: 'Hubo un problema al procesar la solicitud. Inténtalo nuevamente.'
            });
        }
    });
});
