import pygame

class Ligne:

    nb = 0
    def __init__(self,  pointProd,pointCons):
        self.transit = pointProd.puissance
        self.transitMax = 50
        self.pointProd = pointProd
        self.pointCons = pointCons
        Ligne.nb += 1
        
        
    def augmenter(self):
        if self.transit + 10 > self.transitMax:
            return "Vous ne pouvez pas dépasser la capacité de transit maximum"
        else:
            self.transit = self.transit + 10

    def reduire(self, value):
        if self.transit - 10 <= 0:
            return "Vous ne pouvez pas avoir un transit nul"
        else:
            self.transit = self.transit - 10
            
            
     
    def afficher(self,fenetre,x,y):
        myfont = pygame.font.SysFont('Comic Sans MS', 12)
      
          
        texte = str(self.pointProd)+" et "+ str(self.pointCons)
        texte = myfont.render("reseau : "+str(self.pointProd.name)+" et "+str(self.pointCons.name), True, (0, 0, 0))
        fenetre.blit(texte,(x,y))
     
  

                
        texte = myfont.render("transit = "+ str(self.transit) +"MW", True, (0, 0, 0))
        fenetre.blit(texte,(x+10,y+20))