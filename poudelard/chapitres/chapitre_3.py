import random
from poudelard import *

def apprendre_sorts(joueur, chemin_fichier="poudelard/data/sorts.json"):
    tous_les_sorts = sorts.json(poudelard/data/sorts.json)
    quotas = {
        "Offensif": 1,
        "Défensif": 1,
        "Utilitaire": 3
    }

    sorts_appris = []

    while len(sorts_appris) < 5:
        sort = random.choice(tous_les_sorts)
        if quotas[sort["type"]] > 0 and sort not in sorts_appris:
            sorts_appris.append(sort)
            quotas[sort["type"]] -= 1
            print(f"Tu apprends : {sort['nom']} ({sort['type']})")
            input("Appuie sur Entrée...")

    for s in sorts_appris:
        joueur["Sortilèges"].append(s["nom"])

       print("\n===== Sorts appris =====")
    for s in sorts_appris:
