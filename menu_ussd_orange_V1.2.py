# Lien github : https://github.com/BigLineDev0/tp11-python

# Solde initial au demarage
solde = 10000
solde = float(solde)

CODE_SECRET = 9900

historiques_transferts = []

# Fonction pour verifier le code secret 
def verifier_code_secret():
    tentatives = 0
    while tentatives < 3:
        try:
            code = int(input("Entrer votre code secret Orange Money : "))

            if code == CODE_SECRET:
                return True
            else:
                tentatives += 1
                print(f"Code incorrect. Vous avez {tentatives}/3.")

        except ValueError:
            print("Code invalide. Entrer un nombre")

    print("Opération bloquée : trop de tentatives échouées.")
    return False


# Fonction pour afficher le menu principal
def menu_principale():
    print("\n","-" *10,"MENU USSD ORANGE MONEY", "-" *10)
    print("1. Consulter le solde")
    print("2. Effectuer des transferts")
    print("3. Acheter du crédit")
    print("4. Acheter un forfait")
    print("5. Historique des transferts")
    print("6. Annuler le dernier transfert")
    print("0. Quitter")
    print("-" * 40, "\n")


# Fonction pour verifier le code USSD
def code_ussd():

    while True:
        code = input("Composer votre USSD (ex: #144#) : ").strip()

        if code == '#144#':
            break
        else:
            print("Code invalide. Vueillez réessayer")


# Fonction message confirmation
def confirmer(message):
    print("\n" + message)
    print("1. Confirmer")
    print("2. Annuler")

    while True:
        choix = input("Votre choix : ")
        if choix == '1':
            return True
        elif choix == '2':
            return False
        else:
            print("Veuillez taper 1 ou 2.")


# Fonction pour saisir un choix
def saisir_choix(options):
    while True:
        choix = input("Choisissez une option : ").strip()
        if choix in options:
            return choix
        else:
            print("Option invalide.")


# Fonction pour saisir un montant
def saisir_montant(message):
    while True:
        try:
            montant = float(input(message))
            if montant > 0:
                return montant
            else:
                print("Le montant doit être supérieur à 0.")
        except ValueError:
            print("Erreur : veuillez entrer un nombre valide.")


# Fonction pour saisir un numéro de téléphone
def saisir_numero():
    while True:
        numero = input("Numéro de téléphone : ").replace(" ", "").strip()
       
        if numero.isdigit() and len(numero) == 9 and numero.startswith(("77", "78", "71")):
            return numero
        else:
            print("Numéro invalide. Exemple : 772345678")


# Fonction pour consuler le solde
def consuler_solde():
    global solde
    if verifier_code_secret():
        print(f"Solde actuel : {solde} FCFA.")
        print("9. Accueil \n")
    

# Fonction pour effectuer des transferts
def effectuer_transfert():
    global solde
    
    print('1. Transfert National')
    print("9. Accueil \n")

    choix = saisir_choix(['1', '9'])

    if choix == '1':
        
        numero = saisir_numero()
        montant = saisir_montant("Montant à transferer : ")

        if montant > solde:
            print("Solde insuffisant")
            return
        
        if confirmer(f"Voulez-vous transférer {montant} FCFA au {numero} ?"):

            if verifier_code_secret():
                solde -= montant

                transfert = {
                    "montant": montant,
                    'tel': numero
                }

                historiques_transferts.append(transfert)

                historiques_transferts.append(f"Vous avez transfere {montant}f à {numero}")

                print(f"Transfert réussi. Nouveau solde : {solde} FCFA")
                # essayer de facotirser lcette partie
        else:
            print("Transfert annulé.")

    if choix == '9':
        menu_principale()


# Fonction acheter du credit pour mon numéro
def acheter_credit_mon_numero():
    global solde
    montant = saisir_montant("Montant crédit : ")

    if montant > solde:
        print("Solde insuffisant.")
        return

    if confirmer(f"Acheter {montant} FCFA de crédit ?"):
        if verifier_code_secret():
            solde -= montant
            print(f"Crédit acheté. Nouveau solde : {solde} FCFA")
    else:
        print("Opération annulée")


# Fonction pour acheter credit pour un autre numéro
def acheter_credit_autre_numero():
    global solde
   
    montant = saisir_montant("Montant crédit :")
    numero = saisir_numero()
                
    if montant > solde:
        print('Solde insuffisant')
        return
        
    if confirmer(f"Voulez-vous acheter {montant} de crédit pour le numéro {numero} ?"):
        if verifier_code_secret():

            solde -=montant
            print(f"Vous avez acheté {montant} de credit pour le numéro {numero}. Nouveau solde : {solde} FCFA")
    else:
        print("Opération annulée")


# Fonction pour acheter du credit
def acheter_credit():

    print("Je souhaite acheter du credit téléphonique")
    print('1. Pour mon numéro')
    print('2. Pour un autre numéro Orange, Kirene ou Promobile')
    print("-" * 40)
    print("9. Accueil")

    choix = saisir_choix(['1', '2', '9'])

    if choix == '1':
        acheter_credit_mon_numero()

    elif choix == '2':
        acheter_credit_autre_numero()

    elif choix == '9':
        menu_principale()

# Acheter forfait 100 MO
def forfait_1():
    global solde

    montant = 500
    if montant > solde:
        print("Solde insuffisant.")
        return

    if confirmer(f"Acheter {montant} FCFA de forfait ?"):
        if verifier_code_secret():
            solde -= montant
            print(f"Forfait 100 MO acheté. Nouveau solde : {solde} FCFA")
    else:
        print("Opération annulée")

# Acheter forfait 500 MO
def forfait_2():
    global solde
    montant = 1000
    if montant > solde:
        print("Solde insuffisant.")
        return

    if confirmer(f"Acheter {montant} FCFA de forfait ?"):
        if verifier_code_secret():
            solde -= montant
            print(f"Forfait 500 MO acheté. Nouveau solde : {solde} FCFA")
    else:
        print("Opération annulée")

# Acheter forfait 1 GO
def forfait_3():
    global solde
    montant = 2000
    if montant > solde:
        print("Solde insuffisant.")
        return

    if confirmer(f"Acheter {montant} FCFA de forfait ?"):
        if verifier_code_secret():
            solde -= montant
            print(f"Forfait 1 GO acheté. Nouveau solde : {solde} FCFA")
    else:
        print("Opération annulée")

#Fonction pour acheter un forfait
def acheter_forfait():

    print('1. Pass 100 Mo – 500 F')
    print('2. Pass 500 Mo – 1 000 F')
    print('3. Pass 1 Go – 2 000 F')
    print("-" * 40)
    print("9. Accueil")

    choix = saisir_choix(['1', '2', '3', '9'])

    if choix == '1':
        forfait_1()

    elif choix == '2':
        forfait_2()

    elif choix == '3':
        forfait_3()

    elif choix == '9':
        menu_principale()
    else:
        print("Opération annulée")
      

# Fonction pour afficher les transferts
def afficher_transferts():
    if not historiques_transferts:
        print("Aucun transfert éffectuer")
        return
    
    print("\n Historique des Transferts")

    for i, historique in enumerate(historiques_transferts, 1):
        print(f"{i}. Transfert {historique['montant']} FCFA vers {historique['tel']}")

    print("---")
    print("9. Accueil")

# Fonction pour annuler le dernier transfert
def annuler_dernier_transfert():
    global solde
    if not historiques_transferts:
        print("Aucun transfert. Annulation impossible")
        return
    print("9. Accueil")

    dernier_transfert = historiques_transferts[-1]

    montant = historiques_transferts[-1]['montant']
    numero = historiques_transferts[-1]['tel']

    if(dernier_transfert):
        if confirmer(f"Voulez-vous annuler le dernier transfer : {montant}F vers {numero} ?"):
            if verifier_code_secret():
                solde += montant
                print(f"Transfert annulé : Montant {montant}. Nouveau solde : {solde} FCFA")
    else:
        print("Opération annulée")

# Fonction principale pour demarer le programme
def main():

    code_ussd()

    menu_principale() 
    while True:

        choix = saisir_choix(['1', '2', '3', '4', '5', '6', '9', '0'])

        if choix == '1':
            consuler_solde()

        elif choix == '2':
            effectuer_transfert()

        elif choix == '3':
            acheter_credit()

        elif choix == '4':
            acheter_forfait()
        
        elif choix == '5':
            afficher_transferts()

        elif choix == '6':
            annuler_dernier_transfert()

        elif choix == "9":
            menu_principale()

        elif choix == '0':
            print("Merci d'avoir utilisé Orange Money.")
            break

main()

# expression = r"(77|78)\d{7}"
# numero = input("numero")
# re.fullmatch(expression, numero)

# os est un module qui permet d'interagir avec le systeme
