from flask import Flask, render_template, request
from python.cryptage import *
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    message = ""
    saisie = "" 
    cle = ""
    if request.method == 'POST':
        saisie = request.form.get("Entre_texte")
        if saisie:
            message = Chiffre_de_Vernam(saisie) 
            return render_template('Chiffre_de_Vernam.html', resultat=message[1], resultat2=message[0],ancienne_cle2=cle,ancien_texte2=saisie)
        else:
            saisie = request.form.get("Entre_texte2")
            cle = request.form.get("Cle2")
            if saisie and cle:
                print(saisie,cle)
                message=Chiffre_de_Vernam(saisie,cle,"décryptage")
                print(message)
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
            print(message)
            return render_template('Cryptage_de_Vigenère.html', resultat=message,ancienne_cle=cle,ancien_texte=saisie)
        else:
            saisie = request.form.get("Entre_texte2")
            cle = request.form.get("Cle2")
            if saisie and cle:
                print(saisie,cle)
                message=chiffre_de_vigenère(saisie,cle,"décryptage")
                print(message)
                return render_template('Cryptage_de_Vigenère.html', resultat2=message,ancienne_cle2=cle,ancien_texte2=saisie)
    return render_template('Cryptage_de_Vigenère.html')

if __name__ == '__main__':
    app.run(debug=True)