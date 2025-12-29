from poudelard.chapitres.chapitre_1 import lancer_chapitre_1
from poudelard.chapitres.chapitre_2 import lancer_chapitre_2
from poudelard.chapitres.chapitre_3 import lancer_chapitre_3
from poudelard.chapitres.chapitre_4 import lancer_chapitre4_quidditch

def main():
    personnage = lancer_chapitre_1()
    maisons = {"Gryffondor": 0, "Serpentard": 0, "Poufsouffle": 0, "Serdaigle": 0}
    print("personnage", personnage)
    personnage = lancer_chapitre_2(personnage)
    lancer_chapitre_3(personnage, maisons)
    lancer_chapitre4_quidditch(personnage, maisons)

if __name__ == "__main__":
    main()

#pour le commit