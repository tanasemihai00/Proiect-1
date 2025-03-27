from biblioteca import Biblioteca
from utilizator import Utilizator
from autor import Autor
from carte import Carte

def adauga_rating(carte):
    try:
        rating = int(input("Introdu rating-ul (1-10): "))
        if 1 <= rating <= 10:
            carte.adauga_rating(rating)
            print(f"Rating-ul {rating} a fost adăugat pentru cartea '{carte.titlu}'")
        else:
            print("Rating-ul trebuie să fie între 1 și 10!")
    except ValueError:
        print("Te rugăm să introduci un număr valid!")

def statistici_personale(biblioteca):
    print("\nStatistici personale utilizatori:")
    for utilizator in biblioteca.utilizatori.values():
        print(f"\n{utilizator.nume} (ID: {utilizator.id})")
        print(f"Numărul de cărți împrumutate: {len(utilizator.carti_imprumutate)}")
        if utilizator.carti_imprumutate:
            print("Cărțile împrumutate: ")
            for carte in utilizator.carti_imprumutate:
                print(f" - {carte.titlu}")
        else:
            print("Nu a împrumutat nici o carte.")

def cauta_dupa_autor(biblioteca, autor_nume):
    print(f"\nCăutare cărți după autor: {autor_nume}")
    carti_autor = biblioteca.cauta_dupa_autor(autor_nume)
    if carti_autor:
        for carte in carti_autor:
            print(carte)
    else:
        print("Nu au fost găsite cărți pentru acest autor.")

def cauta_dupa_categorie(biblioteca, categorie):
    print(f"\nCăutare cărți după categorie: {categorie}")
    carti_categorie = [carte for carte in biblioteca.lista_carti if carte.categorie == categorie]
    if carti_categorie:
        for carte in carti_categorie:
            print(carte)
    else:
        print("Nu au fost găsite cărți pentru această categorie.")

def cauta_dupa_an(biblioteca, an):
    print(f"\nCăutare cărți după an: {an}")
    carti_an = [carte for carte in biblioteca.lista_carti if carte.an_publicatie == an]
    if carti_an:
        for carte in carti_an:
            print(carte)
    else:
        print("Nu au fost găsite cărți pentru acest an.")

def statistici_biblioteca(biblioteca):
    print("\nStatistici bibliotecă:")
    for carte in biblioteca.lista_carti:
        rating = carte.medie_rating()
        disponibila = "Disponibilă" if carte.disponibila else "Împrumutată"
        print(f"{carte.titlu} - Autor: {carte.autor.nume}, An: {carte.an_publicatie}, Stoc: {disponibila}, Rating: {rating:.1f}")

def afiseaza_utilizatori(biblioteca):
    print("\nUtilizatori:")
    for utilizator in biblioteca.utilizatori.values():
        print(f"{utilizator.nume} - ID: {utilizator.id}")

def meniu():
    biblioteca = Biblioteca()

    while True:
        print("\nMeniu:")
        print("1. Adaugă utilizator")
        print("2. Adaugă carte")
        print("3. Împrumută carte")
        print("4. Returnează carte")
        print("5. Căutare cărți după autor")
        print("6. Căutare cărți după categorie")
        print("7. Căutare cărți după an")
        print("8. Adaugă rating")
        print("9. Statistici personale utilizatori")
        print("10. Statistici bibliotecă")
        print("11. Afișează utilizatori")
        print("12. Ieșire")
        optiune = input("Alege o opțiune: ")

        if optiune == '1':
            id_utilizator = input("ID utilizator: ")
            nume_utilizator = input("Nume utilizator: ")
            utilizator = Utilizator(id_utilizator, nume_utilizator)
            biblioteca.adauga_utilizator(utilizator)

        elif optiune == '2':
            id_carte = input("ID carte: ")
            titlu = input("Titlu carte: ")
            autor_nume = input("Nume autor: ")
            autor = Autor(id_carte, autor_nume)
            categorie = input("Categorie: ")
            an_publicatie = input("An publicatie: ")
            carte = Carte(id_carte, titlu, autor, categorie, an_publicatie)
            biblioteca.adauga_carte(carte)

        elif optiune == '3':
            id_utilizator = input("ID utilizator: ")
            titlu_carte = input("Titlu carte: ")
            utilizator = biblioteca.utilizatori.get(id_utilizator)
            carte = next((x for x in biblioteca.lista_carti if x.titlu == titlu_carte), None)
            if utilizator and carte:
                utilizator.imprumuta_carte(carte)

        elif optiune == '4':
            id_utilizator = input("ID utilizator: ")
            titlu_carte = input("Titlu carte: ")
            utilizator = biblioteca.utilizatori.get(id_utilizator)
            carte = next((x for x in biblioteca.lista_carti if x.titlu == titlu_carte), None)
            if utilizator and carte:
                utilizator.returneaza_carte(carte)

        elif optiune == '5':
            autor_nume = input("Nume autor: ")
            cauta_dupa_autor(biblioteca, autor_nume)

        elif optiune == '6':
            categorie = input("Categorie: ")
            cauta_dupa_categorie(biblioteca, categorie)

        elif optiune == '7':
            an = input("An publicatie: ")
            cauta_dupa_an(biblioteca, an)

        elif optiune == '8':
            titlu_carte = input("Titlu carte: ")
            carte = next((x for x in biblioteca.lista_carti if x.titlu == titlu_carte), None)
            if carte:
                adauga_rating(carte)

        elif optiune == '9':
            statistici_personale(biblioteca)

        elif optiune == '10':
            statistici_biblioteca(biblioteca)

        elif optiune == '11':
            afiseaza_utilizatori(biblioteca)

        elif optiune == '12':
            break
        else:
            print("Opțiune invalidă.")

meniu()
