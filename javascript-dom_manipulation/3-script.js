// Sélectionne l'élément <header> et l'élément avec l'ID toggle_header
const header = document.querySelector('header');
const toggleHeaderButton = document.getElementById('toggle_header');

// Ajoute un gestionnaire d'événement pour le clic sur toggleHeaderButton
toggleHeaderButton.addEventListener('click', () => {
  // Bascule la classe de l'élément <header> entre 'red' et 'green'
  if (header.classList.contains('red')) {
    header.classList.remove('red');
    header.classList.add('green');
  } else {
    header.classList.remove('green');
    header.classList.add('red');
  }
});
