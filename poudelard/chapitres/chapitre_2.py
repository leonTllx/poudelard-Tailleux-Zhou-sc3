def rencontrer_amis(joueur):
    print("Salut ! Moi c'est Ron Weasley. Tu veux qu'on s'assoie ensemble ?")
    print("Que répondez-vous ?")
    print(" 1. Bien sûr, assieds-toi !")
    print(" 2. Désolé, je préfère voyager seul.")
    choix_ron = input("Votre choix ? : ")
    if choix_ron == "1":
        print("Ron s'assoit avec vous. Vous discutez et riez ensemble. Votre loyauté augmente de 1.")
        joueur["attributs"]["loyauté"]+=1
    elif choix_ron == "2":
        print("Vous préférez rester seul. Votre ambition augmente de 1.")
        joueur["attributs"]["ambition"]+=1
    else:
        print("Choix invalide, aucune modification effectuée.")
    return joueur