from Point import Point

import pygame
from Eolienne import Eolienne


class PointProduction(Point):

    def __init__(self, name, lieu, groupes, x, y, fenetre, pathImage):
        self.x=x
        self.y=y
        self.fenetre=fenetre
        self.name = name
        self.lieu = lieu
        self.groupes = groupes
        self.puissance = 0;
        image = pygame.image.load(pathImage).convert_alpha()
        self.image = pygame.transform.scale(image, (30,30))
        self.name = "point de production "+str(Eolienne.nb)

    def production(self):
        for i in self.groupes:
            self.puissance = self.puissance + i.puissance
            
    def dessiner(self):
        self.fenetre.blit(self.image, (self.x,self.y))
        self.boutonClass = pygame.Rect(self.x, self.y, 30, 30)
        

    
    def afficher(self,x,y):
        myfont = pygame.font.SysFont('Comic Sans MS', 12)
        texte = myfont.render(self.name, True, (0, 0, 0))
        self.fenetre.blit(texte,(x,y))
          
        
        image_plus = pygame.image.load("plus.png").convert_alpha()
        image_plus = pygame.transform.scale(image_plus, (20,20))
        
        self.boutonPlus = pygame.Rect(x + 100, y, 20, 20)
        self.fenetre.blit(image_plus,(x + 100, y))
        
        image_moins = pygame.image.load("moins.png").convert_alpha()
        image_moins = pygame.transform.scale(image_moins, (20,20))
        
        self.boutonMoins = pygame.Rect(x + 100 + 30 , y, 20, 20)
        self.fenetre.blit(image_moins,(x + 100 + 30, y))
        
        image_onoff = pygame.image.load("moins.png").convert_alpha()
        image_onoff = pygame.transform.scale(image_onoff, (20,20))
        
        self.boutonOnOff = pygame.Rect(x + 100 + 60, y, 20, 20)
        self.fenetre.blit(image_onoff,(x + 100 + 60, y))