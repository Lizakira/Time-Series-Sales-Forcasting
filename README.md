
# **Prédiction avec LightGBM via une API Flask**

Ce projet implémente une API Flask pour déployer un modèle LightGBM afin de prédire `item_cnt_day`. L'API permet d'effectuer des requêtes programmatiques pour tester les prédictions.

## **Étapes pour utiliser l'API**

### **1. Exécuter le serveur Flask**
Dans un terminal, exécutez le fichier `api.py` pour démarrer le serveur :
```bash
python api.py
```

Vous verrez un message indiquant que l'API est en cours d'exécution :
```
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

### **2. Tester l'API via un script Python**
Dans un autre terminal, exécutez le fichier `test_api.py` pour envoyer une requête à l'API. Ce fichier contient un exemple de vecteur de test extrait de `x_test`.

Exécutez la commande suivante :
```bash
python test_api.py
```

Le script enverra une requête POST avec un vecteur de test, et la réponse sera affichée dans le terminal sous la forme suivante :
```
Réponse de l'API : {"prediction": 3.25}
```

---

## **Fichiers du projet**

1. **`api.py`**
   - Démarre le serveur Flask et charge le modèle LightGBM.
   - Fournit une API REST pour effectuer des prédictions.
   
2. **`test_api.py`**
   - Envoie une requête POST à l'API avec un exemple de vecteur de test.
   - Affiche la réponse de l'API dans le terminal.


---

## **Prérequis**
Assurez-vous d’avoir installé les bibliothèques nécessaires :
```bash
pip install flask lightgbm numpy
```

---

## **Structure du projet**

```
my_project/
│
├── api.py                # API Flask
├── test_api.py           # Script pour tester l'API
├── lgb_model.txt    # Modèle LightGBM entraîné
```

---

## **Notes**
- Assurez-vous que le fichier `lgb_model.txt` est présent dans le même répertoire que `api.py`.
- Le port par défaut utilisé par l'API est `5000`. Si ce port est occupé, modifiez-le dans `api.py` :
  ```python
  app.run(debug=True, host="0.0.0.0", port=5000)
  ```
