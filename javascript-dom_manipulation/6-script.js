// URL de l'API pour obtenir les détails du personnage
const apiUrl = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

// Sélectionne l'élément avec l'ID character
const characterElement = document.getElementById('character');

// Utilisation de l'API Fetch pour obtenir les données du personnage
fetch(apiUrl)
  .then(response => response.json()) // Convertit la réponse en JSON
  .then(data => {
    // Affiche le nom du personnage dans l'élément character
    characterElement.textContent = data.name;
  })
  .catch(error => {
    // Gère les erreurs éventuelles
    console.error('Error fetching data:', error);
  });
