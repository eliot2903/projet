from flask import Flask, render_template, request
from test import test

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    message = ""
    saisie = "" 
    cle = ""
    
    if request.method == 'POST':
        
        saisie = request.form.get('phrase')
        cle=request.form.get("clé")
        
        message = test() 
        
   
    return render_template('index.html', resultat=message, ancienne_phrase=saisie, ancienne_cle=cle)

if __name__ == '__main__':
    app.run(debug=True)
