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

