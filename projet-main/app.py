from flask import Flask, render_template, request
from programme.cryptage import *
import sqlite3
import datetime
import os

chemin = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'programme')



app = Flask(__name__)


@app.route('/')
def home():
    return render_template("Page_d'accueil.html")

@app.route('/desc_hexa')
def desc_hexa():
    return render_template("Description_Hexadecimal.html")

@app.route('/desc_vernam')
def desc_vernam():
    return render_template("Description_Vernam.html")

@app.route('/desc_vigenere')
def desc_vigenere():
    return render_template("Description_Vigenère.html")

@app.route('/desc_trithemius')
def desc_trithemius():
    return render_template("Description_Trithémius.html")

@app.route('/desc_cesar')
def desc_cesar():
    return render_template("Description_César.html")

@app.route('/desc_rot13')
def desc_rot13():
    return render_template("Description_ROT13.html")

@app.route('/jeu')
def jeu():
    return render_template("Jeu.html")

@app.route('/vernam', methods=['GET', 'POST'])
def vernam():
    if request.method == 'POST':
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        if "Entre_texte" in request.form:
            saisie = request.form.get("Entre_texte")
            if saisie:
                message = Chiffre_de_Vernam(saisie)
                ajouter_historique("Vernam", saisie, message[0], date) 
                return render_template('Chiffre_de_Vernam.html', resultat=message[1], resultat2=message[0])
        
        elif "Entre_texte2" in request.form:
            saisie = request.form.get("Entre_texte2")
            cle = request.form.get("Cle2")
            if saisie and cle:
                message = Chiffre_de_Vernam(saisie, cle, "decryptage")
                ajouter_historique("Vernam", saisie, message, date)
                return render_template('Chiffre_de_Vernam.html', resultat3=message)
            
    return render_template('Chiffre_de_Vernam.html')

@app.route('/vigenere', methods=['GET', 'POST'])
def vigenere():
    if request.method == 'POST':
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if "Entre_texte" in request.form:
            saisie = request.form.get("Entre_texte")
            cle = request.form.get("Cle")
            if saisie and cle:
                message = chiffre_de_vigenère(saisie, cle)
                ajouter_historique("Vigenère", saisie, message, date) 
                return render_template('Chiffre_de_Vigenère.html', resultat=message)
        
        elif "Entre_texte2" in request.form:
            saisie = request.form.get("Entre_texte2")
            cle = request.form.get("Cle2")
            if saisie and cle:
                message = chiffre_de_vigenère(saisie, cle, "decryptage")
                ajouter_historique("Vigenère", saisie, message, date)
                return render_template('Chiffre_de_Vigenère.html', resultat2=message)
            
    return render_template('Chiffre_de_Vigenère.html')

@app.route('/historique')
def historique():
    conn = sqlite3.connect(os.path.join(chemin, 'historique.db'))
    cursor = conn.cursor()
    cursor.execute('SELECT methode, texte_original, resultat, date FROM historique ORDER BY id DESC LIMIT 10')
    donnees = cursor.fetchall()
    conn.close()
    return render_template('historique.html', historique=donnees)

@app.route('/hexa', methods=['GET', 'POST'])
def hexa():
    if request.method == 'POST':
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if "Entre_texte" in request.form:
            saisie = request.form.get("Entre_texte")
            if saisie: 
                message = cryptage_en_hexa(saisie)
                ajouter_historique("Héxadécimal", saisie, message, date)
                return render_template('Hexadecimal.html', resultat2=message)
        
        elif "Entre_texte2" in request.form:
            saisie = request.form.get("Entre_texte2")
            if saisie:  
                try:
                    message = cryptage_en_hexa(saisie, "decryptage")
                    ajouter_historique("Héxadécimal", saisie, message, date)
                    return render_template('Hexadecimal.html', resultat3=message)
                except ValueError:
                    return render_template('Hexadecimal.html', resultat3="Erreur : Code hexadécimal invalide")
        
    return render_template('Hexadecimal.html')

@app.route('/trithemius', methods=['GET', 'POST'])
def trithemus():
    if request.method == 'POST':
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Formulaire de Cryptage soumis
        if "Entre_texte" in request.form:
            saisie = request.form.get("Entre_texte")
            if saisie:
                message = chiffre_de_Trithémius(saisie)
                ajouter_historique("Trithémius", saisie, message, date)
                return render_template('Chiffre_de_Trithémius.html', resultat1=message)
        
        # Formulaire de Décryptage soumis
        elif "Entre_texte2" in request.form:
            saisie = request.form.get("Entre_texte2")
            if saisie:
                message = chiffre_de_Trithémius(saisie, "decryptage")
                ajouter_historique("Trithémius", saisie, message, date)
                return render_template('Chiffre_de_Trithémius.html', resultat2=message)

    return render_template('Chiffre_de_Trithémius.html')


@app.route('/cesar', methods=['GET', 'POST'])
def cesar():
    if request.method == 'POST':
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if "Entre_texte" in request.form:
            saisie = request.form.get("Entre_texte")
            decalage = request.form.get("Decalage")
            if saisie and decalage:
                try:
                    decalage = int(decalage)
                    message = chiffre_de_cesar(saisie, decalage)
                    ajouter_historique("César", saisie, message, date)
                    return render_template('Chiffre_de_César.html', resultat=message)
                except ValueError:
                    return render_template('Chiffre_de_César.html', resultat="Erreur : décalage invalide")

        elif "Entre_texte2" in request.form:
            saisie = request.form.get("Entre_texte2")
            decalage = request.form.get("Decalage2")
            if saisie and decalage:
                try:
                    decalage = int(decalage)
                    message = chiffre_de_cesar(saisie, decalage, "decryptage")
                    ajouter_historique("César", saisie, message, date)
                    return render_template('Chiffre_de_César.html', resultat2=message)
                except ValueError:
                    return render_template('Chiffre_de_César.html', resultat2="Erreur : décalage invalide")

    return render_template('Chiffre_de_César.html')


@app.route('/rot13', methods=['GET', 'POST'])
def rot13():
    if request.method == 'POST':
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if "Entre_texte" in request.form:
            saisie = request.form.get("Entre_texte")
            if saisie:
                message = ROT13(saisie)
                ajouter_historique("ROT13", saisie, message, date)
                return render_template('ROT13.html', resultat=message)

        elif "Entre_texte2" in request.form:
            saisie = request.form.get("Entre_texte2")
            if saisie:
                message = ROT13(saisie, "decryptage")
                ajouter_historique("ROT13", saisie, message, date)
                return render_template('ROT13.html', resultat2=message)

    return render_template('ROT13.html')


if __name__ == '__main__':
    app.run(debug=True)
