class Carte:
    def __init__(self, id_carte, titlu, autor, categorie, an_publicatie):
        self.id_carte = id_carte
        self.titlu = titlu
        self.autor = autor
        self.categorie = categorie
        self.an_publicatie = an_publicatie
        self.disponibila = True
        self.rating = []

    def adauga_rating(self, nota):
        self.rating.append(nota)
        print(f"Rating-ul pentru cartea '{self.titlu}' a fost actualizat.")

    def medie_rating(self):
        if self.rating:
            return sum(self.rating) / len(self.rating)
        return 0

    def __str__(self):
        return f"Carte '{self.titlu}' (ID: {self.id_carte})"
