from Point import Point


class PointProduction(Point):

    def __init__(self, name, lieu, groupes):
        self.name = name
        self.lieu = lieu
        self.groupes = groupes
        self.puissance = 0;

    def production(self):
        for i in self.groupes:
            self.puissance = self.puissance + i.puissance