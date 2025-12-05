def demander_texte(message):
    texte = input(message).strip()
    while texte == "":
        print("Erreur, la saisie ne peut pas être vide")
        texte = input(message).strip()
    return texte

def demander_nombre(val):
    val = int(input("Veuillez entrer un nombre entre 1 et 10"))
    while val < 1 or val > 10:
        print(f"Erreur, veuillez saisir une valeur entre 1 et 10.")
        val = int(input("Veuillez entrer un valeur comprise entre 1 et 10 : "))
    return val

