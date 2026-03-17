import string


def chiffre_de_vigenère(texte:str,cle:str):
    texte=str(texte)
    alphabet_min=string.ascii_lowercase
    alphabet_maj=string.ascii_uppercase
    cle.replace(" ","")
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
            if est_maj:
                mot_crypté+=alphabet_maj[(indice_a+indice_b)%26]
            else:
                mot_crypté+=alphabet_min[(indice_a+indice_b)%26]
        else:
            mot_crypté+=texte[i]
    return mot_crypté
