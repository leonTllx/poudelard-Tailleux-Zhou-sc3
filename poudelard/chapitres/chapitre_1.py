import os

from poudelard.univers import personnage
from poudelard.utils.input_utils import demander_choix, demander_texte, demander_nombre, load_fichier
from poudelard.univers.personnage import (initialisation_personnage, afficher_personnage, modifier_argent, ajouter_objet)

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.join(BASE_DIR, 'data')

def introduction():
    print("\n=== Chapitre 1 - L'arrivée dans le monde magique ===\n")
    print("Bienvenue ! Une grande aventure s'apprête à commencer...")
    input("Appuyez sur Entrée pour continuer...")

def creer_personnage():
    nom = demander_texte("Entrez le nom de votre personnage : ")
    prenom = demander_texte("Entrez le prenom de votre personnage : ")
    print("\n Choisissez vos attributs : ")
    courage = demander_nombre("Niveau de courage (1-10) : ", 1, 10)
    intelligence = demander_texte("Niveau d'intelligence (1-10) : ", 1, 10)
    loyaute = demander_nombre("Niveau de loyauté (1-10) : ", 1, 10)
    ambition = demander_nombre("Niveau d'ambition (1-10) : ", 1, 10)

    attributs = {
        "courage": courage,
        "intelligence": intelligence,
        "loyauté": loyaute,
        "ambition": ambition,
    }

    joueur = initialisation_personnage(nom, prenom, attributs)
    print("\n Profil du personnage initialisé : ")
    afficher_personnage(joueur)
    return joueur

def recevoir_lettre():
    print("\n Une chouette traverse la fenêtre et vous apporte une lettre scellée du sceau de Poudlard...")
    print("\n Cher élève, \n Nous avons le plaisir de vous informer que vous avez été admis à lécole de sorcellerie de Poudlard !\n")
    choix = demander_nombre("Souhaitez-vous accepter cette invitation et partir pour Poudlard ?\n" "1. Oui, bien sûr !\n" "2. Non, je préfère rester avec l'oncle Vernon...\n" "Votre choix : ", 1, 2)
    if choix == 2:
        print("\n Vous déchirez la lettre, l'oncle Vernon pousse un cri de joie :\n" "EXCELLENT ! Enfin quelqu'un de NORMAL dans cette maison !\n" "Le monde magique ne saura jamais que vous existiez... Fin du jeu.")
        exit(0)

def rencontrer_Hagrid(personnage):
    print("\n Hagrid : 'Salut ! Je sui venu t'aider à faire tes achats sur le Chemin de Traverse.'")
    choisir = demander_nombre("Voulez-vous suivre Hagrid ?\n1. Oui\n2. Non\nVotre choix : ", 1, 2)
    if choisir == 2:
        print("Hagrid insiste gentiment et vous entraîne quand même avec lui !")
    else:
        print("Vous suivez Hagrid vers le Chemin de Traverse.")

def acheter_fourniture(personnage):
    print("Bienvenue sur le chemin de Traverse !")
    donnees = load_fichier("poudelard/data/inventaire.json")
    items = []
    if isinstance(donnees, dict):
        for nom,prix in donnees.items():
            items.append((str(nom),int(prix)))
    elif isinstance(donnees, list):
        for elt in donnees:
            nom = str(elt.get("nom"))
            prix = int(elt.get("prix"))
            items.append((nom, prix))
    else :
        exit(1)

    items.sort(key=lambda x: x[0].lower())
    prix_par_nom = {nom: prix for (nom, prix) in items}
    noms_catalogue = [nom for (nom, _p) in items]
    obligatoires = ["Baguette magique", "Robe de sorcier", "Manuel de potions"]
    for nom_ob in obligatoires:
        if nom_ob not in prix_par_nom:
            print(f"L'objet obligatoire '{nom_ob}' est manquant dans le catalogue.")
            exit(1)
    obligatoires_restants = obligatoires[:]

    def afficher_catalogue():
        print("Catalogue des objets disponibles :")
        for i, (nom, prix) in enumerate(items, start=1):
            print(f"{i}. {nom} - {prix} galions")
    def recap_obligatoires():
        if obligatoires_restants:
            print("Objets obligatoires restants à acheter : " + ", ".join(obligatoires_restants))
        else :
            print("Tous les objets obligatoires ont été achetés ! \nIl est temps de choisir votre animal de compagnie pour Poudlard !")
    def reste_abordable():
        if not obligatoires_restants:
            return True
        cout_min = min(prix_par_nom[n] for n in obligatoires_restants)
        return personnage["Argent"] >= cout_min

    afficher_catalogue()
    print(f"Vous avez {personnage['Argent']} galions")
    recap_obligatoires()

    while obligatoires_restants:
        options = [f"{nom} - {prix_par_nom[nom]} galions" for nom in noms_catalogue]
        choix_label = demander_choix("Entrez le numéro de l'objet à acheter :", options)
        nom_choisi = choix_label.split(" - ")[0]
        prix = prix_par_nom[nom_choisi]

        if nom_choisi in personnage["Inventaire"] and nom_choisi in obligatoires:
            print(f"Vous avez déjà acheté : {nom_choisi}.")
            continue
        if personnage["Argent"] < prix:
            print("Vous n'avez pas assez d'argent pour cet achat...")
            exit(0)

    modifier_argent(personnage, -prix)
    ajouter_objet(personnage, "Inventaire", nom_choisi)
    print(f"Vous avez acheté : {nom_choisi} (-{prix} galions).")
    print(f"Vous avez {personnage['Argent']} galions.")
    if nom_choisi in obligatoires_restants:
        obligatoires_restants.remove(nom_choisi)
    if not reste_abordable():
        print("Il ne vous reste plus assez d'argent pour compléter les objets obligatoires...")
        exit(0)
    recap_obligatoires()

print(f"Vous avez {personnage['Argent']} galions. Voici les animaux disponibles :")
animaux = [("Chouette", 20), ("Chat", 15), ("Rat", 10), ("Crapaud", 5)]
labels_animaux = [f"{nom} - {prix} galions" for (nom, prix) in animaux]
choix_animal_label = demander_choix("Quel animal voulez-vous ?", labels_animaux)
nom_animal = choix_animal_label.split(" - ")[0]
prix_animal = dict(animaux)[nom_animal]

if personnage["Argent"] < prix_animal:
    print("Pas assez d'argent pour l'animal choisi...")
    exit(0)
modifier_argent(personnage, -prix_animal)
ajouter_objet(personnage, "Inventaire", nom_animal)
print(f"Vous avez choisi : {nom_animal} (-{prix_animal} galions).")

print("Voici votre inventaire final :")