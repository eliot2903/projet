import string
import random
import sqlite3
import os
import datetime

def chiffre_de_vigenère(texte:str,cle:str,mode="cryptage"):
    """
    Cette fonction utilise le chiffre de vigenère pour crypter/décrypter une chaine de charactère.
    Pour fonctionner la fonction a besoin d'un texte et d'une clé toute les deux sous formes de chaines de caractères.
    Le chiffre de vigenère utilise les indices des lettres dans l'alphabet et décalle notre texte en fonction de la clé:
    Par exemple : texte="abc" ,cle="a" texte_final="bcd" tout le texte a été décallé de 1 car l'indice de "a" dans l'alphabet est 1.
    """
    if texte :
        if cle :
            alphabet_min=string.ascii_lowercase
            alphabet_maj=string.ascii_uppercase
            cle=cle.replace(" ","")
            for i in cle:
                if i not in alphabet_maj and i not in alphabet_min:
                    print("test")
                    return "la cle ne doit avoir que des lettres de l'alphabet"
            mot_crypté=""
            indice_a=None
            indice_b=None
            indice_cle=0
            for i in range(len(texte)):
                if texte[i] in alphabet_maj or texte[i] in alphabet_min:
                    est_maj=False
                    if texte[i] in alphabet_maj:
                        est_maj=True
                        indice_a=alphabet_maj.index(texte[i])
                    else:
                        indice_a=alphabet_min.index(texte[i])
                    if cle[indice_cle]in alphabet_maj:
                        indice_b=alphabet_maj.index(cle[indice_cle])
                    else:
                        indice_b=alphabet_min.index(cle[indice_cle])
                    indice_cle=(indice_cle+1)%len(cle)
                    if mode=="cryptage":
                        if est_maj:
                            mot_crypté+=alphabet_maj[(indice_a+indice_b)%26]
                        else:
                            mot_crypté+=alphabet_min[(indice_a+indice_b)%26]
                    else:
                        if est_maj:
                            mot_crypté+=alphabet_maj[(indice_a-indice_b)%26]
                        else:
                            mot_crypté+=alphabet_min[(indice_a-indice_b)%26]
                else:
                    mot_crypté+=texte[i]
            return mot_crypté
    return "veuiller écrire un texte"

def cryptage_en_hexa(mot,mode="cryptage"):
    """
    Cette fonction tranforme un texte en héxadécimal ou l'inverse
    """
    if mot:
        if mode=="cryptage":
            code=mot.encode('utf-8').hex()
        else:
            code=bytes.fromhex(mot).decode('utf-8')
        return code
    return "veuiller écrire un texte"


def Chiffre_de_Vernam(texte:str,cle:str=None,mode:str="cryptage"):
    """
    Cette algorithme marche comme le chiffre de vigenère mais il utilise une clé unique.
    On vérifie donc si la clé est bien unique grace au fichier cle.txt.
    Si la clé existe on en trouve une autre sinon on l'écrit dans le fichier
    """
    if texte :
        alphabet_min=string.ascii_lowercase
        alphabet_maj=string.ascii_uppercase
        if cle==None:
            texte_sans_espace=texte.replace(" ","")
            while True:
                cle = ""
                for i in range(len(texte_sans_espace)):
                    cle += alphabet_min[random.randint(0, 25)]
    
                if not cle_existe(cle):  
                    ajouter_cle(cle)
                    break
        code=chiffre_de_vigenère(texte,cle,mode)
        if mode=="cryptage":
            return code,cle
        else:
            return code
    return "veuiller écrire un texte"



def test_fonction ():
    assert chiffre_de_vigenère("j'aime la nsi","testeststetse")=="c'eafi dt flm"
    assert chiffre_de_vigenère("c'eafi dt flm","testeststetse","decrypte")=="j'aime la nsi"
    assert cryptage_en_hexa("bonjour")=="626f6e6a6f7572"
    assert cryptage_en_hexa("626f6e6a6f7572","décryptage")=="bonjour"
    assert Chiffre_de_Vernam('jfsejxi', 'irfvvdr',"décryptage")=="bonjour"
    assert Chiffre_de_Vernam("tmmmy uachx","mibbkymlwu","decrypter")=="hello world"
    assert chiffre_de_vigenère("","")=="veuiller écrire un texte"
    assert Chiffre_de_Vernam("")=="veuiller écrire un texte"
    assert cryptage_en_hexa("")=="veuiller écrire un texte"
    assert chiffre_de_vigenère("123","test")=="123"
test_fonction()

def chiffre_de_Trithémius(texte,mode="cryptage"):
    alphabet_min=string.ascii_lowercase
    alphabet_maj=string.ascii_uppercase
    indice=0
    indice_a=0
    texte_final=""
    for i in texte:
        if i in alphabet_maj:
            indice_a=alphabet_maj.index(i)
            if mode=="cryptage":
                texte_final+=alphabet_maj[(indice_a+indice)%26]
            else:
                texte_final+=alphabet_maj[(indice_a-indice)%26]
            indice+=1
        elif i in alphabet_min:
            indice_a=alphabet_min.index(i)
            if mode=="cryptage":
                texte_final+=alphabet_min[(indice_a+indice)%26]
            else:
                texte_final+=alphabet_min[(indice_a-indice)%26]
            indice+=1
        else:
            texte_final+=i
        if indice>=26:
            indice=0
    return texte_final

chemin = os.path.dirname(os.path.abspath(__file__))

def init_bd():
    conn = sqlite3.connect(os.path.join(chemin, 'cle.db'))
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cle TEXT NOT NULL,
        taille INTEGER NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

    conn = sqlite3.connect(os.path.join(chemin, 'historique.db'))
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS historique (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            methode TEXT NOT NULL,
            texte_original TEXT NOT NULL,
            resultat TEXT NOT NULL,
            date TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_bd()

def ajouter_cle(cle):
    conn = sqlite3.connect(os.path.join(chemin, 'cle.db'))
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO cles (cle, taille)
        VALUES (?, ?)
    ''', (cle, len(cle)))
    conn.commit()
    conn.close()

def cle_existe(cle):
    conn = sqlite3.connect(os.path.join(chemin, 'cle.db'))
    cursor = conn.cursor()
    cursor.execute('SELECT 1 FROM cles WHERE cle = ?', (cle,))
    resultat = cursor.fetchone()
    conn.close()
    return resultat is not None

def ajouter_historique(methode, original, resultat,date):
    conn = sqlite3.connect(os.path.join(chemin, 'historique.db'))
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO historique (methode, texte_original, resultat,date)
        VALUES (?, ?, ?,?)
    ''', (methode, original, resultat,date))
    conn.commit()
    conn.close()
