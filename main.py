from biblioteca import Biblioteca
from utilizator import Utilizator
from autor import Autor
from carte import Carte

def meniu():
    biblioteca = Biblioteca()

    while True:
        print("\nMeniu:")
        print("1. Adaugă utilizator")
        print("2. Adaugă carte")
        print("3. Împrumută carte")
        print("4. Returnează carte")
        print("5. Căutare după autor")
        print("6. Statistici globale")
        print("7. Ieșire")
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
            categorie = input("Categorie: ")
            an_publicatie = input("An publicatie: ")
            autor = Autor(id_carte, autor_nume)
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
            autor = Autor(0, autor_nume)
            carti_autor = biblioteca.cauta_dupa_autor(autor)
            for carte in carti_autor:
                print(carte)

        elif optiune == '6':
            biblioteca.statistici_globale()

        elif optiune == '7':
            break
        else:
            print("Opțiune invalidă.")

meniu()
