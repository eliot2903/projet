```markdown
# 🔐 Plateforme de Cryptographie - Projet NSI

## 📝 Description
Ce projet est une application web interactive développée avec **Flask** qui permet de sécuriser des messages en utilisant plusieurs méthodes de chiffrement historiques et informatiques. Elle offre une interface moderne pour expérimenter le **Chiffre de Vigenère**, le **Chiffre de Vernam**, le **Chiffre de Trithémius** et la conversion **Hexadécimale**.

## ✨ Fonctionnalités
* `Chiffre de Vigenère` : Cryptage et décryptage de textes à l'aide d'une clé alphabétique.
* `Chiffre de Vernam` : Utilisation d'une clé à usage unique et aléatoire de la même longueur que le message pour une sécurité maximale.
* `Chiffre de Trithémius` : Chiffrement par décalage progressif automatique (sans clé).
* `Conversion Hexadécimale` : Transformation de texte clair en base 16 et inversement.
* `Gestion des clés` : Génération automatique de clés pour Vernam et vérification de leur unicité via une base de données (`cle.db`) et un fichier de sauvegarde (`cle.txt`).
* `Historique des messages` : Suivi des 10 dernières opérations de chiffrement stockées en base de données SQLite.
* `Mode Jeu` : Un module interactif pour s'entraîner à décoder des messages en hexadécimal.

## 🛠 Technologies utilisées
* `Back-end` : Python 3, Flask, SQLite3.
* `Front-end` : HTML5, CSS3 (avec plusieurs thèmes de style) et JavaScript.

## 🚀 Installation et Lancement
### Prérequis
* Avoir Python installé sur votre machine.

### Installation
1. Installez la bibliothèque Flask :
   pip install flask
   
```

### Lancement

1. Lancez le script principal :
```bash
python app.py

```


2. Ouvrez votre navigateur à l'adresse suivante : `http://127.0.0.1:5000`

## 📁 Structure du projet

* `app.py` : Serveur principal gérant les routes, le jeu et la logique de l'application.
* `python/cryptage.py` : Module contenant les algorithmes de chiffrement (Vigenère, Vernam, Trithémius, Hexa) et les tests unitaires (`assert`).
* `python/cle.db` & `python/historique.db` : Bases de données SQLite pour garantir l'unicité des clés et stocker l'historique.
* `python/cle.txt` : Registre de secours pour l'unicité des clés de Vernam.
* `templates/` : Pages HTML (Accueil, interfaces de cryptage, descriptions, jeu et historique).
* `static/` : Fichiers de style (CSS multiples) et scripts JavaScript pour l'interactivité et Logo .

---

## adresse web :
```bash
https://cryptographie-k5wx.onrender.com
https://cryptographie.ddns.net
```

* hebergé sur render.com
* nom de domaine sur no.ip 

**Auteurs :** Eliot / Clément
