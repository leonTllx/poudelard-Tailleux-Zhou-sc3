def initialisation_personnage(nom: str,prenom: str, attributs: dict) -> dict:
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

def afficher_personnage(joueur: dict) -> None:
    print("Profil de personnage :")
    for cle in joueur:
        val = joueur[cle]