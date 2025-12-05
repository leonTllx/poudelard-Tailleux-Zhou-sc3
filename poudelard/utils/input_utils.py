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

def demander_nombre