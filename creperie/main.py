import ingredient
from crepe import Crepe
import os


"""-------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
"""---------------------------------------------------------------------\CREATION VARIABLE AVEC CLASSE/---------------------------------------------------------------------"""
"""-------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""


crepe_nutella = Crepe("Nutella")
crepe_fraise_chantilly = Crepe("Fraise Chantilly")
crepe_kebab_poulet = Crepe("Kebab Poulet")
crepe_emmental = Crepe("Emmental")
crepe_jambon_emmental = Crepe("Jambon Emmental")
crepe_perso = Crepe("Perso")



"""-------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
"""-------------------------------------------------------------------\FIN CREATION VARIABLE AVEC CLASSE/-------------------------------------------------------------------"""
"""-------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""


"""-------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
"""---------------------------------------------------------------------\CREATION VARIABLES UTILES/-------------------------------------------------------------------------"""
"""-------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""


#Récupère le dictionnaire prix dans le fichier ingredient.py
prix_ingredients = ingredient.prix

#Récupère le dictionnaire ingrédient dans le fichier ingredient.py
ingredients = ingredient.ingredients 

liste_crepe = [crepe_nutella, crepe_kebab_poulet, crepe_fraise_chantilly, crepe_jambon_emmental, crepe_emmental, crepe_perso]

#Ouvre les fichiers en ajout uniquement 
filin = open("liste_crepe.txt", "a")
ajout_clients = open("clients.txt", "a")

#Ouvre les fichiers en écriture uniquement
ticket_de_caisse = open("ticket_de_caisse.txt", "w+")

#Fait tourner le programme
running = True

#Va contenir les crêpes dans le panier
panier=[]


"""-------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
"""-------------------------------------------------------------------\FIN CREATION VARIABLES UTILES------------------------------------------------------------------------"""
"""-------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""


"""-------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
"""--------------------------------------------------------------------------------\FONCTIONS/------------------------------------------------------------------------------"""
"""-------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""



#1.Fonction qui renvoie la taille d'une variable#


def taille(smt):
    return len(smt)


#-----------------------------------------------#


#2.Tri à bulle, renvoie un tableau trié/une liste triée (ici par ordre croissant alphabétique)#


def tri_bulle(tab):
    n = taille(tab)
    # Traverser tous les éléments du tableau
    for i in range(n):
        for j in range(0, n-i-1):
            # échanger si l'élément trouvé est plus grand que le suivant
            if tab[j].nom > tab[j+1].nom :
                tab[j], tab[j+1] = tab[j+1], tab[j]


#---------------------------------------------------------------------------------------------#
            

#3. Tri selection, renvoie un tableau trié/une liste triée (ici par ordre croissant des prix)#


def tri_selec(tab):
    n = taille(tab)
    for i in range(n):
        min = tab[i]
        
        for j in range(n-i):
            if (min.prix > tab[j+i].prix):
                min = tab[j+i]
    tab.remove(min)
    tab.insert(i, min)


#--------------------------------------------------------------------------------------------#       


#4. Renvoie les ingrédients d'une crêpe sous forme de string#
def show_ingredients(liste):
    car = ""
    for element in liste:
        car = car + element + " | "
    return car + "\n"


#-----------------------------------------------------------#


#5. Fonction qui prend en entrée une liste et qui affiche la liste de ses éléments#


def renvoie_crepe(liste):
    car =""
    for i, element in enumerate(liste):
        if type(element) == str:
            car = car + (f"{i+1}. {element} ")
        elif type(element) == tuple:
            car = car + (f"{i+1}. {element[0].nom}: ") + show_ingredients(element[1])
        elif type(element.nom) == str:
            car = car + (f"{i+1}. {element.nom} ")
    return car

#--------------------------------------------------------------------------------#


#6. Fonction affiche les éléments d'une liste pour les crêpes-------------------------------------------------------------#


def affiche_crepe(liste):

    for i, element in enumerate(liste):
        print("                                     ", f"{i+1}. {element.nom}.\n-----------Prix : {element.prix} €-----------" )
        print(("                             ", f"-----------Ingrédients : {element.ingredient}-----------\n") 
                if type(element.ingredient) == str 
                else (("                             ",f"-----------Ingrédients : {show_ingredients(element.ingredient)}-----------\n") 
                    if taille(element.ingredient)>1 
                    else (("                             ",f"-----------Ingrédient : {show_ingredients(element.ingredient)}-----------\n"),)  + (f"-----------Saveur : {element.saveur}-----------\n",)))



#---------------------------------------------------------------------------------------------------------------------------------------------------------------#


#7. Fonction qui ajoute un supplément------------------------------------------------------------------------------------------------------------#


def add_supplement(supplement_liste, prix):
    
    supplementAdd_True = True
    while supplementAdd_True:
        #La première lettre de l'ingrédient entrée est mise en majuscule et toutes les autres en minuscule  
        supplement_add = input("Quel ingrédient voulez vous ajouter ? ")
        supplement_add = supplement_add.lower()
        supplement_add = supplement_add.title()
        #Test si l'entrée n'est pas dans la liste des ingredients
        if supplement_add in ingredients["Sucrée"] or supplement_add in ingredients["Salée"] or supplement_add in ingredients["Végétarienne"]:
            os.system('cls')
            print(f"Ajout de {supplement_add}")
           
            prix += prix_ingredients[f"{supplement_add}"]
            supplementAdd_True = False  
            supplement_liste.append(supplement_add)              
        else:    
            os.system('cls')
            print("L'élément n'est pas dans la liste, veuillez reessayer.")

    return supplement_liste, prix


#------------------------------------------------------------------------------------------------------------------------------------------------#

              
#8. Fonction qui demande si le client veut ajouter un supplément-------------------------------------------------------------#


def ask_supplement(liste_crepe, inputNumber):
    ask_supplement = True

    #Si le client ne demande pas de supplèment alors il n'y aura pas de prix supplémentaire et d'aliment ajouter
    prix = 0
    supplement_liste = []

    while ask_supplement:
        
        # Demande d'ajout d'un supplément
        suppl = input("Voulez vous ajouter un supplément sur votre crêpe ? [Y/N] ")
        suppl = suppl.title()
        if suppl == "Y":
            os.system('cls')
            print("Liste ingrédients: ")

            #Cas d'une crêpe sucrée
            if liste_crepe[inputNumber-1].saveur == "Sucrée":
                print("Sucrée: ", show_ingredients(ingredients["Sucrée"]),"\n")

            #Cas d'une crêpe salée
            elif liste_crepe[inputNumber-1].saveur == "Salée":
                print("Salée: ", show_ingredients(ingredients["Salée"]))
                print("Végétarienne: ", show_ingredients(ingredients["Végétarienne"]), "\n")

            #Cas d'une crêpe végétarienne
            elif liste_crepe[inputNumber-1].saveur == "Végétarienne":
                print("Salée: ", show_ingredients(ingredients["Salée"]))
                print("Végétarienne: ", show_ingredients(ingredients["Végétarienne"]), "\n")

            #Cas d'une crêpe personalisée
            else:
                print("Salée: ", show_ingredients(ingredients["Salée"]))
                print("Sucrée: ", show_ingredients(ingredients["Sucrée"]))
                print("Végétarienne: ", show_ingredients(ingredients["Végétarienne"]), "\n")

            ajout_supp = add_supplement(supplement_liste, prix)
            supplement_liste = ajout_supp [0] #Nom du supplément
            prix = ajout_supp[1] #Prix du supplément

        elif suppl == "N":
            os.system('cls')
            print("\n")
            ask_supplement = False
            
        else:
            os.system('cls')
            print("Ce choix n'est pas possible\n")

    return supplement_liste, prix


#------------------------------------------------------------------------------------------------------------------------------------------------#


#9. Calcul le coût total du panier#


def cout_panier(panier):
    prix = 0
    for element in panier:
        prix += element[2]
    return prix


#---------------------------------#


#10. Supprimer un élément du panier--#


def suppElem_panier(panier, element):

    panier.remove(element)
    return panier


#-----------------------------------#


#11. Ecrire dans le fichier texte--------------------------------------------#


def write_text(listetuple, file, ispanier):
    n = taille(listetuple)
    
    for i in range(n):
        file.write("\n")
        file.write("\====================================================================================================/\n")
        file.write(f"                               Saveur : {((listetuple[i])[0]).saveur}                      \n")
        file.write(f"                               Prix : {listetuple[i][2]}€                                  \n")
        file.write(f"                               Ingrédients : {show_ingredients(listetuple[i][1])}          \n")
        file.write("/====================================================================================================\ \n")
        file.write("\n")

    if ispanier:
        file.write(f"                           Total : {cout_panier(listetuple)}€          \n")
        file.write("\n")
        file.write("/====================================================================================================\ \n")

#----------------------------------------------------------------------------#


#12. Entre un nouveau client dans le registre ou Accède au contenu des clients récurrents-----------------------------------------#


def client():
    new_client = True
    while new_client:
        is_new_client = input("                               Etes-vous un nouveau client? [Y/N] ")
        is_new_client = is_new_client.title()
        
        #Si c'est un nouveau client
        if is_new_client == "Y":
            
            #Console plus propre
            os.system('cls')
            style_console(0)

            nom = input("                                   Entrez votre nom: ")
            nom = nom.upper()

            print("")

            prenom = input("                                   Entrez votre prénom : ")
            prenom = prenom.lower()
            prenom = prenom.title()


            #Montre la liste des crêpes au client pour qu'il choisisse sa préférée
            print("")
            print(renvoie_crepe(liste_crepe))
            print("")
            crepe_prefere = input("             Entrez votre Crêpe préférée (en toute lettre la crêpe sans accent): ")

            #Ajout du client dans le fichier clients.txt
            ajout_clients.write("*****************************************************************************************\n")
            ajout_clients.write(f"NOM et Prenom : {nom} {prenom}\n")

            ajout_clients.write(f"Crepe preferee : {crepe_prefere}\n")
            ajout_clients.write("*****************************************************************************************\n\n")
            new_client = False

        #Si le client est déjà dans le fichier
        elif is_new_client == "N":

            os.system('cls')
            style_console(0)

            nom = input("                                       Quel est votre nom : ")
            nom = nom.upper()

            print("")

            prenom = input("                                    Quel est votre prénom : ")
            prenom = prenom.lower()
            prenom = prenom.title()

            print("")

            #Ouvre le fichier clients.txt
            lire_clients = open("clients.txt", "r")

            #Lignes est une liste contenant chaque ligne du fichier
            lignes = lire_clients.readlines()
            for i, element in enumerate(lignes):

                nomprenom = f"NOM et Prenom : {nom} {prenom}\n"

                if nomprenom in element:
                    
                    #La ligne d'après contient forcément la crêpe préférée du client
                    crepe_prefere = lignes[i+1]
                    print("                                     ", crepe_prefere)
                    nom_crepe = crepe_prefere.split()[-1]
                    want_it = input("                            Voulez vous votre crêpe préférée dans votre panier? [Y/N] ")
                    print("\n\n")

                    #Il veut rajouter sa crêpe préférée au panier
                    if want_it == "Y":    
                        new_client = False
                        
                        
                        style_console(1)

                        input("\nAppuyez sur Entrée pour continuer...\n")
                        os.system('cls')

                        return nom_crepe

                    #Il ne veut pas rajouter sa crêpe préférée au panier
                    else:
                        
                        style_console(1)

                        input("\nAppuyez sur Entrée pour continuer...\n")
                        os.system('cls')

                        new_client = False

                    


                #Le client n'est pas dans le fichier client       
                elif i== taille(lignes)-1 and new_client:

                    os.system('cls')
                    style_console(0)

                    print("                                   Vous n'êtes pas enregistrés dans la liste.\n\n")

                    style_console(1)

                    input("\nAppuyez sur Entrée pour continuer...\n")
                    os.system('cls')

                elif i== taille(lignes)-1 and not new_client:
                    new_client = False

                else:
                    new_client = True
                lire_clients.close()
        else:
            print("                                   Choisissez Y ou N pour Oui ou Non.\n")
    
    style_console(1)
    input("\nAppuyez sur Entrée pour continuer...\n")
    os.system('cls')
    

#----------------------------------------------------------------------------------------------------------------------------------#


#13.Donne un style en début (0) et fin de console (1)------------------------------------------------------------------------------#


def style_console(entier):

    if (entier ==0):
        print("\====================================================================================================/\n\n")

    elif (entier == 1):
        print("/====================================================================================================\ \n\n")


#----------------------------------------------------------------------------------------------------------------------------------#

"""-------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
"""-----------------------------------------------------------------------------\FIN FONCTIONS/-----------------------------------------------------------------------------"""
"""-------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""





"""-------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
"""--------------------------------------------------------------------------\DEBUT DU PROGRAMME/---------------------------------------------------------------------------"""
"""-------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""


#Accueil du client
style_console(0)
print("                                 Bienvenue à la Crêperie Whaou!                                       ")
print("                   Ici vous pouvez déguster nos meilleures crêpes artisanales.                    \n\n")
style_console(1)

#Le client est-il nouveau?
client_rec = client()

#Si c'est un client récurrent on ajoute sa crêpe préférée à son panier (suivant sa demande)
if type(client_rec) == str:
    panier.append((Crepe(client_rec), Crepe(client_rec).ingredient, Crepe(client_rec).prix))
else:
    None

#Le programme est en cours d'éxécution
while(running):
    

    
    #S'il y a quelque chose à payer, afficher le panier
    if len(panier) != 0:
        os.system('cls')
        style_console(0)
        print("                                     Votre panier est de " + str(cout_panier(panier)) + f"€.\n                               Il est composé de : {renvoie_crepe(panier)}\n")
        style_console(1)

    
    
    #Les crêpes sont d'abord triés dans l'ordre croissant des prix puis dans l'ordre des alphabétiques
    tri_selec(liste_crepe)
    tri_bulle(liste_crepe)
    print("                                                   MENU: \n")
    affiche_crepe(liste_crepe)

    #Test pour que la valeur entrée soit un int entre 1 et 6
    choiceIngredient = True
    while choiceIngredient:
        try:
            if len(panier) != 0:
                print("\nPour supprimer un élément du panier, Entrez 0.\n")
                inputNumber = int(input("Choisissez une crêpe en entrant un nombre entre 0 et 6 : "))
            else:
                inputNumber = int(input("Choisissez une crêpe en entrant un nombre entre 1 et 6 : "))
            
            if inputNumber > 6 or inputNumber < 0:
                print("Cette valeur n'est pas reconnue.\n")
            elif inputNumber == 0 and cout_panier(panier) == 0:
                print("Cette valeur n'est pas reconnue.\n")
            else:
                choiceIngredient = False
        except:
            print("Cette valeur n'est pas reconnue.\n")

    #choix de la crepe classique + ajout du prix au panier
    choicePerso_True = True
    if (inputNumber <= 6 and inputNumber >0):

        if (inputNumber < 6 and inputNumber >0):
            os.system('cls') #Clear de la console
            print(f"Vous avez choisit une {liste_crepe[inputNumber-1].nom}.\nCela vous coûtera {liste_crepe[inputNumber-1].prix}€.\n")
        

        #choix de la crepe personalisée
        elif (inputNumber == 6):
            os.system('cls') #Clear de la console
            liste_crepe[inputNumber-1].ingredient = []
            choiceIngredient_True = True

            num_ingredient = 1

            #Choix des ingredients
            os.system('cls') #Clear de la console
            print("Liste ingrédients: ")
            print("Sucrée: ", show_ingredients(ingredients["Sucrée"]))
            print("Salée: ", show_ingredients(ingredients["Salée"]))
            print("Végétarienne: ", show_ingredients(ingredients["Végétarienne"]), "\n")
            print("Choisissez 3 ingrédients : ")

            while choiceIngredient_True:
            
                #La première lettre de l'ingrédient est mise en majuscule et toutes les autres en minuscule  
                choix_ingredient = input(f"Ingrédient {num_ingredient}: ")
                choix_ingredient = choix_ingredient.lower()
                choix_ingredient = choix_ingredient.title()
                

                #Test si l'entrée n'est pas dans la liste des ingredients
                if choix_ingredient in ingredients["Sucrée"] or choix_ingredient in ingredients["Salée"] or choix_ingredient in ingredients["Végétarienne"]:

                    num_ingredient += 1
                    
                    liste_crepe[inputNumber-1].ingredient.append(choix_ingredient)
                    print("Ajout de l'ingrédient à la crêpe perso...\n")
                    print(liste_crepe[inputNumber-1].ingredient)


                    if num_ingredient == 4:

                        os.system('cls') #Clear de la console
                        print(f"Votre crêpe personalisée contient comme ingrédients :")
                        print(renvoie_crepe(liste_crepe[inputNumber-1].ingredient))
                        choiceIngredient_True = False

                        os.system('cls') #Clear de la console
                        print(f"Vous avez choisit une {liste_crepe[inputNumber-1].nom}.\nCela vous coûtera {liste_crepe[inputNumber-1].prix}€.\n")

                        #Ajoute la crêpe perso dans la liste de crêpe (faux c'est pour n'est pas le panier)
                        write_text([(liste_crepe[inputNumber-1], liste_crepe[inputNumber-1].ingredient, liste_crepe[inputNumber-1].prix)], filin, False)
                        
                        input("\nAppuyez sur Entrée pour continuer...\n")
                        os.system('cls') #Clear de la console

                else:
                    os.system('cls') #Clear de la console
                    print("L'ingrédient n'est pas dans la liste.\nVeuillez rentrer un ingrédient qui est dans la liste.\n")


        """--------------------Demande au client si il souhaite un supplément--------------------"""


        #Récupère le tuple
        supp = ask_supplement(liste_crepe, inputNumber)
        #On récupère les nouvelles valeurs des ingrédients de la crêpe
        supplement_Add = supp[0]

        #On récupère le prix du supplément dans le tuple
        prix_supp = supp[1]

        panier.append((liste_crepe[inputNumber-1], liste_crepe[inputNumber-1].ingredient + supplement_Add, liste_crepe[inputNumber-1].prix + prix_supp))
        print(panier)
        print(renvoie_crepe(panier))


        """--------------Fin de la demande au client si il souhaite un supplément----------------"""


        input("Appuyez sur Entrée pour continuer...")
        os.system('cls') #Clear de la console

        
    elif(inputNumber == 0):
        

        """--------------------Demande au client si il souhaite supprimer un élément du panier--------------------"""
   

        os.system('cls')
        suppOn = True
        # Test si le choix de l'utilisateur est correct
        while suppOn:
            print("Votre panier est de " + str(cout_panier(panier)) + f"€.\nIl est composé de : \n{renvoie_crepe(panier)}\n")
            try:
                suppChoice = int(input("Quel item voulez vous enlever du panier ? [0 pour annuler] "))
                if suppChoice == 0:
                    os.system('cls')
                    suppOn = False
                elif suppChoice !=0 and suppChoice <= taille(panier) :
                    os.system('cls')
                    print(f"Suppression de {panier[suppChoice-1][0].nom}:\n {show_ingredients(panier[suppChoice-1][1])}")
                    panier = suppElem_panier(panier, panier[suppChoice-1])
                    print(f"Votre panier est de {str(cout_panier(panier))} €")
                    suppOn = False
                else:
                    os.system('cls')
                    print("Ce choix n'est pas possible\n")
            except:
                os.system('cls')
                print("Ce choix n'est pas possible, veuillez entrer un nombre.\n")
    

        """--------------Fin de la demande au client de la suppression de l'élément dans son panier----------------"""


    newCrepe_True = True 


    """--------------------Demande au client si il souhaite continuer ses achats--------------------"""


    #Possibilité d'ajouter une nouvelle crepe au panier
    while newCrepe_True:
        #Affichage du panier
        if len(panier) !=0:
            print("Votre panier est de " + str(cout_panier(panier)) + f"€.\nIl est composé de : \n{renvoie_crepe(panier)}\n")
        newCrepe = input("Souhaitez vous continuer vos achats ? [Y/N] ")
        
        # L'utilisateur souhaite continuer ses achats
        if newCrepe == "Y" or newCrepe == "y":
            print("")
            newCrepe_True = False


            os.system('cls') #Clear de la console

        # L'utilisateur ne souhaite pas continuer ses achats
        elif newCrepe == "N" or newCrepe == "n":
            os.system('cls') #Clear de la console
            if len(panier)!=0:
                print("Votre panier est de " + str(cout_panier(panier)) + f"€.\nIl est composé de : \n{renvoie_crepe(panier)}\n")
           
            
            print("Bonne journée et merci pour votre fidelité!\n")

            running = False
            newCrepe_True = False
        else:
            os.system('cls') #Clear de la console
            print("Cette valeur n'est pas reconnue.\n")


    """--------------Fin de la demande au client de la continuation de son panier----------------"""

#Créer un ticket de caisse (vrai pour c'est bien le panier et non pas une crepe perso)
write_text(panier, ticket_de_caisse, True)

# Ferme le dossier text.txt
filin.close()
ticket_de_caisse.close()


"""-------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
"""---------------------------------------------------------------------------\FIN DU PROGRAMME/----------------------------------------------------------------------------"""
"""-------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""