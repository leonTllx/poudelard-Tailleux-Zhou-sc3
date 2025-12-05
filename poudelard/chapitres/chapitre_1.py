from poudelard.univers import personnage
from poudelard.utils.input_utils import demander_texte, demander_nombre

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
    loyauté = demander_nombre("Niveau de loyauté (1-10) : ")
    ambition = demander_nombre("Niveau d'ambition (1-10) : ")

    attributs = {
        "courage": courage,
        "intelligence": intelligence,
        "loyauté": loyauté,
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
print(f"Nom : {personnage['nom']}")
print(f"Prenom : {personnage['prenom']}")
print(f"Argent : {personnage['argent']}")
print(f"Inventaire : ", ", ".join(personnage['inventaire']) if personnage['inventaire'] else "Aucun")
print(f"Sortilèges : ", ", ".join(personnage['sortileges']) if personnage['sortileges'] else "Aucun")
print("Attributs :")
for attr, valeur in personnage['attributs'].items():
    print(f"-{attr} : {valeur}")
print("*********************************************************\n")
