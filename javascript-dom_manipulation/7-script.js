// URL de l'API pour obtenir la liste des films
const apiUrl = 'https://swapi-api.hbtn.io/api/films/?format=json';

// Sélectionne l'élément <ul> avec l'ID list_movies
const listMoviesElement = document.getElementById('list_movies');

// Utilisation de l'API Fetch pour obtenir les données des films
fetch(apiUrl)
  .then(response => response.json()) // Convertit la réponse en JSON
  .then(data => {
    // Pour chaque film, crée un <li> avec le titre et l'ajoute à la liste
    data.results.forEach(film => {
      const listItem = document.createElement('li');
      listItem.textContent = film.title;
      listMoviesElement.appendChild(listItem);
    });
  })
  .catch(error => {
    // Gère les erreurs éventuelles
    console.error('Error fetching data:', error);
  });
