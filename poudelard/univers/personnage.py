def initialisation_personnage(nom, prenom, attributs):
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
        if isinstance(val, dict):
            print(f"{cle} : ")
            for k in val:
                print(f"- {k} : {val[k]}")
        elif isinstance(val, list):
            print(f"{cle} : {'.'.join(str(x) for x in val)}")
        else:
            print(f"{cle} : {val}")

def modifier_argent(joueur, montant):
    joueur["Argent"] += montant

def ajouter_objet(joueur, cle, objet):
    if cle not in ("Inventaire", "Sortilèges"):
        return
    joueur[cle].append(objet)