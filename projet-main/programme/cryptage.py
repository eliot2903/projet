import string
import sqlite3
import os
import secrets 

def chiffre_de_vigenère(texte:str,cle:str,mode : str ="cryptage"):
    """
    Cette fonction utilise le chiffre de vigenère pour crypter/décrypter une chaine de charactère.
    Pour fonctionner la fonction a besoin d'un texte et d'une clé toute les deux sous formes de chaines de caractères.
    Le chiffre de vigenère utilise les indices des lettres dans l'alphabet et décalle notre texte en fonction de la clé:
    Par exemple : texte="abc" ,cle="a" texte_final="abc"car l'indice de "a" dans l'alphabet est 0.
    Pareil avec : texte="abc" , cle=b texte_final="bcd" car l'indice de "b" dans l'alphabet est 1.
    """
    if texte :
        if cle :
            alphabet_min=string.ascii_lowercase
            alphabet_maj=string.ascii_uppercase
            cle=cle.replace(" ","")
            if not cle:
                return None
            for i in cle:
                if i not in alphabet_maj and i not in alphabet_min:
                    return None
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
    return texte

def cryptage_en_hexa(mot : str ,mode : str ="cryptage"):
    """
    Cette fonction tranforme un texte en héxadécimal ou l'inverse
    """
    if mot:
        if mode=="cryptage":
            code=mot.encode('utf-8').hex()
        else:
            mot_hex = mot.replace(" ", "").replace("-", "")
            code = bytes.fromhex(mot_hex).decode('utf-8')
        return code
    return mot


def Chiffre_de_Vernam(texte:str,cle:str=None,mode:str="cryptage"):
    """
    Cette algorithme marche comme le chiffre de vigenère mais il utilise une clé unique.
    On vérifie donc si la clé est bien unique grace a la base de données cle.
    Si la clé existe on en trouve une autre sinon on l'écrit dans le fichier
    """
    if texte :
        texte_sans_espace=texte.replace(" ","")
        if not texte_sans_espace:
            if mode=="cryptage":
                return texte, ""
            else:
                return texte
        alphabet=string.ascii_lowercase+string.ascii_uppercase
        if cle==None:
            max_tentatives = 10
            for _ in range(max_tentatives):
                cle = ""
                for _ in range(len(texte)):
                    cle += secrets.choice(alphabet)
                if not cle_existe(cle):
                    ajouter_cle(cle)
                    break
            else:
                return None
        code=chiffre_de_vigenère(texte,cle,mode)
        if code is None:
            return None
        elif mode=="cryptage":
            return code,cle
        else:
            return code
    return texte





def chiffre_de_Trithémius(texte : str ,mode : str ="cryptage"):
    """
    cette fonction utilise le chiffre de trithémius pour cypter/décrypter un texte. cette algorithme est similaire au chiffre de vigenere mais ne nécéssite pas de clé.
    chaque lettre du texte est décaler par son indice dans la phrase 
    Ex: mot = mpv car m+a=m o+b=p et t+c=v
    """
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
    return texte_final

def chiffre_de_cesar(texte : str,numero : int ,mode : str ="cryptage"):
    """
    Cette fonction utilise le chiffre de césar pour crypter un message
    """
    texte_final=""
    alphabet_min=string.ascii_lowercase
    alphabet_maj=string.ascii_uppercase
    for i in texte:
        if i in alphabet_maj:
            indice=alphabet_maj.index(i)
            if mode=="cryptage" :
                texte_final+=alphabet_maj[(indice+numero)%26]
            else:
                texte_final+=alphabet_maj[(indice-numero)%26]
        elif i in alphabet_min:
            indice=alphabet_min.index(i)
            if mode=="cryptage":
                texte_final+=alphabet_min[(indice+numero)%26]
            else:
                texte_final+=alphabet_min[(indice-numero)%26]
        else:
            texte_final+=i
    return texte_final

def ROT13(texte : str,mode : str="cryptage"):
    """
    Cette fonction utilise ROT13 pour crypter un message (Chiffre de césar mais décale tout de 13)
    """
    return chiffre_de_cesar(texte,13,mode)


chemin = os.path.dirname(os.path.abspath(__file__))

def init_bd():
    """
    Cette fonction initialiste les bases de données cle.db et historique.db
    """
    conn = sqlite3.connect(os.path.join(chemin, 'cle.db'))
    try:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS cles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cle TEXT NOT NULL,
            taille INTEGER NOT NULL
        )
        ''')
        conn.commit()
    finally:
        conn.close()

    conn = sqlite3.connect(os.path.join(chemin, 'historique.db'))
    try:
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
    finally:
        conn.close()

init_bd()

def ajouter_cle(cle : str):
    """
    Cette fonction rajoute une cle et sa taille dans la base de donnée cle.db
    """
    conn = sqlite3.connect(os.path.join(chemin, 'cle.db'))
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO cles (cle, taille)
            VALUES (?, ?)
        ''', (cle, len(cle)))
        conn.commit()
    finally:
        conn.close()

def cle_existe(cle : str):
    """
    Cette fonction vérifie si une clé est déja enregistré dans la base de donnée
    """
    conn = sqlite3.connect(os.path.join(chemin, 'cle.db'))
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT 1 FROM cles WHERE cle = ?', (cle,))
        resultat = cursor.fetchone()
        return resultat is not None
    finally:
        conn.close()

def ajouter_historique(methode : str , original : str, resultat : str ,date : str):
    """
    Cette fonction permet de sauvegarder l'historique des algorithmes utilisé et leur résultat dans la base de donnée historique.db
    """
    conn = sqlite3.connect(os.path.join(chemin, 'historique.db'))
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO historique (methode, texte_original, resultat,date)
            VALUES (?, ?, ?,?)
        ''', (methode, original, resultat,date))
        conn.commit()
    finally:
        conn.close()

def supprimer_historique():
    """
    Cette fonction permet de suprimer l'historique dans la base de donné historique.db
    """
    conn = sqlite3.connect(os.path.join(chemin, 'historique.db'))
    try:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM historique')
        conn.commit()
    finally:
        conn.close()