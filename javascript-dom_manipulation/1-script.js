// Sélectionne l'élément <header> et l'élément avec l'ID red_header
const header = document.querySelector('header');
const redHeaderButton = document.getElementById('red_header');

// Ajoute un gestionnaire d'événement pour le clic sur redHeaderButton
redHeaderButton.addEventListener('click', () => {
  header.style.color = '#FF0000'; // Change la couleur du texte de l'élément <header> en rouge
});
