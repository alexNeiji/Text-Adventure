def ask_input(prompt):
    reponse = input(prompt)
    if reponse == "quit":
        print("Au revoir!")
        exit()
    return reponse

def main():
    print("Bienvenue dans Text Adventure!")

    print("Voulez-vous jouer?")
    reponse = ask_input("o/n: ")
    Play = False
    if reponse == "o":
        print("Super! Commençons l'aventure!")
        Play = True
    elif reponse == "n":
        print("D'accord, peut-être une autre fois!")
    else:
        print("Saisie invalide.")

    if Play:
        AskName = ask_input("Quel est votre nom? ")
        if AskName.__len__() == 0:
            print("Vous n'avez pas entré de nom. Veuillez réessayer.")
            raise TypeError("Le nom ne peut pas être vide.")
        elif AskName.__len__() > 20:
            print("Le nom est trop long. Veuillez réessayer.")
            raise TypeError("Le nom doit être de 20 caractères ou moins.")
        else:
            Name = AskName
            print("Bienvenue, " + Name + "! Votre aventure commence maintenant.")
            print("Vous vous réveillez dans une salle illuminée par une seule ampoule suspendue au plafond. Il n'y a pas de fenêtres mais seulement une porte.")
            print("Vous vous souvenez seulement de votre nom et de votre désir de sortir d'ici.")
            print("Que voulez-vous faire?")
            print("1. Crier pour attirer l'attention.")
            print("2. Examiner la pièce pour trouver des objets.")
            print("3. Tenter d'ouvrir la porte.")
            print("4. S'asseoir par terre et attendre quelqu'un.")
            choix = ask_input("Entrez le numéro de votre choix: ")
            if choix == "1":
                print("Vous criez à pleins poumons, quelqu'un arrive et vous ouvre en vous demandans de le suivre.")
                print("Vous suivez la personne à travers un long couloir sombre, jusqu'à ce que vous arriviez à une autre pièce.")
                print("La personne vous force à vous assoir sur une chaise et vous attache.")
                print("Vous remarquez maintenant que vous êtes sur une chaise électrique, et que la personne est un scientifique fou qui veut vous électrocuter pour ses expériences.")
                print("Malheuresement, vous aviez dejà grillé, c'était trop tard.")
            elif choix == "2":
                print("Vous fouillez la pièce et trouvez une cuillère et un bol de soupe froide.")
                print("Voulez-vous boire la soupe?")
                reponse_soupe = ask_input("o/n: ")
                if reponse_soupe == "o":
                    print("Vous buvez la soupe et vous endormez sans jamais vous réveiller.")
                else:
                    print("Que voulez-vous faire ensuite?")
                    print("1. Crier pour attirer l'attention.")
                    print("3. Tenter d'ouvrir la porte.")
                    print("4. S'asseoir par terre et attendre quelqu'un.")
                    choix2 = ask_input("Entrez le numéro de votre choix: ")
                    if choix2 == "1":
                        print("Vous criez à pleins poumons, quelqu'un arrive et vous ouvre en vous demandans de le suivre.")
                        print("Vous suivez la personne à travers un long couloir sombre, jusqu'à ce que vous arriviez à une autre pièce.")
                        print("La personne vous force à vous assoir sur une chaise et vous attache.")
                        print("Vous remarquez maintenant que vous êtes sur une chaise électrique, et que la personne est un scientifique fou qui veut vous électrocuter pour ses expériences.")
                        print("Malheuresement, vous aviez dejà grillé, c'était trop tard.")
                    elif choix2 == "3":
                        print("Vous essayez d'ouvrir la porte mais elle est verrouillée. Vous entendez des bruits de pas derrière la porte.")
                        print("Soudainement, la porte s'ouvre brusquement et un groupe de personnes masquées entre dans la pièce.")
                        print("Ils vous capturent et vous emmènent dans un endroit inconnu où ils font des expériences sur vous.")
                    elif choix2 == "4":
                        print("Vous décidez de rester assis par terre et d'attendre quelqu'un. Après un moment, une personne entre dans la pièce et vous voit assis là.")
                        print("Elle vous dis: Tu as été Bien sage, je t'accorde une pause, sort dans la cour.")
            elif choix == "3":
                print("Vous essayez d'ouvrir la porte mais elle est verrouillée. Vous entendez des bruits de pas derrière la porte.")
                print("Soudainement, la porte s'ouvre brusquement et un groupe de personnes masquées entre dans la pièce.")
                print("Ils vous capturent et vous emmènent dans un endroit inconnu où ils font des expériences sur vous.")
            elif choix == "4":  
                print("Vous décidez de rester assis par terre et d'attendre quelqu'un. Après un moment, une personne entre dans la pièce et vous voit assis là.")
                print("Elle vous dis: Tu as été Bien sage, je t'accorde une pause, sort dans la cour.")
                choix4 = True
            else:
                print("Saisie invalide. Veuillez réessayer.")
                raise TypeError("Choix doit être 1, 2, 3 ou 4.")
        if choix4:
            print("Vous sortez dans la cour et vous voyez un groupe de personnes qui jouent au football avec un caillou.")
            print("Ils vous invitent à jouer avec eux mais vous ne jouez pas vraiment vous faites un plan pour s'échapper, au passage vos 4 nouveaux amis vous expliquent où vous êtes.")
            print("Vous apprenez que vous êtes dans un laboratoires d'experimentation humaine, et que les personnes qui vous ont capturé sont des scientifiques fous qui font des expériences sur les gens.")
            print("Vous décidez de rentrer dans votre cellule.")
            print("Que faites-vous?")
            print("1. Vous rejoignez vos amis pour vous échapper un fois la nuit tombée.")
            print("2. Vous décidez de rester dans votre cellule car vous ne voulez pas vous échapper.")
            choix5 = ask_input("Entrez le numéro de votre choix: ")
            if choix5 == "1":
                print("Vous rejoignez vos amis pour vous échapper une fois la nuit tombée. Vous suivez le plan qu'ils ont élaboré et vous réussissez à vous échapper du laboratoire en hélicoptère.")
                print("Vous courez à travers les bois et vous vous souvenez de tout.")
                print("Vous savez où vous habitez et comment vous vous êtes retrouvés dans le laboratoire.")
                print("Vous rentrez chez vous, vous y êtes en sécurité et vous êtes heureux d'être libre.")
                print("Félicitations, vous avez gagné!")
            elif choix5 == "2":
                print("Vous décidez de rester dans votre cellule car vous ne voulez pas vous échapper.")
                print("Vous attendez patiemment que quelqu'un vienne vous voir.")
                print("Après un moment, une personne entre dans votre cellule et vous emmene dans une autre pièce.")
                print("Vous suivez la personne à travers un long couloir sombre, jusqu'à ce que vous arriviez à une autre pièce.")
                print("La personne vous force à vous assoir sur une chaise et vous attache.")
                print("Vous remarquez maintenant que vous êtes sur une chaise électrique, et que la personne est un scientifique fou qui veut vous électrocuter pour ses expériences.")
                print("Malheuresement, vous aviez dejà grillé, c'était trop tard.")              

while True:
    main()
    print("\n" + "="*50 + "\n")
    rejouer = ask_input("Voulez-vous recommencer? o/n: ")
    if rejouer != "o":
        print("Au revoir!")
        break
