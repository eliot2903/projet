-Plateforme de Cryptographie - Projet NSI

-Description:

Ce projet est une application web interactive développée avec Flask qui permet de sécuriser des messages en utilisant trois méthodes de chiffrement historiques : le Chiffre de Vigenère , le Chiffre de Vernam et le chiffrement en Héxadécimal.

-Fonctionnalités:

    Chiffre de Vigenère : Cryptage et décryptage de textes à l'aide d'une clé alphabétique.

    Chiffre de Vernam : Utilisation d'une clé à usage unique et aléatoire de la même longueur que le message pour une sécurité maximale.

    Gestion des clés : Génération automatique de clés uniques pour Vernam et vérification de leur unicité via un fichier de stockage (cle.txt).

    Conversion Hexadécimale : Fonctions de support pour transformer du texte en hexadécimal.

-Technologies utilisées

    Langage : Python(flask)

    Front-end : HTML, CSS et JavaScript 

-Installation et Lancement:
-Prérequis:

    Avoir Python installé sur votre machine.

-Installation:

    Installez la bibliothèque Flask :
    Bash

    pip install flask

-Lancement:

    Lancez le serveur Flask :
    
    lancer le script app.py

    Ouvrez votre navigateur à l'adresse suivante : http://127.0.0.1:5000

-Structure du projet

    app.py : Serveur principal gérant les routes et la logique de l'application.

    python/cryptage.py : Module contenant les algorithmes de chiffrement et les tests unitaires.

    python/cle.txt : Registre servant à garantir l'unicité des clés de Vernam.

    templates/ : Pages HTML.

    static/ : Fichiers de style CSS et scripts JavaScript.

Auteur : Eliot / Clément
