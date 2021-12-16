from GroupeNonRenouvelable import GroupeNonRenouvelable
from PointConsommation import PointConsommation
from PointProduction import PointProduction

groupe1 = GroupeNonRenouvelable("groupe1", 30, 20, 100)
groupe2 = GroupeNonRenouvelable("groupe2", 50, 10, 240)
conso = PointConsommation("ajaccio", 210)
prod = PointProduction("prod", "ajaccio", [groupe1, groupe2])
prod.production()
print(prod.puissance)
groupe2.ajouterPuissance(60)
prod.production()
print(prod.puissance)
