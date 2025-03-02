import requests

# URL de l'API
url = 'http://127.0.0.1:5000/predict'

# Exemple de données d'entrée
data = {
    'input': [24,53,17015,-0.226030,6,1,2015,-0.116985]  # Exemple d'un vecteur de x_test
}

# Envoyer une requête POST
response = requests.post(url, json=data)

# Afficher la réponse
print("Status Code:", response.status_code)
print("Response JSON:", response.json())
