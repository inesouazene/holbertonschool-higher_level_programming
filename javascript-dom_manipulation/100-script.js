document.addEventListener('DOMContentLoaded', () => {
  // Sélectionne les éléments nécessaires
  const myList = document.querySelector('.my_list');
  const addItemButton = document.getElementById('add_item');
  const removeItemButton = document.getElementById('remove_item');
  const clearListButton = document.getElementById('clear_list');

  // Ajoute un nouvel élément <li> à la liste
  addItemButton.addEventListener('click', () => {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    myList.appendChild(newItem);
  });

  // Supprime le dernier élément <li> de la liste
  removeItemButton.addEventListener('click', () => {
    const lastItem = myList.lastElementChild;
    if (lastItem) {
      myList.removeChild(lastItem);
    }
  });

  // Supprime tous les éléments <li> de la liste
  clearListButton.addEventListener('click', () => {
    myList.innerHTML = '';
  });
});
