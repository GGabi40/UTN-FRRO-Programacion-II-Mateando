document.addEventListener('DOMContentLoaded', () => {
    const checkboxes = document.querySelectorAll('.filter-checkbox');
    const productosContainer = document.querySelector('.producto-categoria');

    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', actualizaProductos);
    });

    function actualizaProductos() {
        const categorias = Array.from(checkboxes)
            .filter(checkbox => checkbox.checked)
            .map(checkbox => checkbox.dataset.filter);

        fetch('/filtrar', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ categorias })
        })
        .then(response => response.json())
        .then(data => {
            //Saqué la línea de abajo porq directamente saco los productos de "data"
            // const producto = data;
            productosContainer.innerHTML = '';

            if(data.productos.length > 0) {
                // Faltaba agregar un for que recorra todos los elementos que trae data
                data.productos.forEach(producto => {
                const productoHTML = `
                <div class="producto">
                    <div class="imagen-producto">
                        <img src="${producto.image_url}" alt="Foto Producto" />
                    </div>
                    <div class="info-producto">
                        <span class="nombre-producto"><strong class="unid-producto">${producto.nombre}</strong></span>
                        <span class="precio">${producto.precio}</span>
                        <div class="acciones">
                            <button class="btn agregar-carrito">Agregar al carrito</button>
                            <button class="btn comprar">Comprar</button>
                        </div>
                    </div>
                </div>`;

                productosContainer.insertAdjacentHTML('beforeend', productoHTML);
            });
            } else {
                // Url de la imagen modificada. No usar JINJA, sino HTML normal
                const productoHTML = `
                <div class="error">
                    <div class="mensaje-error">
                        <h2>¡Lo sentimos!</h2>
                        <p>No se encontraron resultados.</p>
                    </div>
                    <div class="mate">
                        <img src="./static/assets/img/error/404.png" alt="Foto Sin Resultados">
                    </div>
                </div>`;

                productosContainer.insertAdjacentHTML('beforeend', productoHTML);
            }
        })
        .catch(error => console.error('Error:', error));
    }

});