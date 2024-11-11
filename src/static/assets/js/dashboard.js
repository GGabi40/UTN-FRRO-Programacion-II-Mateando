// MODO OSCURO
const darkModeButton = document.querySelector('.modo-oscuro');
const body = document.body;

darkModeButton.addEventListener('click', toggleDarkMode);

function toggleDarkMode() {
  body.classList.toggle("dark-mode");

  const enModoOscuro = body.classList.contains('dark-mode');
  localStorage.setItem('darkMode', enModoOscuro);
  darkModeButton.textContent = enModoOscuro ? 'Modo Claro' : 'Modo Oscuro';
}

const modoOscuroGuardado = localStorage.getItem('darkMode');
if (modoOscuroGuardado === 'true') {
    body.classList.add('dark-mode');
    darkModeButton.textContent = 'Modo Claro';
}

// FORMULARIO
document.addEventListener("DOMContentLoaded", () => {
  const formulario = document.getElementById("agregar-producto-form");

  formulario.addEventListener("submit", validaProductos);
});

const validaProductos = (e) => {
  e.preventDefault();

  const nombre = document.querySelector("#nombre").value;
  const categoria = document.querySelector("#categoria").value;
  const precio = document.querySelector("#precio").value;

  const nombreValidado = verificaNombre(nombre.trim());
  const categoriaValidado = verificaCategoria(categoria);
  const precioValidado = verificaPrecio(precio);

  if (nombreValidado && categoriaValidado && precioValidado) {
    Swal.fire({
      icon: "success",
      title: "¡Listo!",
      text: "Se ha agregado el producto con éxito.",
      confirmButtonText: "Aceptar",
    }).then((result) => {
      if (result.isConfirmed) {
        e.target.submit();
      }
    });
  }
};

const verificaPrecio = (precio) => {
  if (precio <= 0) {
    mensajeError("Precio", "El precio debe ser mayor que 0.");
    return false;
  }

  if (isNaN(precio)) {
    mensajeError("Precio", "El precio debe ser un número.");
    return false;
  }

  ocultarError("Precio");
  return true;
};

const verificaCategoria = (categoria) => {
  if (categoria == "") {
    mensajeError("Categoria", "Debe elegir una categoría.");
    return false;
  }

  ocultarError("Categoria");
  return true;
};

const verificaNombre = (nombre) => {
  if (nombre == "" || nombre == " " || nombre.length < 3) {
    mensajeError("Nombre", "El nombre debe tener al menos 3 caracteres.");
    return false;
  }

  ocultarError("Nombre");
  return true;
};

// Mensaje:
function mensajeError(id, msj) {
  const elemento = document.getElementById(`error${id}`);

  elemento.style.color = "red";
  elemento.textContent = msj;
}

function ocultarError(id) {
  const elemento = document.getElementById(`error${id}`);
  elemento.textContent = "";
}
