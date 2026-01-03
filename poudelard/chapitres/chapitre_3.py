import random
from poudelard.utils.input_utils import load_fichier
from poudelard.univers.maison import actualiser_points_maison, afficher_maison_gagnante
from poudelard.univers.personnage import afficher_personnage

def apprendre_sorts(joueur, chemin_fichier="poudelard/data/sorts.json"):
    tous_les_sorts = load_fichier(chemin_fichier)
    quotas = {
        "Offensif": 1,
        "Défensif": 1,
        "Utilitaire": 3
    }
    sorts_appris = []
    while len(sorts_appris) < 5:
        sort = random.choice(tous_les_sorts)
        if ("type" not in sort) or ("nom" not in sort) or ("description" not in sort):
            continue
        type_sort = sort["type"]
        if type_sort in quotas:
            quota_restant = quotas[type_sort]
            if (quota_restant > 0) and (sort not in sorts_appris):
                sorts_appris.append(sort)
                quotas[type_sort] = quota_restant - 1
                print(f"Tu apprends : {sort['nom']} ({type_sort})")
                input("Appuie sur Entrée...")
    i = 0
    while i < len(sorts_appris):
        joueur["Sortilèges"].append(sorts_appris[i]["nom"])
        i += 1
    print("\n===== Sorts appris =====")
    i = 0
    while i < len(sorts_appris):
        s = sorts_appris[i]
        print(f"- {s['nom']} ({s['type']}) : {s['description']}")
        i += 1

def quiz_magie(joueur, chemin_fichier="poudelard/data/quiz_magie.json"):
    questions = load_fichier(chemin_fichier)
    questions_tirees = []
    while len(questions_tirees) < 4:
        q = random.choice(questions)
        if ("question" in q) and ("reponse" in q):
            deja = False
            i = 0
            while i < len(questions_tirees):
                if questions_tirees[i] == q:
                    deja = True
                    break
                i += 1
            if not deja:
                questions_tirees.append(q)
    score = 0
    print("\n=== Début du Quiz de Magie ===")
    i = 0
    while i < len(questions_tirees):
        q = questions_tirees[i]
        print(q["question"])
        reponse = input("> ")
        if reponse.strip().lower() == q["reponse"].lower():
            print("Bonne réponse ! +25 points")
            score += 25
        else:
            print("Mauvaise réponse. La bonne était :", q["reponse"])
        i += 1
    print(f"\nScore obtenu : {score} points")
    return score

def lancer_chapitre_3(personnage, maisons):
    print("\n===== CHAPITRE 3 — Les cours à Poudlard =====\n")
    apprendre_sorts(personnage)
    points = quiz_magie(personnage)
    nom_maison = personnage["Maison"]
    actualiser_points_maison(maisons, nom_maison, points)
    afficher_maison_gagnante(maisons)
    if nom_maison in maisons:
        personnage["scoreMaison"] = maisons[nom_maison]
    afficher_personnage(personnage)
    print("\nFin du Chapitre 3 !")
    return personnage