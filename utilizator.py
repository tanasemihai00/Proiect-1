from persoana import Persoana
from carte import Carte


class Utilizator(Persoana):
    def __init__(self, id, nume):
        super().__init__(id, nume)
        self.carti_imprumutate = []
        self.istoric_imprumuturi = set()

    def imprumuta_carte(self, carte):
        if carte.disponibila:
            self.carti_imprumutate.append(carte)
            self.istoric_imprumuturi.add(carte.titlu)
            carte.disponibila = False
            print(f"Cartea '{carte.titlu}' a fost împrumutată de {self.nume}.")
        else:
            print(f"Cartea '{carte.titlu}' nu este disponibilă pentru împrumut.")

    def returneaza_carte(self, carte):
        if carte in self.carti_imprumutate:
            self.carti_imprumutate.remove(carte)
            self.istoric_imprumuturi.add(carte.titlu)
            carte.disponibila = True
            print(f"Cartea '{carte.titlu}' a fost returnată de {self.nume}.")
        else:
            print(f"Nu ai împrumutat cartea '{carte.titlu}'.")

    def statistici_personale(self):
        print(f"{self.nume} a împrumutat {len(self.carti_imprumutate)} cărți.")

    def __str__(self):
        return f"Utilizator {self.nume} (ID: {self.id})"
