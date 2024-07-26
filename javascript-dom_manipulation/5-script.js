// Sélectionne l'élément <header> et l'élément avec l'ID update_header
const header = document.querySelector('header');
const updateHeaderButton = document.getElementById('update_header');

// Ajoute un gestionnaire d'événement pour le clic sur updateHeaderButton
updateHeaderButton.addEventListener('click', () => {
  // Met à jour le texte de l'élément <header>
  header.textContent = 'New Header!!!';
});
