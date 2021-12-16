from Groupe import Groupe


class GroupeNonRenouvelable(Groupe):

    def __init__(self, name, puissance, puissanceMin, puissanceMax):
        self.name = name
        self.puissance = puissance
        self.puissanceMin = puissanceMin
        self.puissanceMax = puissanceMax

    def ajouterPuissance(self, ajout):
        if self.puissance + ajout > self.puissanceMax:
            return "Vous ne pouvez pas dépasser la puissance maximale"
        else:
            self.puissance = self.puissance + ajout


    def baisserPuissance(self, retrait):
        if self.puissance - retrait > self.puissanceMin:
            return "Vous ne pouvez pas être en dessous de la puissance minimale"
        else:
            self.puissance = self.puissance - retrait

    def arreter(self):
        self.puissance = 0

    def demarrer(self, value):
        self.puissance = value
