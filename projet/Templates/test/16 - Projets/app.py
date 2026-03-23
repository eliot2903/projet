from flask import Flask, render_template, request
from cryptage import chiffre_de_vigenère
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
        print(saisie,cle)
        print(message)
    return render_template('index.html', resultat=message, ancienne_phrase=saisie, ancienne_cle=cle)

@app.route('/decrypter' , methods=['GET', 'POST'])
def decrypter():
    message = ""
    saisie = "" 
    cle = ""
    
    if request.method == 'POST':
        saisie = request.form.get("phrase2")
        cle=request.form.get("clé2")
        if saisie!=None and cle!=None:
            message = chiffre_de_vigenère(saisie,cle,"décrypter") 
        else:
            message="veuiller écrire un texte"
        print(saisie,cle)
        print(message)
    return render_template('decrypter.html', resultat=message, ancienne_phrase=saisie, ancienne_cle=cle)

if __name__ == '__main__':
    app.run(debug=True)