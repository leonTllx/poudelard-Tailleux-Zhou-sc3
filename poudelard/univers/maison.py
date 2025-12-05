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