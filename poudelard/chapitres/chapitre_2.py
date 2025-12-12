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
        joueur["attributs"]["loyauté"]+=1
    if choix_drago == "3":
        joueur["attributs"]["courage"]+=1

    #FIN DE LA SCENE

    print("\nLe train continue sa route. Le château de Poudlard se profile à l'horizon..")
    print("\nTes choix semblent déjâ en dire long sur ta personnalité !")
    print("\nTes attributs sont mis à jour :", joueur["attributs"])

    return joueur