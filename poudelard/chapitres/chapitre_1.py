from poudelard.utils.input_utils import (
    demander_texte,
    demander_nombre,
    demander_choix,
    load_fichier,
)
from poudelard.univers.personnage import (
    initialiser_personnage,
    afficher_personnage,
    modifier_argent,
    ajouter_objet,
)

def _choisir_option(message, options):
    choix = demander_choix(message, options)

    if isinstance(choix, int):
        if choix < 1 or choix > len(options):
            print("Choix hors des bornes.")
            return _choisir_option(message, options)
        return options[choix - 1]

    if choix not in options:
        try:
            idx = int(str(choix))
            if 1 <= idx <= len(options):
                return options[idx - 1]
        except (ValueError, TypeError):
            pass
        print("Choix invalide.")
        return _choisir_option(message, options)
    return choix

def _to_int_prix(raw):
    if isinstance(raw, (int, float)):
        return int(raw)
    if isinstance(raw, str):
        s = raw.strip()
        digits = "".join(ch for ch in s if ch.isdigit())
        if digits == "":
            print(f"Erreur: prix invalide (« {raw} »). Attendu un nombre.")
            exit(1)
        return int(digits)
    print(f"Erreur: type de prix invalide ({type(raw).__name__}).")
    exit(1)

def _normaliser_catalogue(donnees_catalogue):
    items = []
    if isinstance(donnees_catalogue, dict):
        for nom, prix in donnees_catalogue.items():
            items.append((str(nom), _to_int_prix(prix)))
    elif isinstance(donnees_catalogue, list):
        for objet in donnees_catalogue:
            if not isinstance(objet, dict) or "nom" not in objet or "prix" not in objet:
                print("Erreur : chaque entrée du catalogue doit contenir 'nom' et 'prix'.")
                exit(1)
            items.append((str(objet["nom"]), _to_int_prix(objet["prix"])))
    else:
        print("Erreur : format du fichier inventaire.json invalide.")
        exit(1)

    items.sort(key=lambda x: x[0].lower())
    return items

def _afficher_catalogue(items):
    print("Catalogue des objets disponibles :")
    for i, (nom, prix) in enumerate(items, start=1):
        print(f"{i}. {nom} - {prix} galions")

def _reste_abordable(joueur, obligatoires_restants, prix_par_nom):
    if not obligatoires_restants:
        return True
    cout_min = min(prix_par_nom[n] for n in obligatoires_restants)
    return joueur["Argent"] >= cout_min

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

    options = ["Oui, bien sûr !", "Non, je préfère rester avec l’oncle Vernon..."]
    rep = _choisir_option("Souhaitez-vous accepter cette invitation et partir pour Poudlard ?", options)

    if rep == options[1]:
        print("\nVous déchirez la lettre. L’oncle Vernon s’écrie :")
        print("« EXCELLENT ! Enfin quelqu’un de NORMAL dans cette maison ! »")
        print("Le monde magique ne saura jamais que vous existiez... Fin du jeu.")
        exit(0)
    print("\nParfait ! Fais tes bagages, l’aventure commence !")

def rencontrer_hagrid(joueur):
    print("\nUn géant frappe à la porte et entre d’un air bonhomme...")
    prenom = joueur.get("Prenom", "")
    print(f"Hagrid : « Salut {prenom} ! Je suis venu t’aider à faire tes achats sur le Chemin de Traverse. »")

    rep = _choisir_option(
        "Voulez-vous suivre Hagrid ?",
        ["Oui", "Non"]
    )

    if rep == "Non":
        print("Hagrid insiste gentiment et t’entraîne quand même avec lui !")
    else:
        print("Tu suis Hagrid dans les rues animées du Chemin de Traverse.")

def acheter_fournitures(joueur):
    print("\nBienvenue sur le Chemin de Traverse !")

    donnees = load_fichier("poudelard/data/inventaire.json")
    items = _normaliser_catalogue(donnees)
    _afficher_catalogue(items)

    prix_par_nom = {nom: prix for (nom, prix) in items}
    noms_catalogue = [nom for (nom, _p) in items]

    obligatoires = ["Baguette magique", "Robe de sorcier", "Manuel de potions"]
    for nom_ob in obligatoires:
        if nom_ob not in prix_par_nom:
            print(f"Erreur : l’objet obligatoire « {nom_ob} » est absent du catalogue.")
            exit(1)
    obligatoires_restants = obligatoires[:]

    def recap_obligatoires():
        if obligatoires_restants:
            print("Objets obligatoires restant à acheter : " + ", ".join(obligatoires_restants))
        else:
            print("Tous les objets obligatoires ont été achetés !")
            print("Il est temps de choisir votre animal de compagnie pour Poudlard !")

    print(f"Vous avez {joueur['Argent']} galions.")
    recap_obligatoires()

    while obligatoires_restants:
        labels = [f"{nom} - {prix_par_nom[nom]} galions" for nom in noms_catalogue]
        choix = _choisir_option("Entrez le numéro de l’objet à acheter :", labels)
        nom_choisi = choix.split(" - ")[0]
        prix_choisi = prix_par_nom[nom_choisi]

        if nom_choisi in joueur["Inventaire"] and nom_choisi in obligatoires:
            print(f"Vous avez déjà acheté : {nom_choisi}.")
            continue

        if joueur["Argent"] < prix_choisi:
            print("Vous n’avez pas assez d’argent pour cet achat... Fin du jeu.")
            exit(0)

        modifier_argent(joueur, -prix_choisi)
        ajouter_objet(joueur, "Inventaire", nom_choisi)
        print(f"Vous avez acheté : {nom_choisi} (-{prix_choisi} galions).")
        print(f"Vous avez {joueur['Argent']} galions.")

        if nom_choisi in obligatoires_restants:
            obligatoires_restants.remove(nom_choisi)

        if not _reste_abordable(joueur, obligatoires_restants, prix_par_nom):
            print("Il ne vous reste plus assez d’argent pour compléter les objets obligatoires...")
            print("Le directeur vous renvoie chez les Dursley. Fin du jeu.")
            exit(0)
        recap_obligatoires()

    print(f"\nVous avez {joueur['Argent']} galions. Voici les animaux disponibles :")
    animaux = [("Chouette", 20), ("Chat", 15), ("Rat", 10), ("Crapaud", 5)]
    labels_animaux = [f"{nom} - {prix} galions" for (nom, prix) in animaux]
    choix_animal = _choisir_option("Quel animal voulez-vous ?", labels_animaux)
    nom_animal = choix_animal.split(" - ")[0]
    prix_animal = dict(animaux)[nom_animal]

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