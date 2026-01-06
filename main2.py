liste_apprenants = []
def ajouter_apprenant():
   
    identifiant = input("Entrez votre identifiant : ")

    for a in liste_apprenants:

        if a['id'] == identifiant:

            print("Cet identifiant existe deja.")
            return
    while True:
        nom = input("Votre nom : ")
        if nom.isalpha():
            break
        else:
            print("Nom invalide. Uniquement des lettres")
    while True:
        prenom = input("Votre prénom : ")
        if prenom.isalpha():
            break
        else:
            print("Prenon invalide. Uniquement des lettres")

    promo = input("Votre promo : ")

    apprenant = {
        'id':identifiant,
        'nom':nom,
        'prenom':prenom,
        'promo':promo,
        'presence': None
    }

    liste_apprenants.append(apprenant)

    print("\n Apprenant enregistré avec succes. ")

# Fonction pour afficher la liste des apprenants
def afficher_liste_apprenant():

    if not liste_apprenants:
        print("\n la liste est vide.")
        return

    for i, a in enumerate(liste_apprenants, 1):

        statut = a['presence'] if a['presence'] else 'Non pointé'

        print(f"{i}. {a['prenom']} {a['nom']} ({a['promo']}) - {statut}")

# Fonction  pour marquer une présence
def pointer_apprenant():
    if not liste_apprenants:
        print("Aucun apprenant enregistré.")
        return
    
    print("\nla liste des apprenants")
    
    while True:
        afficher_liste_apprenant()

        choix = input("\nChoisissez le numéro de l'apprenant à pointer (0 pour quitter) : ")

        if choix == '0':
            print("Fin du pointage")
            break

        if not choix.isdigit():
            print("Veuillez saisir un numero")
            continue

        choix = int(choix)

        if choix < 1 or choix > len(liste_apprenants):
            print("Nombre invalide")
            continue

        apprenant = liste_apprenants[choix - 1]

        while True:
            marquer = input(f"Marquer {apprenant['prenom']} {apprenant['nom']} ('P(présent) / A(absent)') : ").lower()

            if marquer == 'p':
                apprenant['presence'] = "present"
                print("Apprenant marquer present")
                break

            elif marquer == 'a':
                apprenant['presence'] = "absent"
                print("apprenant marquer absent")
                break

            else:
                print("Tapez A(absent) ou P(présent)")

# Fonction pour afficher la liste des présences
def lister_presence():

    nbre_present = 0

    for apprenant in liste_apprenants:

        if apprenant['presence'] == 'present':

            nbre_present += 1

            print(f"{apprenant['id']}: {apprenant['prenom']} {apprenant['nom']} promo : {apprenant['promo']} statut : {apprenant['presence']}")

            print(f"\nIl y a {nbre_present} présents sur {len(liste_apprenants)}")

# Fonction pour calculer le taux de présence
def taux_presence():
    if not liste_apprenants:
        print("\n Aucun apprenant.")
    
    total_apprenant = len(liste_apprenants)

    presents = 0

    for apprenant in liste_apprenants:
        if apprenant["presence"] == "present":
            presents = presents + 1
            
    taux_presence = (presents / total_apprenant ) * 100

    print(f"le taux de présence est : {taux_presence} %")


# Fonction afficher le menu
def menu():

    print("\n ====== Application de Poitage =====")
    print("1. Ajouter un apprenant")
    print("2. Pointer un apprenant")
    print("3. Afficher les apprenants présents")
    print("4. Calculer le taux de présence")
    print("0. Quitter")

# Fonction principale
def main():
    while  True:
        menu()
        choix = input("\n Choisissez une option : ")
            
        if choix == '1':
            ajouter_apprenant()
        elif choix == '2':
           pointer_apprenant()
        elif choix == '3':
            lister_presence()
        elif choix == '4':
            taux_presence()
        elif choix == '0':
            print("Au revoir!")
            break 
        else:
            print("Option invalide, veuillez réessayer.")
main()
