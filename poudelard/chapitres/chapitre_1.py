import os
from poudelard.utils.input_utils import demander_texte, demander_nombre, load_fichier
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

def introduction():
    print("*********************************************************")
    print("         Bienvenue dans le monde de la magie !           ")
    print("*********************************************************\n")

    print("Vous êtes un jeune sorcier encore inconscient des merveilles qui vous attendent.")
    print("Les rues du monde moldu semblent normales, mais aujourd'hui, quelque chose d'extraordinaire va se produire")
    print("Une lettre au sceau de Poudlard arrive mystérieusement à votre porte, et votre destin est sur le point de changer\n")

    print("Préparez-vous à découvrir un univers où la magie est partout.")
    print("Votre aventure commence donc maintenant...\n")

    input("Appuyez sur Entrée pour continuer et débuter votre aventure...")

def creer_personnage():
    nom = input("Veuillez entrer le nom du personnage : ")
    prenom = input("Veuillez entrer le prénom du personnage : ")
    print(f"\nBienvenue, {prenom} {nom} ! Il est temps de choisir vos qualités.")
    print("Attribuez un niveau de 1 à 10 à chacune des qualités suivantes :\n")

    courage = demander_nombre("Niveau de courage (1-10) : ")
    intelligence = demander_nombre("Niveau d'intelligence (1-10) : ")
    loyaute = demander_nombre("Niveau de loyauté (1-10) : ")
    ambition = demander_nombre("Niveau d'ambition (1-10) : ")

    attributs = {
        "courage": courage,
        "intelligence": intelligence,
        "loyauté": loyaute,
        "ambition": ambition
    }

    personnage = {
        "nom": nom,
        "prenom": prenom,
        "argent": 100,
        "inventaire": [],
        "sortilèges": [],
        "attributs": attributs
    }

print("\n*********************************************************")
print("                    Profil du personnage                   ")
print("*********************************************************\n")
print(f"Nom : {personnage['Nom']}")
print(f"Prenom : {personnage['Prenom']}")
print(f"Argent : {personnage['Argent']}")
print(f"Inventaire : ", ", ".join(personnage{'inventaire'}) if personnage['inventaire'] else: "Aucun")
print(f"Sortilèges : ", ", ".join(personnage['sortileges']) if personnage['sortileges'] else: "Aucun")
print("Attributs :")
for attr, valeur in personnage['attributs'].items():
    print(f"-{attr} : {valeur}")
print("*********************************************************\n")
