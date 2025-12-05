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

def demander_nombre():
    min_val = 1
    max_val = 10
    val = int(input("Veuillez entrer un nombre entre 1 et 10"))
    while val < min_val or val > max_val:
        print(f"Erreur, veuillez saisir une valeur entre {min_val} et {max_val}.")
        val = int(input("Veuillez entrer un nombre"))
    return val

