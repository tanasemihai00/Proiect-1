from carte import Carte

class Autor:
    def __init__(self, id_autor, nume):
        self.id_autor = id_autor
        self.nume = nume
        self.carti_scrise = []

    def adauga_carte(self, carte):
        self.carti_scrise.append(carte)

    def __str__(self):
        return f"Autor {self.nume} (ID: {self.id_autor})"
