document.addEventListener('DOMContentLoaded', () => {
  // Sélectionne les éléments nécessaires
  const languageSelect = document.getElementById('language_code');
  const translateButton = document.getElementById('btn_translate');
  const helloElement = document.getElementById('hello');

  // Ajoute un gestionnaire d'événement pour le clic sur le bouton de traduction
  translateButton.addEventListener('click', () => {
    // Récupère le code de langue sélectionné
    const lang = languageSelect.value;

    // Vérifie qu'une langue a été sélectionnée
    if (lang) {
      // URL de l'API pour obtenir la traduction de "Hello"
      const apiUrl = `https://hellosalut.stefanbohacek.dev/?lang=${lang}`;

      // Utilisation de l'API Fetch pour obtenir la traduction de "Hello"
      fetch(apiUrl)
        .then(response => response.json()) // Convertit la réponse en JSON
        .then(data => {
          // Affiche la traduction de "Hello" dans l'élément hello
          helloElement.textContent = data.hello;
        })
        .catch(error => {
          // Gère les erreurs éventuelles
          console.error('Error fetching data:', error);
          helloElement.textContent = 'Error fetching translation.';
        });
    } else {
      // Affiche un message d'erreur si aucune langue n'est sélectionnée
      helloElement.textContent = 'Please select a language.';
    }
  });
});
