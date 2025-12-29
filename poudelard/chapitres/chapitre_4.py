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

