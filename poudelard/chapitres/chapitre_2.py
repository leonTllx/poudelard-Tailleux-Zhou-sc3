from poudelard.univers.maison import repartition_maison


def rencontrer_amis(joueur):
    print("-Salut ! Moi c'est Ron Weasley. Tu veux qu'on s'assoie ensemble ?")
    print("Que répondez-vous ?")
    print(" 1. Bien sûr, assieds-toi !")
    print(" 2. Désolé, je préfère voyager seul.")
    choix_ron = input("Votre choix ? : ")
    while choix_ron != "1" and choix_ron != "2":
        choix_ron = input("Votre choix ? : ")
    if choix_ron == "1":
        print("Ron s'assoit avec vous. Vous discutez et riez ensemble. Votre loyauté augmente de 1.")
        joueur["attributs"]["loyaute"]+=1
    elif choix_ron == "2":
        print("Vous préférez rester seul. Votre ambition augmente de 1.")
        joueur["attributs"]["ambition"]+=1

    #RENCONTRE AVEC HERMIONE

    print("—Bonjour je m'appelle Hermione Granger. Vous avez déjà lu 'Histoire de la Magie' ?" )
    print("Que répondez-vous ?")
    print("1. Oui, j’adore apprendre de nouvelles choses !")
    print("2. Euh… non, je préfère les aventures aux bouquins.")
    choix_hermione = input("Votre choix ? : ")
    while choix_hermione != "1" and choix_hermione != "2":
        choix_hermione = input("Votre choix ? : ")
    if choix_hermione == "1":
        joueur["attributs"]["intelligence"]+=1
    elif choix_hermione == "2":
        joueur["attributs"]["courage"]+=1

    #RENCONTRE AVEC DRAGO MALEFOY

    print("—Je suis Drago Malefoy. Mieux vaut bien choisir ses amis dès le départ, tu ne crois pas ?")
    print("Comment réagissez-vous ?")
    print("1. Je lui serre la main poliment.")
    print("2. Je l’ignore complètement")
    print("3. Je lui réponds avec arrogance.")
    choix_drago = input("Votre choix ? : ")
    while choix_drago != "1" and choix_drago != "2" and choix_drago != "3":
        choix_drago = input("Votre choix ? : ")
    if choix_drago == "1":
        joueur["attributs"]["ambition"]+=1
    if choix_drago == "2":
        joueur["attributs"]["loyaute"]+=1
    if choix_drago == "3":
        joueur["attributs"]["courage"]+=1

    #FIN DE LA SCENE

    print("\nLe train continue sa route. Le château de Poudlard se profile à l'horizon..")
    print("\nTes choix semblent déjâ en dire long sur ta personnalité !")
    print("\nTes attributs sont mis à jour :", joueur["attributs"])

    return joueur

def mot_de_bienvenue():
    print("«Bienvenue à Pourdlard, jeunes sorciers et sorcières.")
    print("L'année qui s'annonce sera pleine de décourvertes, de défis, et surtout d'occasions de prouver qui vous êtes vraiment.» \n")
    print("-Professeur Albus Dumbledore\n")

    input("Appuyez sur Entrée pour continuer...")

def ceremonie_repartition(joueur):
    print("\nLa cérémonie de répartition commence dans la Grande Salle...")
    print("Le Choixpeau magique t'observe longuement avant de poser ses questions : ")
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
            ["Fonces sans hésiter", "Cherches la meilleure stratégie",
             "Comptes sur tes amis", "Analyses le problème"],
            ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
        )
    ]
    maison = repartition_maison(joueur, questions)
    joueur["Maison"] = maison

    print(f"Le Choixpeau Magique s'exclame : {maison} !!!")
    if maison == "Gryffondor":
        print("Tu rejoins les élèves de Gryffondor sous les acclamations !")
    elif maison == "Serpentard":
        print("Tu rejoins les élèves de Serpentard, certains te regardent avec curiosité...")
    elif maison == "Poufsouffle":
        print("Tu rejoins les élèves de Poufsouffle qui t'accueillent chaleureusement !")
    elif maison == "Serdaigle":
        print("Tu rejoins les élèves de Serdaigle qui t'adressent un signe de bienvenue !")

    return joueur

import os
import json

def installation_salle_commune(joueur):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    fichier_maisons = os.path.join(base_dir, 'maisons.json')

    try:
        with open(fichier_maisons, 'r', encoding="utf-8") as f:
            maisons_data= json.load(f)
    except FileNotFoundError:
        print("Erreur : le fichier maisons.json est introuvable.")
        return
    except json.JSONDecodeError:
        print("Erreur : le fichier json contient des erreurs")
        return

    maison_joueur = joueur.get("Maison")
    if maison_joueur not in maisons_data:
        print(f"Erreur : la maison '{maison_joueur}' n'existe pas")
        return
    info_maison = maisons_data[maison_joueur]
    description = info_maison.get("description","Aucune description disponible")
    accueil = info_maison.get("accueil","")
    couleurs = info_maison.get("couleurs",[])


    print("\nVous suivez les préfets à travers les couloirs du chateau...")
    print(f"{info_maison.get('emoji', '')}{info_maison.get('description', 'Aucune description disponible')}")
    print(f"{info_maison.get('message_installation', '')}")
    couleurs = info_maison.get("couleurs",[])
    if couleurs:
        print("Les couleurs de votre maison : ",",".join(couleurs))

    bonus = info_maison.get("bonus_attributs",{})
    for attr, valeur in bonus.items():
        if attr in joueur["attributs"]:
            joueur["attributs"][attr] += valeur
        else:
            joueur["attributs"][attr] = valeur
    print("\nVos attributs ont été mis à jour avec les bonus de la maison :", joueur["attributs"])
    input("Appuyez sur Entrée pour continuer...")

def lancer_chapitre_2(personnage):
    return rencontrer_amis(personnage), mot_de_bienvenue(), ceremonie_repartition(personnage), installation_salle_commune(personnage)
