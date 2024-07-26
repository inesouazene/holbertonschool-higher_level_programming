// Sélectionne l'élément avec l'ID add_item et le <ul> avec la classe my_list
const addItemButton = document.getElementById('add_item');
const myList = document.querySelector('.my_list');

// Ajoute un gestionnaire d'événement pour le clic sur addItemButton
addItemButton.addEventListener('click', () => {
  // Crée un nouvel élément <li> et définit son contenu
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';

  // Ajoute le nouvel élément <li> à la fin de la liste <ul> my_list
  myList.appendChild(newItem);
});
