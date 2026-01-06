depenses = []

# Fonction pour ajouter une depense
def ajouter_depense():
    montant = float(input("Entrez le montant de la dépense : "))
    categorie = input("Entrez la catégorie de la dépense : ")
    description = input("Entrez une description de la dépense : ")

    depense = {
        "montant": montant,
        "categorie": categorie,
        "description": description
    }
    
    depenses.append(depense)
    print("Dépense ajoutée avec succès !")

# Fonction pour afficher les depense
def afficher_depenses():
    if not depenses:
        print("Aucune dépense enregistrée.")
        return
    
    print("\nDépenses enregistrées :")
    for depense in depenses:
        print(f"Montant: {depense['montant']} | Catégorie: {depense['categorie']} | Description: {depense['description']}")

# Fonction pour calculer le total des depenses
def total_depenses():
    total = 0
    for depense in depenses:
       total += depense['montant']
    print(f"Total de depense {total} FCFA \n")

# Fonction pour afficher les depenses par categorie
def depenses_par_categorie():
    if not depenses:
        print("Aucune dépense enregistrée.\n")
        return

    categorie_recherche = input("Entrez la catégorie : ")
    trouve = False

    print(f"\n Dépenses pour la catégorie '{categorie_recherche}' :")
    for depense in depenses:
        if depense["categorie"].lower() == categorie_recherche.lower():
            print(f"- {depense['description']} : {depense['montant']} FCFA")
            trouve = True

    if not trouve:
        print("Aucune dépense trouvée pour cette catégorie.")
    print()

# Fonction pour afficher l menu interactif
def menu():
    while True:
        print("\n===========  Menu =============")
        print("1. Ajouter une dépense")
        print("2. Afficher les dépenses")
        print("3. Afficher le total des dépenses")
        print("4. Afficher les dépenses par catégorie")
        print("5. Quitter")
        
        choix = input("Choisissez une option : ")
        
        if choix == '1':
            ajouter_depense()
        elif choix == '2':
            afficher_depenses()
        elif choix == '3':
            total_depenses()
        elif choix == '4':
            depenses_par_categorie()
        elif choix == '5':
            print("Au revoir!")
            break 
        else:
            print("Option invalide, veuillez réessayer.")
menu()