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
