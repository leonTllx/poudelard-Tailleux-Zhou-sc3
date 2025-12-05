nom = input("Entrez le nom de votre personnage : ")
choix = int(input("Niveau de courage (1-10) : "))
if choix < 1 or choix > 10:
    while choix < 1 or choix > 10:
        int(input("Veuillez entrer un nombre entre 1 et 10. "))
print("Voulez-vous continuer ?")
print("1. Oui")
print("2. Non")
choix_continuer = input("Votre choix")

def demander_texte(message):
    texte = input(message).strip()
    while texte == "":
        print("Erreur, la saisie ne peut pas être vide")
        texte = input(message).strip()
    return texte

import json
def demander_texte(message):
    """Demander un texte non vide; répète tant que la saisie est vide."""
    while True:
        s = input(message).strip()
        if s:
            return s
        print("Veuillez saisir un texte non vide")

def is_int_string(s):
    """Retourne True si s représente un entier signé sans utiliser int()"""
    s = s.strip()
    if not s:
        return False

    if s[0] in '+-':
        s_digits = s[1:]
    else:
        s_digits = s
    if not s_digits:
        return False
    for c in s_digits:
        if c < '0' or c > '9':
            return False
    return True

def to_int(s):
    s =