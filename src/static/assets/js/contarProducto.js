document.addEventListener('DOMContentLoaded', () => {
    verificaProductos();
})

const btnCantidad = document.querySelectorAll('.cantidad-btn');

btnCantidad.forEach(btn => {
    btn.addEventListener('click', () => {
        verificaProductos();
    })
})

const verificaProductos = async () => {
    try {
        const response = await fetch('/verificaProductos', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        });

        const data = await response.json();

        const cantProductosEnCarrito = document.querySelectorAll('#carrito-compras');
        
        if (cantProductosEnCarrito && data.cantidad) {
            cantProductosEnCarrito.forEach(num => {
                num.innerHTML = data.cantidad;
            });
        }
    } catch (error) {
        console.error('Error al verificar: ', error);
        return false;
    }
}
