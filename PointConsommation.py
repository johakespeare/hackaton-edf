from Point import Point


class PointConsommation(Point):

    def __init__(self, name, puissance, lieu, lignes):
        self.name = name
        self.lieu = lieu
        self.puissance = puissance
        self.lignes = lignes

    def consommationTotale(self):
        if not self.lignes:
            return 0
        else:
            return sum(ligne.transit for ligne in self.lignes)