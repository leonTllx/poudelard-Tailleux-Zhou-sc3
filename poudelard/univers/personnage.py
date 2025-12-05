def initialisation_personnage(nom ,prenom ,attributs):
    joueur = {
        "Nom":nom,
        "Prenom":prenom,
        "Argent":100,
        "Inventaires":[],
        "Sortilèges":[],
        "Attributs":dict(attributs),
        "Maison":None,
        "scoreMaison":0
    }
    return joueur

def afficher_personnage(joueur):
    print("Profil de personnage :")
    for cle in joueur:
        val = joueur[cle]