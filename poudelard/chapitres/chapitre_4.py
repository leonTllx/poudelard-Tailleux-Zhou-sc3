import random
from poudelard.utils.input_utils import load_fichier
from poudelard.univers.maison import actualiser_points_maison

def creer_equipe(maison, equipe_dict, est_joueur=False, joueur=None):
    joueurs_source = list(equipe_dict.get("joueurs", []))
    equipe = {
        "nom": maison,
        "score": 0,
        "a_marque": 0,
        "a_stoppe": 0,
        "attrape_vifdor": False,
        "capitaine": equipe_dict.get("capitaine"),
        "joueurs": joueurs_source,
    }
    if est_joueur and joueur is not None:
        attrapeur = f"{joueur['Prenom']} {joueur['Nom']} (Attrapeur)"
        joueurs_sans_doublon = [j for j in joueurs_source if j != attrapeur]
        equipe["joueurs"] = [attrapeur] + joueurs_sans_doublon
    return equipe

def afficher_equipe(maison, equipe):
    print(f"Équipe de {maison} :")
    for nom in equipe["joueurs"]:
        print(f"- {nom}")

def tentative_marque(equipe_attaque, equipe_defense, joueur_est_joueur=False):
    proba = random.randint(1, 10)
    if proba >= 6:
        buteur = (equipe_attaque["joueurs"][0] if joueur_est_joueur
                  else random.choice(equipe_attaque["joueurs"]))
        equipe_attaque["score"] += 10
        equipe_attaque["a_marque"] += 1
        print(f"{buteur} marque un but pour {equipe_attaque['nom']} ! (+10 points)")
    else:
        equipe_defense["a_stoppe"] += 1
        print(f"{equipe_defense['nom']} bloque l’attaque !")

def apparition_vifdor():
    return random.randint(1, 6) == 6

def attraper_vifdor(e1, e2):
    gagnante = random.choice([e1, e2])
    gagnante["score"] += 150
    gagnante["attrape_vifdor"] = True
    return gagnante

def afficher_score(e1, e2):
    print("Score actuel :")
    print(f"→ {e1['nom']} : {e1['score']} points")
    print(f"→ {e2['nom']} : {e2['score']} points")

def match_quidditch(joueur, maisons):
    data = load_fichier("poudelard/data/equipes_quidditch.json")
    maison_joueur = joueur["Maison"]
    adversaires = [m for m in data.keys() if m != maison_joueur]
    maison_adverse = random.choice(adversaires)

    e1 = creer_equipe(maison_joueur, data[maison_joueur], est_joueur=True, joueur=joueur)
    e2 = creer_equipe(maison_adverse, data[maison_adverse], est_joueur=False, joueur=None)

    print(f"\nMatch de Quidditch : {e1['nom']} vs {e2['nom']} !")
    print()
    afficher_equipe(e1["nom"], e1)
    print()
    afficher_equipe(e2["nom"], e2)
    print()
    print(f"Tu joues pour {e1['nom']} en tant qu’Attrapeur")

    for tour in range(1, 21):
        print(f"\n━━━ Tour {tour} ━━━")
        print()
        tentative_marque(e1, e2, joueur_est_joueur=True)
        tentative_marque(e2, e1, joueur_est_joueur=False)
        print()
        afficher_score(e1, e2)

        if apparition_vifdor():
            gagnante_capture = attraper_vifdor(e1, e2)
            print(f"\nLe Vif d’Or a été attrapé par {gagnante_capture['nom']} ! (+150 points)")
            print("\nFin du match !")
            print()
            afficher_score(e1, e2)
            total_match = gagnante_capture["score"]
            print()
            print(f"Résultat final : Le Vif d’Or a été attrapé par {gagnante_capture['nom']} !")
            print(f"+150 points pour {gagnante_capture['nom']} ! Total : {total_match} points.")
            print(f"La maison gagnante est {gagnante_capture['nom']} avec {total_match} points !")
            print(f"{gagnante_capture['nom']} rempporte le match...")
            print(f"+500 points pour {gagnante_capture['nom']} ! Total : {total_match + 500} points.")
            print(f"La maison gagnante est {gagnante_capture['nom']} avec {total_match + 500} points !")
            return

        print("Appuyez sur Entrée pour continuer")
        input()
    print("Fin du match !")
    afficher_score(e1, e2)

    if e1["score"] > e2["score"]:
        vainqueur = e1
    elif e2["score"] > e1["score"]:
        vainqueur = e2
    else:
        vainqueur = None
    if vainqueur is None:
        print("Résultat final : Match nul !")
    else:
        print(f"Résultat final : {vainqueur['nom']} l’emporte !")
        total_match = vainqueur["score"]
        actualiser_points_maison(maisons, vainqueur["nom"], 500)
        print(f"+500 points pour {vainqueur['nom']} ! Total : {total_match + 500} points.")
        print(f"La maison gagnante est {vainqueur['nom']} avec {total_match + 500} points !")

def lancer_chapitre4_quidditch(joueur, maisons):
    print("\n=== Chapitre 4 — Épreuve de Quidditch ===")
    match_quidditch(joueur, maisons)
    print("Fin du Chapitre 4 — Quelle performance incroyable sur le terrain !")