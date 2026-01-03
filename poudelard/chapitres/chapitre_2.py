from poudelard.utils.input_utils import demander_choix, load_fichier
from poudelard.univers.personnage import afficher_personnage
from poudelard.univers.maison import repartition_maison

def rencontrer_amis(joueur):
    print("Vous montez à bord du Poudlard Express. Le train démarre vers le Nord...\n")
    print("Un garçon roux entre dans votre compartiment, l’air amical.")
    print("— Salut ! Moi c’est Ron Weasley. Tu veux bien qu’on s’assoie ensemble ?")
    choix_ron = demander_choix(
        "Que répondez-vous ?",
        ["Bien sûr, assieds-toi !", "Désolé, je préfère voyager seul."]
    )
    if choix_ron == "Bien sûr, assieds-toi !":
        joueur["Attributs"]["loyauté"] += 1
    else:
        joueur["Attributs"]["ambition"] += 1
    print("\nUne fille entre ensuite, portant déjà une pile de livres.")
    print("— Bonjour, je m’appelle Hermione Granger. Vous avez déjà lu ‘Histoire de la Magie’ ?")
    choix_hermione = demander_choix(
        "Que répondez-vous ?",
        ["Oui, j’adore apprendre !", "Non, je préfère l’aventure."]
    )
    if choix_hermione == "Oui, j’adore apprendre !":
        joueur["Attributs"]["intelligence"] += 1
    else:
        joueur["Attributs"]["courage"] += 1
    print("\nUn garçon blond entre avec un air arrogant.")
    print("— Je suis Drago Malefoy. Mieux vaut bien choisir ses amis dès le départ, tu ne crois pas ?")
    choix_drago = demander_choix(
        "Comment réagissez-vous ?",
        ["Je lui serre la main poliment.", "Je l’ignore.", "Je réponds avec arrogance."]
    )
    if choix_drago == "Je lui serre la main poliment.":
        joueur["Attributs"]["ambition"] += 1
    elif choix_drago == "Je l’ignore.":
        joueur["Attributs"]["loyauté"] += 1
    else:
        joueur["Attributs"]["courage"] += 1
    print("\nTes attributs mis à jour :", joueur["Attributs"])
    return joueur

def mot_de_bienvenue():
    print("\nLe train arrive à Poudlard. Dans la Grande Salle, le Professeur Dumbledore prend la parole...")
    print("« Bienvenue à Poudlard ! Que votre année soit riche en connaissances et en amitiés. »")
    input("Appuie sur Entrée pour continuer...")

def ceremonie_repartition(joueur):
    print("\nLa cérémonie de répartition commence dans la Grande Salle...")
    print("Le Choixpeau magique t’observe longuement avant de poser ses questions :\n")
    questions = [
        (
            "Tu vois un ami en danger. Que fais-tu ?",
            ["Je fonce l'aider", "Je réfléchis à un plan", "Je cherche de l’aide", "Je reste calme et j’observe"],
            ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
        ),
        (
            "Quel trait te décrit le mieux ?",
            ["Courageux et loyal", "Rusé et ambitieux", "Patient et travailleur", "Intelligent et curieux"],
            ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
        ),
        (
            "Face à un défi difficile, tu...",
            ["Fonces sans hésiter", "Cherches la meilleure stratégie", "Comptes sur tes amis", "Analyses le problème"],
            ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
        ),
    ]
    nom_maison = repartition_maison(joueur, questions)
    joueur["Maison"] = nom_maison
    print(f"\nLe Choixpeau s’exclame : {nom_maison} !!!")
    print(f"Tu rejoins les élèves de {nom_maison} sous les acclamations !")
    return joueur

def installation_salle_commune(joueur, chemin_fichier="poudelard/data/maisons.json"):
    data_maisons = load_fichier(chemin_fichier)
    maison = joueur["Maison"] if "Maison" in joueur else None
    info = {}
    if (type(data_maisons) is dict) and (maison in data_maisons):
        info = data_maisons[maison]
    print("\nVous suivez les préfets à travers les couloirs du château...")
    if (type(info) is dict) and ("description" in info):
        print(info["description"])
    else:
        print("Salle commune inconnue.")
    if (type(info) is dict) and ("bienvenue" in info):
        print(info["bienvenue"])
    if (type(info) is dict) and ("couleurs" in info):
        couleurs = info["couleurs"]
        if (type(couleurs) is list) and (len(couleurs) > 0):
            print("Les couleurs de votre maison :", ", ".join(couleurs))

def lancer_chapitre_2(joueur):
    joueur = rencontrer_amis(joueur)
    mot_de_bienvenue()
    joueur = ceremonie_repartition(joueur)
    installation_salle_commune(joueur)
    afficher_personnage(joueur)
    print("\nFin du Chapitre 2 — Les cours vont commencer...")
    return joueur