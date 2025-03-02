from flask import Flask, request, jsonify
import numpy as np
import lightgbm as lgb

# Charger le modèle LightGBM
model = lgb.Booster(model_file='lgb_model.txt')

# Initialiser l'application Flask
app = Flask(__name__)

# Route pour la prédiction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Récupérer les données envoyées via POST
        data = request.get_json()

        # Vérifier que les données contiennent 'input'
        if 'input' not in data:
            return jsonify({'error': 'Key "input" is missing'}), 400

        # Convertir les données en tableau NumPy
        input_data = np.array(data['input']).reshape(1, -1)

        # Faire une prédiction
        prediction = model.predict(input_data)

        # Retourner la prédiction
        return jsonify({'prediction': prediction.tolist()})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Lancer le serveur Flask
if __name__ == '__main__':
    app.run(debug=True)
