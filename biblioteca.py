from functools import reduce
from utilizator import Utilizator
from carte import Carte

class Biblioteca:
    def __init__(self):
        self.lista_carti = []
        self.utilizatori = {}

    def adauga_carte(self, carte):
        self.lista_carti.append(carte)

    def adauga_utilizator(self, utilizator):
        self.utilizatori[utilizator.id] = utilizator

    def cauta_dupa_autor(self, autor):
        return list(filter(lambda x: x.autor == autor, self.lista_carti))

    def cauta_dupa_categorie(self, categorie):
        return list(filter(lambda x: x.categorie == categorie, self.lista_carti))

    def cauta_dupa_rating(self, min_rating):
        return list(filter(lambda x: x.medie_rating() >= min_rating, self.lista_carti))

    def statistici_globale(self):
        total_carti = len(self.lista_carti)
        carti_imprumutate = len([carte for carte in self.lista_carti if not carte.disponibila])
        print(f"Total cărți: {total_carti}")
        print(f"Număr de cărți împrumutate: {carti_imprumutate}")

        categorii = [carte.categorie for carte in self.lista_carti]
        cele_mai_populare_categorii = reduce(lambda x, y: x + [y] if y not in x else x, categorii, [])
        print(f"Cele mai populare categorii: {cele_mai_populare_categorii}")

    def __str__(self):
        return f"Biblioteca cu {len(self.lista_carti)} cărți"
