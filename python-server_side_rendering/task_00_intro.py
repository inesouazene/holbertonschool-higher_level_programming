import os

def generate_invitations(template, attendees):
    # Vérifier les types d'entrée
    if not isinstance(template, str):
        print("Error: Template is not a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return

    # Vérifier si le modèle est vide
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # Vérifier si la liste des participants est vide
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Traiter chaque participant
    for index, attendee in enumerate(attendees, start=1):
        # Remplacer les placeholders dans le modèle
        try:
            personalized_content = template.format(
                name=attendee.get("name", "N/A"),
                event_title=attendee.get("event_title", "N/A"),
                event_date=attendee.get("event_date", "N/A"),
                event_location=attendee.get("event_location", "N/A")
            )
        except KeyError as e:
            print(f"Error: Missing placeholder in template - {e}")
            continue

        # Nom du fichier de sortie
        output_filename = f"output_{index}.txt"

        # Écrire le contenu personnalisé dans le fichier de sortie
        try:
            with open(output_filename, 'w') as output_file:
                output_file.write(personalized_content)
            print(f"Generated file: {output_filename}")
        except IOError as e:
            print(f"Error writing file {output_filename}: {e}")

# Exemple d'utilisation
if __name__ == "__main__":
    # Lire le modèle à partir d'un fichier
    with open('template.txt', 'r') as file:
        template_content = file.read()

    # Liste des participants
    attendees = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
    ]

    # Appeler la fonction avec le modèle et la liste des participants
    generate_invitations(template_content, attendees)
