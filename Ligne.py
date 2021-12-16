class Ligne:

    def __init__(self, transit, transitMax):
        self.transit = transit
        self.transitMax = transitMax

    def augmenter(self, value):
        if self.transit + value > self.transitMax:
            return "Vous ne pouvez pas dépasser la capacité de transit maximum"
        else:
            self.transit = self.transit + value

    def reduire(self, value):
        if self.transit - value <= 0:
            return "Vous ne pouvez pas avoir un transit nul"
        else:
            self.transit = self.transit - value