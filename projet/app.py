from flask import Flask, render_template, request
from test import test

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    message = ""
    saisie = "" # On crée une variable vide au début
    cle = ""
    
    if request.method == 'POST':
        # On récupère ce que l'utilisateur a tapé
        saisie = request.form.get('phrase')
        cle=request.form.get("clé")
        # On fait le traitement (ton programme)
        message = test() 
        
    # On renvoie les DEUX variables au HTML
    return render_template('index.html', resultat=message, ancienne_phrase=saisie, ancienne_cle=cle)

if __name__ == '__main__':
    app.run(debug=True)