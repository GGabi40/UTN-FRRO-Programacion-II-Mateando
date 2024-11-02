function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
}

document.getElementById('agregar-producto-form').addEventListener('submit', function (e) {
    e.preventDefault();
    
    // Aquí iría la lógica para enviar los datos del formulario al servidor
    console.log('Producto agregado:', {
        nombre: this.nombre.value,
        precio: this.precio.value,
        image_url: this.image_url.value,
        categoria: this.categoria.value
    });
    this.reset();
});

// AGREGAR VALIDACION DE FORMULARIO