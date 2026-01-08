# Solde initial au demarage
solde = 10000
float(solde)

CODE_SECRET = 9900

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
    print("0. Quitter")
    print("-" * 40, "\n")


# Fonction pour verifier le code USSD
def code_ussd():

    while True:
        code = input("Composer votre USSD (ex: #144#) : ").strip()

        if code.startswith('#') and code.endswith('#') and code == '#144#':
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
        numero = input("Numéro de téléphone : ").strip()
        if numero.isdigit() and len(numero) in [9, 10]:
            return numero
        else:
            print("Numéro invalide. Exemple : 771234567")


# Fonction pour consuler le solde
def consuler_solde():
    global solde
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
                print(f"Transfert réussi. Nouveau solde : {solde} FCFA")
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
    print("---------------------------------")
    print("9. Accueil")

    choix = saisir_choix(['1', '2', '9'])

    if choix == '1':
        acheter_credit_mon_numero()

    elif choix == '2':
        acheter_credit_autre_numero()

    elif choix == '9':
        menu_principale()


# Fonction principale pour demarer le programme
def main():

    code_ussd()

    menu_principale()

    while True:

        choix = saisir_choix(['1', '2', '3', '9', '0'])

        if choix == '1':
            consuler_solde()

        elif choix == '2':
            effectuer_transfert()

        elif choix == '3':
            acheter_credit()

        elif choix == "9":
            menu_principale()

        elif choix == '0':
            print("Merci d'avoir utilisé Orange Money.")
            break

main()