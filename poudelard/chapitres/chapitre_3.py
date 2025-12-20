import random
from poudelard.chapitres.chapitre_2 import *
from poudelard.univers.maison import *

def apprendre_sorts(joueur, chemin_fichier="data/sorts.json"):
    tous_les_sorts = load_fichier(chemin_fichier)

    quotas = {
        "Offensif": 1,
        "Défensif": 1,
        "Utilitaire": 3
    }
    sorts_appris = []

    while len(sorts_appris) < 5:
        sort = random.choice(tous_les_sorts)
        if quotas.get(sort["type"], 0) > 0 and sort not in sorts_appris:
            sorts_appris.append(sort)
            quotas[sort["type"]] -= 1
            print(f"Tu apprends : {sort['nom']} ({sort['type']})")
            input("Appuie sur Entrée...")
    for s in sorts_appris:
        joueur["Sortilèges"].append(s["nom"])
    print("\n===== Sorts appris =====")
    for s in sorts_appris:
        print(f"- {s['nom']} ({s['type']}) : {s['description']}")

def quiz_magie(joueur, chemin_fichier="data/quiz_magie.json"):
    questions = load_fichier(chemin_fichier)
    questions_tirees = []
    while len(questions_tirees) < 4:
        q = random.choice(questions)
        if q not in questions_tirees:
            questions_tirees.append(q)
    score = 0
    print("\n=== Début du Quiz de Magie ===")
    for q in questions_tirees:
        print(q["question"])
        reponse = input("> ")
        if reponse.strip().lower() == q["reponse"].lower():
            print("Bonne réponse ! +25 points")
            score += 25
        else:
            print("Mauvaise réponse. La bonne était :", q["reponse"])
    print(f"\nScore obtenu : {score} points")
    return score

def lancer_chapitre_3(personnage, maisons):
    print("\n===== CHAPITRE 3 — Les cours à Poudlard =====\n")
    apprendre_sorts(personnage)
    points = quiz_magie(personnage)
    nom_maison = personnage["Maison"]
    actualiser_points_maison(maisons, nom_maison, points)
    afficher_maison_gagnante(maisons)
    personnage["scoreMaison"] = maisons[nom_maison]
    afficher_personnage(personnage)
    print("\nFin du Chapitre 3 !")
    return