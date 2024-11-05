document.addEventListener('DOMContentLoaded', () => {
    inputBuscador = document.querySelector('#search');
    inputBuscador.addEventListener('input', filtraBuscador);
})

const filtraBuscador = (e) => {
    console.log(e.target.value);
}