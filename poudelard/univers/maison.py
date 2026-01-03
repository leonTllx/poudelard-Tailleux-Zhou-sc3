def actualiser_points_maison(maisons, nom_maison, points):
    if nom_maison in maisons:
        maisons[nom_maison] += points
        print(f"{nom_maison} recoit {points} points. Total : {maisons[nom_maison]}")
    else:
        print("Maison introuvable.")

def afficher_maison_gagnante(maisons):
    if not maisons:
        print("Aucune maison")
        return
    max_score = None
    gagnantes = []
    for m in maisons:
        s = maisons[m]
        if (max_score is None) or (s > max_score):
            max_score = s
            gagnantes = [m]
        elif s == max_score:
            gagnantes.append(m)
    if len(gagnantes) == 1:
        print(f"Maison en tête : {gagnantes[0]} avec {max_score} points")
    else:
        print(f"Maisons en ex aequo : {', '.join(gagnantes)} avec {max_score} points")


def repartition_maison(joueur, questions):
    scores = {"Gryffondor": 0, "Serpentard": 0, "Poufsouffle": 0, "Serdaigle": 0}
    attr = joueur.get("Attributs", {})
    courage = attr.get("courage", 0)
    ambition = attr.get("ambition", 0)
    loyaute = attr.get("loyauté", 0)
    intelligence = attr.get("intelligence", 0)
    scores["Gryffondor"] += courage * 2
    scores["Serpentard"] += ambition * 2
    scores["Poufsouffle"] += loyaute * 2
    scores["Serdaigle"] += intelligence * 2

    from poudelard.utils.input_utils import demander_choix

    for question in questions:
        texte, options, maisons_assoc = question
        choix = demander_choix(texte, options)
        i = 0
        while i < len(options):
            if options[i] == choix:
                break
            i += 1
        if i >= len(options):
            print("Choix invalide, aucun score ajouté.")
        else:
            maison = maisons_assoc[i]
            scores[maison] += 3
    print("Résumé des scores :")
    for m in scores:
        print(f"{m} : {scores[m]} points")

    maison_finale = None
    max_score = None
    for m in scores:
        s = scores[m]
        if (max_score is None) or (s > max_score):
            max_score = s
            maison_finale = m
    return maison_finale