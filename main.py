from GroupeNonRenouvelable import GroupeNonRenouvelable
from Ligne import Ligne
from PointConsommation import PointConsommation
from PointProduction import PointProduction

#groupe1 = GroupeNonRenouvelable("groupe1", 30, 20, 100)
#groupe2 = GroupeNonRenouvelable("groupe2", 50, 10, 240)
ligne1 = Ligne(40, 70)
ligne2 = Ligne(40, 70)
conso = PointConsommation("ajaccio", 210, "conso1", [])
print(conso.consommationTotale())
conso.lignes = [ligne1, ligne2]
print(conso.consommationTotale())
#prod = PointProduction("prod", "ajaccio", [groupe1, groupe2], 3, 6, "truc", "img")
#prod.production()
#print(prod.puissance)
#groupe2.ajouterPuissance(60)
#prod.production()
#print(prod.puissance)

