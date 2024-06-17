// Obtén el botón o checkbox que activará/desactivará el modo oscuro
const toggleDarkModeButton = document.getElementById('toggle-dark-mode');

// Agrega un evento de clic o cambio al botón o checkbox
toggleDarkModeButton.addEventListener('click', function() {
  // Obtén la etiqueta <body>
  const body = document.querySelector('body');

  // Alternar la clase 'dark-mode' en la etiqueta <body>
  body.classList.toggle('dark-mode');
});
