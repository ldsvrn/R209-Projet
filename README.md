# Projet R209 (Django)

## Sujet:
Votre projet porte sur un schéma avec des contenants et des contenus (des catégories et des livres de chaque catégorie par exemple)

Il devra comporter donc: 

- 2 modèles et les formulaires associés
- 2 CRUD (1 par modèle) et les vue ALL associées
- La gestion de la relation entre les 2 modèles
- de la mise en forme CSS
- l'usage d'un squelette de gabarit pour uniformiser le site 
- le dépôt sur GITHUB.

Il va sans dire que votre site doit être navigable à partir de la page d'accueil sans avoir besoin de taper les requêtes dans le navigateur autre que celle de la page d'accueil.

Vous déposez dans un fichier doc, le lien du dépôt GitHub et l'url de votre page d'accueil. le Github doit rester actif jusqu'à la fin de l'année minimum.

## Sujet choisi:
Contenant: Systèmes d'exploitations
Contenu: Version (de système d'exploitation)
Les deux CRUD sont liés grâce au bouton "Détails" dans la liste des OS.
Pour l'instant, un bug empêche les nouvelles OS d'apparaître dans le drop down sans le redémarrage du serveur.
Le projet utilise bootstrap. 

## Mise en place:
- Création du venv, installation dépendances
```bash
py -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
- Lancement du serveur
```bash
./manage.py runserver
```