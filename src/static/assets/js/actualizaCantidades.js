document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.cantidad-btn').forEach(boton => {
        boton.addEventListener('click', (e) => {
            e.preventDefault();

            const action = e.target.getAttribute('data-action');
            const idProducto = e.target.getAttribute('data-id');

            actualizaCantidades(idProducto, action);
        })
    })
})

const actualizaCantidades = (idProducto, action) => {
    fetch(`/actualizarCantidad`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ idProducto, action }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            const cantidadElement = document.querySelector(`.cantidad[data-id="${idProducto}"]`);
            cantidadElement.textContent = data.newQuantity;

            document.querySelector('.precio-total').textContent = data.newTotal;
        } else {
            console.error('Error al actualizar.')
        }
    });
};