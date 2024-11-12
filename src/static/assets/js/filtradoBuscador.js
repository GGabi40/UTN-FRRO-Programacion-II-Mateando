document.addEventListener('DOMContentLoaded', () => {
    inputBuscador = document.querySelector('#search');
    fetch('/obtenerProductos') // pide productos del servidor
    .then(response => response.json()) // lo convierte a json
    .then(data => {
        const productos = data; // los almacena en una var

        inputBuscador.addEventListener('input', (e) => {
            const busqueda = e.target.value.toLowerCase();
            const resultados = productos.filter(producto => producto.nombre.toLowerCase().includes(busqueda));

            // mostrar resultado filtrado:
            const contenedorProductos = document.getElementById('productos');
            contenedorProductos.innerHTML = ''; // primero lo limpia

            if(resultados.length > 0) {
                resultados.forEach(producto => {
                    const productoDiv = document.createElement('div');
                    productoDiv.classList.add('producto');
                    productoDiv.innerHTML = `
                        <div class="imagen-producto">
                            <img src="${producto.image_url}" alt="Foto Producto"/>
                        </div>
                        <div class="info-productos">
                            <span class="nombre-producto">${producto.nombre}</span>
                            <span class="precio">${producto.precio}</span>
                            <div class="acciones">
                                <form class="btn agregar-carrito" method="post" action="/editProducto/${producto.id}">
                                    <input type="submit" value="Editar Producto">
                                </form>
                                <form class="btn agregar-carrito" method="post" action="/eliminarProducto/${producto.id}">
                                    <input type="submit" value="Eliminar Producto">
                                </form>
                            </div>
                        </div>
                    `;
                    contenedorProductos.appendChild(productoDiv);
                });
            } else {
                contenedorProductos.innerHTML = '<div class="error"><p>No se encontraron resultados.</p></div>'
            }
        })
    })
    .catch(error => {
        console.error('Error al obtener productos: ', error);
    })

})