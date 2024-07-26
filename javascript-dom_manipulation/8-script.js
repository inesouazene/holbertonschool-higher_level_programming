document.addEventListener('DOMContentLoaded', () => {
  // URL de l'API pour obtenir la traduction de "hello" en français
  const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  // Sélectionne l'élément avec l'ID hello
  const helloElement = document.getElementById('hello');

  // Utilisation de l'API Fetch pour obtenir la traduction de "hello"
  fetch(apiUrl)
    .then(response => response.json()) // Convertit la réponse en JSON
    .then(data => {
      // Affiche la traduction de "hello" dans l'élément hello
      helloElement.textContent = data.hello;
    })
    .catch(error => {
      // Gère les erreurs éventuelles
      console.error('Error fetching data:', error);
    });
});
