import sys
from poudelard.utils.input_utils import demander_nombre
from poudelard.chapitres.chapitre_1 import lancer_chapitre_1
from poudelard.chapitres.chapitre_2 import lancer_chapitre_2
from poudelard.chapitres.chapitre_3 import lancer_chapitre_3
from poudelard.chapitres.chapitre_4 import lancer_chapitre4_quidditch

def afficher_menu_principal():
    print("\n=== Menu principal ===")
    print("1. Lancer l’aventure")
    print("2. Quitter")

def lancer_choix_menu():
    maisons = {"Gryffondor": 0, "Serpentard": 0, "Poufsouffle": 0, "Serdaigle": 0}
    while True:
        afficher_menu_principal()
        choix = demander_nombre("Votre choix : ", 1, 2)
        if choix == 2:
            print("Au revoir !")
            sys.exit(0)
        personnage = lancer_chapitre_1()
        personnage = lancer_chapitre_2(personnage)
        personnage = lancer_chapitre_3(personnage, maisons)
        lancer_chapitre4_quidditch(personnage, maisons)
        print("\nPartie terminée. Voulez-vous rejouer ?")
        print("1. Oui")
        print("2. Non (retour menu)")
        rejouer = demander_nombre("Votre choix : ", 1, 2)
        if rejouer == 2:
            pass
