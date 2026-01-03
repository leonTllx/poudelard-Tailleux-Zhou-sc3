import sys
from poudelard.utils.input_utils import demander_texte, demander_nombre, demander_choix, load_fichier
from poudelard.univers.personnage import initialiser_personnage, afficher_personnage, modifier_argent, ajouter_objet

def introduction():
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("   Chapitre 1 — L’arrivée dans le monde magique")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("\nBienvenue ! Une chouette tourne au-dessus de ta fenêtre...")
    input("Appuie sur Entrée pour commencer l’aventure.")

def creer_personnage():
    nom = demander_texte("\nEntrez le nom de votre personnage : ")
    prenom = demander_texte("Entrez le prénom de votre personnage : ")
    print("\nChoisissez vos attributs (entre 1 et 10) :")
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
    print()
    joueur = initialiser_personnage(nom, prenom, attributs)
    afficher_personnage(joueur)
    return joueur

def recevoir_lettre():
    print("\nUne chouette traverse la fenêtre et dépose une lettre scellée du sceau de Poudlard...")
    print("« Cher élève,")
    print("Nous avons le plaisir de vous informer que vous avez été admis à l’école de sorcellerie de Poudlard ! »\n")
    choix = demander_choix(
        "Souhaitez-vous accepter cette invitation et partir pour Poudlard ?",
        ["Oui, bien sûr !", "Non, je préfère rester avec l’oncle Vernon..."]
    )
    if choix == "Non, je préfère rester avec l’oncle Vernon...":
        print("\nVous déchirez la lettre. L’oncle Vernon s’écrie :")
        print("« EXCELLENT ! Enfin quelqu’un de NORMAL dans cette maison ! »")
        print("Le monde magique ne saura jamais que vous existiez... Fin du jeu.")
        return False  # Propager l'abandon vers le lanceur
    print("\nParfait ! Fais tes bagages, l’aventure commence !")
    return True

def rencontrer_hagrid(joueur):
    print("\nUn géant frappe à la porte et entre d’un air bonhomme...")
    prenom = joueur.get("Prenom", "")
    print(f"Hagrid : « Salut {prenom} ! Je suis venu t’aider à faire tes achats sur le Chemin de Traverse. »")
    choix = demander_choix("Voulez-vous suivre Hagrid ?", ["Oui", "Non"])
    if choix == "Non":
        print("Hagrid insiste gentiment et t’entraîne quand même avec lui !")
    else:
        print("Tu suis Hagrid dans les rues animées du Chemin de Traverse.")

def acheter_fournitures(joueur, chemin_fichier="poudelard/data/inventaire.json"):
    print("\nBienvenue sur le Chemin de Traverse !")
    catalogue = load_fichier(chemin_fichier)
    items = []
    if type(catalogue) is dict:
        for k in catalogue:
            val = catalogue[k]
            if (type(val) is list) and (len(val) == 2):
                nom_item = val[0]
                prix_item = val[1]
                items.append((nom_item, prix_item))
            elif type(val) is int:
                items.append((k, val))
    elif type(catalogue) is list:
        i = 0
        while i < len(catalogue):
            obj = catalogue[i]
            nom_item = obj.get("nom")
            prix_item = obj.get("prix")
            if (type(nom_item) is str) and (type(prix_item) is int):
                items.append((nom_item, prix_item))
            i += 1

    prix_par_nom = {}
    i = 0
    while i < len(items):
        nom_item = items[i][0]
        prix_item = items[i][1]
        prix_par_nom[nom_item] = prix_item
        i += 1
    obligatoires = ["Baguette magique", "Robe de sorcier", "Manuel de potions"]
    i = 0
    while i < len(obligatoires):
        ob = obligatoires[i]
        if ob not in prix_par_nom:
            print(f"\nErreur : l’objet obligatoire « {ob} » est absent du catalogue.")
            return False
        i += 1
    obligatoires_restants = obligatoires[:]

    def afficher_catalogue():
        print("\nCatalogue des objets disponibles :")
        idx = 1
        j = 0
        while j < len(items):
            nom_item, prix_item = items[j]
            print(f"{idx}. {nom_item} - {prix_item} galions")
            idx += 1
            j += 1

    def recap_obligatoires():
        if len(obligatoires_restants) > 0:
            print("\nObjets obligatoires restant à acheter : " + ", ".join(obligatoires_restants))
        else:
            print("\nTous les objets obligatoires ont été achetés !")
            print("Il est temps de choisir votre animal de compagnie pour Poudlard !")

    def reste_abordable():
        if len(obligatoires_restants) == 0:
            return True
        cout_min = None
        j = 0
        while j < len(obligatoires_restants):
            nom_oblig = obligatoires_restants[j]
            prix = prix_par_nom[nom_oblig]
            if (cout_min is None) or (prix < cout_min):
                cout_min = prix
            j += 1
        return joueur["Argent"] >= cout_min
    noms = []
    i = 0
    while i < len(items):
        noms.append(items[i][0])
        i += 1

    print(f"\nVous avez {joueur['Argent']} galions.")
    afficher_catalogue()
    recap_obligatoires()
    while len(obligatoires_restants) > 0:
        nom_choisi = demander_choix("\nEntrez le numéro de l’objet à acheter :", noms)
        if nom_choisi not in prix_par_nom:
            print("Objet inconnu. Réessayez.")
            continue
        prix = prix_par_nom[nom_choisi]
        deja_oblig = False
        if nom_choisi in obligatoires:
            if nom_choisi in joueur["Inventaire"]:
                deja_oblig = True
        if deja_oblig:
            print(f"Vous avez déjà acheté : {nom_choisi}.")
            continue
        if joueur["Argent"] < prix:
            print("Vous n’avez pas assez d’argent pour cet achat... Fin du jeu.")
            return False
        modifier_argent(joueur, -prix)
        ajouter_objet(joueur, "Inventaire", nom_choisi)
        print(f"Vous avez acheté : {nom_choisi} (-{prix} galions).")
        print(f"Vous avez {joueur['Argent']} galions.")
        k = 0
        found_index = -1
        while k < len(obligatoires_restants):
            if obligatoires_restants[k] == nom_choisi:
                found_index = k
                break
            k += 1
        if found_index != -1:
            nouvelle_liste = []
            t = 0
            while t < len(obligatoires_restants):
                if t != found_index:
                    nouvelle_liste.append(obligatoires_restants[t])
                t += 1
            obligatoires_restants = nouvelle_liste
        if not reste_abordable():
            print("Il ne vous reste plus assez d’argent pour compléter les objets obligatoires...")
            print("Le directeur vous renvoie chez les Dursley. Fin du jeu.")
            return False
        recap_obligatoires()
    print(f"\nVous avez {joueur['Argent']} galions. Voici les animaux disponibles :")
    animaux = [("Chouette", 20), ("Chat", 15), ("Rat", 10), ("Crapaud", 5)]
    idx = 1
    i = 0
    while i < len(animaux):
        nom, prix = animaux[i]
        print(f"{idx}. {nom} - {prix} galions")
        idx += 1
        i += 1
    noms_animaux = []
    i = 0
    while i < len(animaux):
        noms_animaux.append(animaux[i][0])
        i += 1
    nom_animal = demander_choix("Quel animal voulez-vous ?", noms_animaux)
    prix_animal = None
    i = 0
    while i < len(animaux):
        if animaux[i][0] == nom_animal:
            prix_animal = animaux[i][1]
            break
        i += 1
    if prix_animal is None:
        print("Choix d’animal invalide... Fin du jeu.")
        return False
    if joueur["Argent"] < prix_animal:
        print("Pas assez d’argent pour l’animal choisi... Fin du jeu.")
        return False
    modifier_argent(joueur, -prix_animal)
    ajouter_objet(joueur, "Inventaire", nom_animal)
    print(f"Vous avez choisi : {nom_animal} (-{prix_animal} galions).")
    print("\nVoici votre inventaire final :")
    afficher_personnage(joueur)
    return True

def lancer_chapitre_1():
    introduction()
    joueur = creer_personnage()
    if not recevoir_lettre():
        print("\nFin du Chapitre 1 (lettre refusée).")
        sys.exit(0)
    rencontrer_hagrid(joueur)
    if not acheter_fournitures(joueur):
        print("\nFin du Chapitre 1 (achats impossibles).")
        sys.exit(0)
    print("\nFin du Chapitre 1 ! Votre aventure commence à Poudlard...")
    return joueur