_NOM_MAISONS= ("Gryffondor","Serpentard","Poufsouffle","Serdaigle")
def actualiser_points_maison(maison, nom_maison, points):
    if nom_maison in maison:
        maison[nom_maison] += points
        print(f"{nom_maison} recoit {points} points. Total : {maison[nom_maison]}")
    else:
        print("Maison introuvable.")

def afficher_maison_gagnante(maison):
    if not maisons:
        print("Aucune maison")
        return
    max_score = None
    gagnantes = []
    for m, s in maisons.items():
        if max_score is None or s > max_score:
            max_score = s
            gagnantes = [m]
        elif s== max_score:
            gagnantes.append(m)
    if len(gagnantes) == 1:
        print(f"Maison en tête : {gagnantes[0]} avec {max_score} points")
    else:
        print(f"Maisons en ex aequo : {','.join(gagnantes)} avec {max_score} points")

def repartition_maison(joueur, questions):
    scores = {"Gryffondor": 0, "Serpentard": 0, "Poufsouffle": 0, "Serdaigle": 0}