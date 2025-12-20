from poudelard.utils.input_utils import *
from poudelard.univers.personnage import *


def introduction():
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("   Chapitre 1 — L’arrivée dans le monde magique")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("Bienvenue ! Une chouette tourne au-dessus de ta fenêtre...")
    input("Appuie sur Entrée pour commencer l’aventure.")

def creer_personnage():
    nom = demander_texte("Entrez le nom de votre personnage : ")
    prenom = demander_texte("Entrez le prénom de votre personnage : ")
    print("Choisissez vos attributs (entre 1 et 10) :")
    courage = demander_nombre("Niveau de courage (1-10) : ", 1, 10)
    intelligence = demander_nombre("Niveau d’intelligence (1-10) : ", 1, 10)
    loyaute = demander_nombre("Niveau de loyauté (1-10) : ", 1, 10)
    ambition = demander_nombre("Niveau d’ambition (1-10) : ", 1, 10)
    attributs = {
        "courage": courage,
        "intelligence": intelligence,
        "loyauté": loyaute,
        "ambition": ambition,
    }
    joueur = initialiser_personnage(nom, prenom, attributs)
    print("\nProfil du personnage :")
    afficher_personnage(joueur)
    return joueur

def recevoir_lettre():
    print("\nUne chouette traverse la fenêtre et dépose une lettre scellée...")
    print("« Cher élève,")
    print("Nous avons le plaisir de vous informer que vous avez été admis à l’école de sorcellerie de Poudlard ! »\n")
    choix = demander_choix(
        "Souhaitez-vous accepter cette invitation et partir pour Poudlard ?",
        ["Oui, bien sûr !", "Non, je préfère rester avec l’oncle Vernon..."]
    )
    if choix == 1 or choix == "1":
        choix = "Oui, bien sûr !"
    elif choix == 2 or choix == "2":
        choix = "Non, je préfère rester avec l’oncle Vernon..."
    if choix == "Non, je préfère rester avec l’oncle Vernon...":
        print("\nVous déchirez la lettre. L’oncle Vernon s’écrie :")
        print("« EXCELLENT ! Enfin quelqu’un de NORMAL dans cette maison ! »")
        print("Le monde magique ne saura jamais que vous existiez... Fin du jeu.")
        exit(0)
    print("\nParfait ! Fais tes bagages, l’aventure commence !")

def rencontrer_hagrid(joueur):
    print("\nUn géant frappe à la porte et entre d’un air bonhomme...")
    prenom = joueur.get("Prenom", "")
    print(f"Hagrid : « Salut {prenom} ! Je suis venu t’aider à faire tes achats sur le Chemin de Traverse. »")
    choix = demander_choix("Voulez-vous suivre Hagrid ?", ["Oui", "Non"])
    if choix == 1 or choix == "1":
        choix = "Oui"
    elif choix == 2 or choix == "2":
        choix = "Non"
    if choix == "Non":
        print("Hagrid insiste gentiment et t’entraîne quand même avec lui !")
    else:
        print("Tu suis Hagrid dans les rues animées du Chemin de Traverse.")

def acheter_fournitures(joueur, chemin_fichier="data/inventaire.json", noms_catalogue=None):
    print("\nBienvenue sur le Chemin de Traverse !")
    catalogue = load_fichier(chemin_fichier)
    items = []
    if isinstance(catalogue, dict):
        for _, val in catalogue.items():
            if isinstance(val, list) and len(val) == 2:
                nom, prix = val[0], val[1]
                items.append((nom, prix))
            elif isinstance(val, int):
                items.append((_, val))
    elif isinstance(catalogue, list):
        for obj in catalogue:
            nom = obj.get("nom")
            prix = obj.get("prix")
            if isinstance(nom, str) and isinstance(prix, int):
                items.append((nom, prix))
    items = sorted(items, key=lambda t: t[0].lower())
    noms = [nom_item for (nom_item, _p) in items]
    prix_par_nom = {nom_item: prix_item for (nom_item, prix_item) in items}
    obligatoires = ["Baguette magique", "Robe de sorcier", "Manuel de potions"]
    for ob in obligatoires:
        if ob not in prix_par_nom:
            print(f"Erreur : l’objet obligatoire « {ob} » est absent du catalogue.")
            exit(1)
    obligatoires_restants = obligatoires[:]

    def afficher_catalogue():
        print("Catalogue des objets disponibles :")
        for i, (nom_item, prix_item) in enumerate(items, start=1):
            print(f"{i}. {nom_item} - {prix_item} galions")

    def recap_obligatoires():
        if obligatoires_restants:
            print("Objets obligatoires restant à acheter : " + ", ".join(obligatoires_restants))
        else:
            print("Tous les objets obligatoires ont été achetés !")
            print("Il est temps de choisir votre animal de compagnie pour Poudlard !")

    def reste_abordable():
        if not obligatoires_restants:
            return True
        cout_min = min(prix_par_nom[nom_oblig] for nom_oblig in obligatoires_restants)
        return joueur["Argent"] >= cout_min
    print(f"\nVous avez {joueur['Argent']} galions.")
    afficher_catalogue()
    recap_obligatoires()

    while obligatoires_restants:
        choix = demander_choix("Entrez le numéro de l’objet à acheter :", [f"{nom}" for nom in noms])
        if isinstance(choix, int):
            if 1 <= choix <= len(noms):
                nom_choisi = noms[choix - 1]
            else:
                continue
        else:
            nom_choisi = choix
            if nom_choisi.isdigit():
                idx = int(nom_choisi)
                if 1 <= idx <= len(noms):
                    nom_choisi = noms[idx - 1]
        if nom_choisi not in prix_par_nom:
            print("Objet inconnu. Réessayez.")
            continue
        prix = prix_par_nom[nom_choisi]
        if nom_choisi in joueur["Inventaire"] and nom_choisi in obligatoires:
            print(f"Vous avez déjà acheté : {nom_choisi}.")
            continue
        if joueur["Argent"] < prix:
            print("Vous n’avez pas assez d’argent pour cet achat... Fin du jeu.")
            exit(0)
        modifier_argent(joueur, -prix)
        ajouter_objet(joueur, "Inventaire", nom_choisi)
        print(f"Vous avez acheté : {nom_choisi} (-{prix} galions).")
        print(f"Vous avez {joueur['Argent']} galions.")
        if nom_choisi in obligatoires_restants:
            obligatoires_restants.remove(nom_choisi)
        if not reste_abordable():
            print("Il ne vous reste plus assez d’argent pour compléter les objets obligatoires...")
            print("Le directeur vous renvoie chez les Dursley. Fin du jeu.")
            exit(0)
        recap_obligatoires()

    print(f"\nVous avez {joueur['Argent']} galions. Voici les animaux disponibles :")
    animaux = [("Chouette", 20), ("Chat", 15), ("Rat", 10), ("Crapaud", 5)]
    labels_animaux = [f"{nom} - {prix} galions" for (nom, prix) in animaux]
    choix_animal = demander_choix("Quel animal voulez-vous ?", labels_animaux)
    if isinstance(choix_animal, int):
        if 1 <= choix_animal <= len(animaux):
            nom_animal, prix_animal = animaux[choix_animal - 1]
        else:
            print("Choix invalide... Fin du jeu.")
            exit(0)
    else:
        texte = str(choix_animal)
        if " - " in texte:
            nom_animal = texte.split(" - ")[0].strip()
            prix_animal = dict(animaux).get(nom_animal)
            if prix_animal is None:
                print("Choix d’animal invalide... Fin du jeu.")
                exit(0)
        elif texte.isdigit():
            idx = int(texte)
            if 1 <= idx <= len(animaux):
                nom_animal, prix_animal = animaux[idx - 1]
            else:
                print("Choix d’animal invalide... Fin du jeu.")
                exit(0)
        else:
            prix_animal = dict(animaux).get(texte)
            if prix_animal is None:
                print("Choix d’animal invalide... Fin du jeu.")
                exit(0)
            nom_animal = texte
    if joueur["Argent"] < prix_animal:
        print("Pas assez d’argent pour l’animal choisi... Fin du jeu.")
        exit(0)

    modifier_argent(joueur, -prix_animal)
    ajouter_objet(joueur, "Inventaire", nom_animal)
    print(f"Vous avez choisi : {nom_animal} (-{prix_animal} galions).")
    print("\nVoici votre inventaire final :")
    afficher_personnage(joueur)

def lancer_chapitre_1():
    introduction()
    joueur = creer_personnage()
    recevoir_lettre()
    rencontrer_hagrid(joueur)
    acheter_fournitures(joueur)
    print("\nFin du Chapitre 1 ! Votre aventure commence à Poudlard...")
    return joueur