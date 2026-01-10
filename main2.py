# Lien depot github : https://github.com/BigLineDev0/tp11-python

liste_apprenants = []

# Fonction pour ajouter un apprenant
def ajouter_apprenant():
   
    # identifiant = input("Entrez votre identifiant : ")

    # for a in liste_apprenants:

    #     if a['id'] == identifiant:

    #         print("\n Cet identifiant existe deja.")
    #         return

    # longuer de liste + 1
    identifiant = f'ID_{len(liste_apprenants) + 1}'
    # print(identifiant)
        
    while True:
        nom = input("Nom : ").strip()
        if nom.replace(" ", "").replace("-", "").isalpha():
            break
        else:
            print("\nNom invalide. Uniquement des lettres")

    while True:
        prenom = input("Prénom : ").strip()
        if prenom.replace(" ", "").replace("-", "").isalpha():
            break
        else:
            print("\nPrenom invalide. Uniquement des lettres")

    while True:
        promo = input("Promo : ").strip().lower()
        if promo.startswith("p") and promo[1:].isnumeric():
            break
        else:
            print("\nPromo Invalide. Veuillez réessayer (ex: p4)")

    apprenant = {
        'id':identifiant,
        'nom':nom,
        'prenom':prenom,
        'promo':promo,
        'presence': None # par defaut false
    }

    liste_apprenants.append(apprenant)

    print("\nApprenant enregistré avec succes. ")

# Fonction pour afficher la liste des apprenants
def afficher_liste_apprenant():

    if not liste_apprenants:
        print("\nla liste est vide.")
        return

    for i, a in enumerate(liste_apprenants, 1):
        if a['presence']:
            statut = a['presence']
        else:
            statut = "absent"

        # statut = a['presence'] if a['presence'] else 'Non pointé'

        print(f"{i}. {a['id']} - {a['prenom']} {a['nom']} ({a['promo']}) - {statut}")

# Fonction  pour marquer une présence
def pointer_apprenant():
    if not liste_apprenants:
        print("\nAucun apprenant enregistré.")
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
                print("\nApprenant marquer present")
                break

            elif marquer == 'a':
                apprenant['presence'] = "absent"
                print("\nApprenant marquer absent")
                break

            else:
                print("\n Tapez A(absent) ou P(présent)")

# Fonction pour afficher la liste des présences
def lister_presence():
    if not liste_apprenants:
        print("\n Aucun apprenant.")

    nbre_present = 0

    for apprenant in liste_apprenants:

        if apprenant['presence'] == 'present':

            nbre_present += 1

            print(f"{apprenant['id']}: {apprenant['prenom']} {apprenant['nom']} promo : {apprenant['promo']} statut : {apprenant['presence']}")

    print(f"Il y a {nbre_present} présents sur {len(liste_apprenants)}")

# Fonction pour afficher la liste des absences
def lister_absence():
    if not liste_apprenants:
        print("\n Aucun apprenant.")

    nbre_absence = 0

    for apprenant in liste_apprenants:

        if apprenant['presence'] == 'absent':

            nbre_absence += 1

            print(f"{apprenant['id']}: {apprenant['prenom']} {apprenant['nom']} promo : {apprenant['promo']} statut : {apprenant['presence']}")

    print(f"Il y a {nbre_absence} absent sur {len(liste_apprenants)}")

# Fonction pour calculer le taux de présence
def taux_presence():
   
    total_apprenant = len(liste_apprenants)

    presents = 0
    absents = 0

    for apprenant in liste_apprenants:
        if apprenant["presence"] == "present":
            presents = presents + 1
        else:
            absents = absents + 1
    try:       
        taux_presence = (presents / total_apprenant ) * 100
    except ZeroDivisionError:
        print("Aucun taux car la liste des apprenants est vide")

    print("---- Taux de Présence ----")
    print(f"Nombre total d'apprenants {total_apprenant}")
    print(f"Nombre de présents : {presents}")
    print(f"Nombre d'absents : {absents}")
    print(f"Taux de présence : {taux_presence} %")
    print("-" * 40)

# Fonction afficher le menu
def menu():

    print("\n-------- Application de Poitage --------")
    print("1. Ajouter un apprenant")
    print("2. Aficher le nombre total d'apprenants")
    print("3. Marquer un apprenant")
    print("4. Afficher les apprenants présents")
    print("5. Afficher les apprenants absents")
    print("6. Calculer le taux de présence")
    print("0. Quitter")
    print("-" * 40)

# Fonction principale
def main():
    while  True:
        menu()
        choix = input("\nChoisissez une option : ")
            
        if choix == '1':
            ajouter_apprenant()
        elif choix == '2':
           print(f"Nombre totlal d'apprenant : {len(liste_apprenants)}")
        elif choix == '3':
           pointer_apprenant()
        elif choix == '4':
            lister_presence()
        elif choix == '5':
            lister_absence()
        elif choix == '6':
            taux_presence()
        elif choix == '0':
            print("Au revoir!")
            break 
        else:
            print("\nOption invalide, veuillez réessayer.")

main()