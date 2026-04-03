from flask import Flask, render_template, request
from cryptage import *
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    message = ""
    saisie = "" 
    cle = ""
    
    if request.method == 'POST':
        saisie = request.form.get("phrase")
        cle=request.form.get("clé")
        if saisie!=None and cle !=None:
            message = chiffre_de_vigenère(saisie,cle) 
        else:
            message="veuiller écrire un texte"

    return render_template('index.html', resultat=message, ancienne_phrase=saisie, ancienne_cle=cle)

@app.route('/decrypter' , methods=['GET', 'POST'])
def decrypter():
    message = ""
    saisie = "" 
    cle = ""
    
    if request.method == 'POST':
        saisie = request.form.get("phrase")
        cle=request.form.get("clé")
        if saisie!=None and cle!=None:
            message = chiffre_de_vigenère(saisie,cle,"décrypter") 
        else:
            message="veuiller écrire un texte"

    return render_template('decrypter.html', resultat=message, ancienne_phrase=saisie, ancienne_cle=cle)

@app.route('/Hexa' , methods=['GET', 'POST'])
def hexa():
    message = ""
    saisie = "" 
    cle = ""
    
    if request.method == 'POST':
        saisie = request.form.get("phrase")
        if saisie:
            message = cryptage_en_hexa(saisie) 
        else:
            message="veuiller écrire un texte"

    return render_template('Hexa.html', resultat=message, ancienne_phrase=saisie)

@app.route('/Hexa2' , methods=['GET', 'POST'])
def hexa2():
    message = ""
    saisie = "" 
    cle = ""
    
    if request.method == 'POST':
        saisie = request.form.get("phrase")
        if saisie:
            message = cryptage_en_hexa(saisie,"décrypter") 
        else:
            message="veuiller écrire un texte"

    return render_template('Hexa2.html', resultat=message, ancienne_phrase=saisie)

if __name__ == '__main__':
    app.run(debug=True)

