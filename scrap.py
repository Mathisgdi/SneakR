import requests
import json
import requests

url = "http://54.37.12.181:1337/api/sneakers"

# Ajoute les paramètres de pagination à l'URL
params = {
    "pagination[pageSize]": 100,
    "pagination[page]": 1
}

# Envoie une requête GET à l'URL spécifiée avec les paramètres de pagination
response = requests.get(url, params=params)

# Récupère les données de la réponse au format JSON
data = response.json()

# Initialisation de la variable pour le contrôle de la boucle
# Initialisation de la liste pour stocker les données
data_list = []

# Initialisation de la variable pour le contrôle de la boucle

while True:
    # Envoie une requête GET à l'URL spécifiée avec les paramètres de pagination
    response = requests.get(url, params=params)

    # Récupère les données de la réponse au format JSON
    data = response.json()

    # Vérifie si des données ont été récupérées
    if len(data["data"]) == 0:
        break
    else:
        print("page", params["pagination[page]"], ":", "\n", data["data"])
        # Si des données sont disponibles, les ajoute à la liste
        data_list.extend(data["data"])

    # Incrémente le numéro de page
    params["pagination[page]"] += 1

# Une fois que toutes les données ont été récupérées, les enregistre dans un fichier JSON
with open("data.json", "w") as file:
    json.dump(data_list, file)