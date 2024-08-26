// Agarro el botón:
let mybutton = document.getElementById("myBtn");

// Cuando hago 20px de scroll desde el tope del documento, el boton aparece
window.onscroll = function() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
};

// Cuando se toca en el botón, sube al tope
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
} 