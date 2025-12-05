import json
def demander_texte(message):
    while True:
        s = input(message).strip()
        if s:
            return s
        print("Veuillez saisir un texte non vide")

def is_int_string(s):
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
    """en gros  ca convertit une chaine en entier en utilisant ord(), supp si t'as compris"""
    s = s.strip()
    neg = False
    if s[0] == '-':
        neg = True
        s = s[1:]
    elif s[0] == '+':
        s = s[1:]
    val = 0
    for c in s:
        val = val * 10 + (ord(c) - ord('0'))
    return -val if neg else val

def demander_nombre(message, min_val=None, max_val=None):
    """La je demande un entier et je rajoute les bornes, supp si t'as compris"""
    while True:
        s = input(message)
        if not is_int_string(s):
            print("Veuillez entrer un nombre entier valide.")
            continue
        n = to_int(s)
        if min_val is not None and n < min_val:
            print(f"Veuillez entrer un nombre entre {min_val} et {max_val if max_val is not None else 'infinie'}.")
            continue
        if max_val is not None and n > max_val:
            print(f"Veuillez entrer un nombre entre {min_val if min_val is not None else '-infinie'} et {max_val}.")
            continue
        return n

def demander_choix(message, options):
    while True:
        print(message)
        for i, opt in enumerate(options, start=1):
            print(f"{i}. {opt}")
        choix = demander_nombre("Votre choix : ", 1, len(options))
        return options[choix - 1]

def load_fichier(chemin_fichier):
    with open(chemin_fichier, 'r', encoding='utf-8') as f:
        return json.load(f)