def initialiser_personnage(nom, prenom, attributs):
    joueur = {
        "Nom": nom,
        "Prenom": prenom,
        "Argent": 100,
        "Inventaire": [],
        "Sortilèges": [],
        "Attributs": dict(attributs),
        "Maison": None,
        "scoreMaison": 0
    }
    return joueur

def afficher_personnage(joueur):
    print("Profil du personnage :")
    for cle in joueur:
        val = joueur[cle]
        if type(val) is dict:
            print(f"{cle} :")
            for k in val:
                print(f"- {k} : {val[k]}")
        elif type(val) is list:
            elems_str = []
            i = 0
            while i < len(val):
                elems_str.append(str(val[i]))
                i += 1
            print(f"{cle} : {', '.join(elems_str)}")
        else:
            print(f"{cle} : {val}")

def modifier_argent(joueur, montant):
    joueur["Argent"] += montant

def ajouter_objet(joueur, cle, objet):
    if cle == "Inventaire" or cle == "Sortilèges":
        joueur[cle].append(objet)