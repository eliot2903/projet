from flask import Flask, render_template, request
from python.cryptage import *
import sqlite3
from datetime import *
import os 
import datetime



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
    return render_template("Description_vigenère.html")

@app.route('/desc_trithemius')
def desc_vigenere():
    return render_template("Description_Trithémius.html")

@app.route('/jeu')
def jeu():
    return render_template("Jeu.html")


@app.route('/vernam', methods=['GET', 'POST'])
def vernam():
    message = ""
    saisie = "" 
    cle = ""

    if request.method == 'POST':
        saisie = request.form.get("Entre_texte")

        if saisie:
            message = Chiffre_de_Vernam(saisie)
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ajouter_historique("Vernam", saisie, message[0],date) 
            return render_template('Chiffre_de_Vernam.html', resultat=message[1], resultat2=message[0])
        
        else:
            saisie = request.form.get("Entre_texte2")
            cle = request.form.get("Cle2")

            if saisie and cle:
                
                message=Chiffre_de_Vernam(saisie,cle,"décryptage")
                date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                ajouter_historique("Vernam", saisie, message,date)
                return render_template('Chiffre_de_Vernam.html', resultat3=message)
            
    return render_template('Chiffre_de_Vernam.html')

@app.route('/vigenere', methods=['GET', 'POST'])
def vigenere():
    message = ""
    saisie = "" 
    cle = ""

    if request.method == 'POST':
        saisie = request.form.get("Entre_texte")
        cle=request.form.get("Cle")

        if saisie and cle:
            message = chiffre_de_vigenère(saisie,cle)
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ajouter_historique("Vigenère", saisie, message,date) 
            return render_template('Chiffre_de_Vigenère.html', resultat=message,ancienne_cle=cle,ancien_texte=saisie)
        
        else:
            saisie = request.form.get("Entre_texte2")
            cle = request.form.get("Cle2")

            if saisie and cle:
                message=chiffre_de_vigenère(saisie,cle,"décryptage")
                date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                ajouter_historique("Vigenère", saisie, message,date)
                return render_template('Chiffre_de_Vigenère.html', resultat2=message,ancienne_cle2=cle,ancien_texte2=saisie)
            
    return render_template('Chiffre_de_Vigenère.html')

@app.route('/hexa', methods=['GET', 'POST'])
def hexa():
    saisie=""
    if request.method == 'POST':
        saisie=request.form.get("Entre_texte")

        if saisie:
            message=cryptage_en_hexa(saisie)
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ajouter_historique("Héxadécimal", saisie, message,date)
            return render_template('Hexadecimal.html',resultat2=message)
        
        else:
            saisie=request.form.get("Entre_texte2")
            message=cryptage_en_hexa(saisie,"decryptage")
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ajouter_historique("Héxadécimal", saisie, message,date)
            return render_template('Hexadecimal.html',resultat3=message)
        
    return render_template('Hexadecimal.html')

@app.route('/historique')
def historique():
    conn = sqlite3.connect(os.path.join(chemin, 'historique.db'))
    cursor = conn.cursor()
    cursor.execute('SELECT methode, texte_original, resultat, date FROM historique ORDER BY id DESC LIMIT 10')
    donnees = cursor.fetchall()
    print(donnees)
    conn.close()
    return render_template('historique.html', historique=donnees)

@app.route('/Trithémius', methods=['GET', 'POST'])
def trithemus():
    saisie=""
    if request.method == 'POST':
        saisie=request.form.get("Entre_texte")

        if saisie:
            message=chiffre_de_Trithémius(saisie)
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ajouter_historique("Trithémius", saisie, message,date)
            return render_template('Chiffre_de_Trithémius.html',resultat1=message)
        
        else:
            saisie=request.form.get("Entre_texte2")
            message=chiffre_de_Trithémius(saisie,"decryptage")
            date = datetime.datetime.now()
            ajouter_historique("Trithémius", saisie,message,date)
            return render_template('Chiffre_de_Trithémius.html',resultat2=message)
        
    return render_template('Chiffre_de_Trithémius.html')

if __name__ == '__main__':
    app.run(debug=True)