import random
from poudelard.utils.input_utils import load_fichier
from pourdelard.univers.maison import *
from poudelard.univers.personnage import afficher_personnage

def creer_equipe(maison, equipe_data, est_joueur=False, joueur=None):
    equipe = {
        "nom": maison,
        "score": 0,
        "a_marque": 0,
        "a_stoppe": 0,
        "attrape_vifdor": False,
        "joueurs": list(equipe_data)
    }
    if est_joueur and joueur is not None:
        nom_prenom = f"{joueur.get('Prenom', '')}{joueur.get('Nom', '')}".strip()
        joueur_principal = f"{nom_prenom}(Attrapeur)"
        nouvelle_liste = [joueur_principal]
        for j in equipe_data:
            if nom_prenom not in j:
                nouvelle_liste.append(j)
        equipe["joueurs"] = nouvelle_liste
    return equipe

def tentative_marque(equipe_attaque, equipe_defense, joueur_est_joueur=False):
    proba_but = random.randint(1, 10)
    if proba_but >= 6:
        if joueur_est_joueur:
            buteur = equipe_attaque["joueurs"][0]
        else:
            buteur = random.choice(equipe_attaque["joueurs"])
        equipe_attaque["score"] += 10
        equipe_attaque["a_marque"] += 1
        print(f"{buteur} marque un but pour {equipe_attaque['nom']} ! (+10 points)")
    else:
        equipe_defense["a_stoppe"] += 1
        print(f"{equipe_defense['nom']} bloque l'attaque !")

def apparition_vifdor():
    return random.randint(1,6) == 6

def attraper_vifdor(e1, e2):
    gagnant = random.choice([e1, e2])
    gagnant["score"] += 150
    gagnant["attrape_vifdor"] = True
    print(f"Le Vif d'Or a été attrapé par {gagnant['nom']} ! (+150 points)")
    return gagnant

def afficher_score(e1, e2):
    print("Score actuel :")
    print(f"→ {e1['nom']} : {e1['score']} points")
    print(f"→ {e2['nom']} : {e2['score']} points")

def afficher_equipe(maison, equipe):
    print(f"Équipe de {maison} :")
    for j in equipe["joueurs"]:
        print(f"- {j}")

def match_quidditch(joueur, maisons, chemin_fichier="data/equipes_quidditch.json"):
    data_equipes = load_fichier(chemin_fichier)

    maison_joueur = joueur.get("Maison")
    toutes_maisons = list(data_equipes.keys())
    adversaires = [m for m in toutes_maisons if m != maison_joueur]
    maison_adverse = random.choice(adversaires)

    equipe_joueur = creer_equipe(maison_joueur, data_equipes[maison_joueur], est_joueur=True, joueur=joueur)
    equipe_adv = creer_equipe(maison_adverse, data_equipes[maison_adverse], est_joueur=False, joueur=None)

    print(f"Match de Quidditch : {maison_joueur} vs {maison_adverse} !")
    afficher_equipe(maison_joueur, equipe_joueur)
    afficher_equipe(maison_adverse, equipe_adv)
    print(f"Tu joues pour {maison_joueur} en tant qu’Attrapeur")

    for tour in range(1, 21):
        print(f"\n━━━ Tour {tour} ━━━")
        tentative_marque(equipe_adv, equipe_joueur, joueur_est_joueur=False)
        tentative_marque(equipe_joueur, equipe_adv, joueur_est_joueur=True)
        afficher_score(equipe_joueur, equipe_adv)
        if apparition_vifdor():
            equipe_victorieuse = attraper_vifdor(equipe_joueur, equipe_adv)
            print("Fin du match !")
            afficher_score(equipe_joueur, equipe_adv)
            actualiser_points_maison(maisons, equipe_victorieuse["nom"], 500)
            print(f"+500 points pour {equipe_victorieuse['nom']} ! Total : {maisons[equipe_victorieuse['nom']]}")
            return equipe_victorieuse["nom"]
        input("Appuyez sur Entrée pour continuer")

    print("\nFin du match !")
    afficher_score(equipe_joueur, equipe_adv)
    if equipe_joueur["score"] > equipe_adv["score"]:
        maison_gagnante = equipe_joueur["nom"]
        print(f"Résultat final : {maison_gagnante} gagne au score !")
    elif equipe_joueur["score"] < equipe_adv["score"]:
        maison_gagnante = equipe_adv["nom"]
        print(f"Résultat final : {maison_gagnante} gagne au score !")
    else:
        maison_gagnante = None
        print("Résultat final : Match nul !")

    if maison_gagnante is not None:
        actualiser_points_maison(maisons, maison_gagnante, 500)
        print(f"+500 points pour {maison_gagnante} ! Total : {maisons[maison_gagnante]}")
    return maison_gagnante

def lancer_chapitre4_quidditch(joueur, maisons):
    print("\n===== CHAPITRE 4 — Épreuve de Quidditch =====\n")
    gagnante = match_quidditch(joueur, maisons, chemin_fichier="data/equipes_quidditch.json")
    print("\nFin du Chapitre 4 — Quelle performance incroyable sur le terrain !")
    afficher_maison_gagnante(maisons)
    afficher_personnage(joueur)
