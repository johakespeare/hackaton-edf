from Point import Point

import pygame
from Eolienne import Eolienne


class PointProduction(Point):
    
    nb = 0
    def __init__(self, name, lieu, groupes, x, y, fenetre, pathImage,renouvelable):
        self.x=x
        self.y=y
        self.fenetre=fenetre
        self.name = name
        self.lieu = lieu
        self.groupes = groupes
        self.puissance = 0;
        image = pygame.image.load(pathImage).convert_alpha()
        self.image = pygame.transform.scale(image, (30,30))
        PointProduction.nb +=1
        self.name = "point de production "+str(PointProduction.nb)
        self.puissance = 40
        self.puissanceMin = 0
        self.puissanceMax = 150
        self.renouvelable = renouvelable
        self.allumer = True
        
      
    def ajouterPuissance(self):
        if self.puissance + 10 > self.puissanceMax:
            return "Vous ne pouvez pas dépasser la puissance maximale"
        else:
            self.puissance = self.puissance + 10


    def baisserPuissance(self):
        if self.puissance - 10 < self.puissanceMin:
            return "Vous ne pouvez pas être en dessous de la puissance minimale"
        else:
            self.puissance = self.puissance - 10

    def arreter(self):
        
        self.value = self.puissance
        self.puissance = 0
        self.allumer = False

    def demarrer(self):
        self.puissance = self.value
        self.allumer = True

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
          
        if not self.renouvelable :
            image_plus = pygame.image.load("plus.png").convert_alpha()
            image_plus = pygame.transform.scale(image_plus, (20,20))
            
            self.boutonPlus = pygame.Rect(x + 130, y, 20, 20)
            self.fenetre.blit(image_plus,(x + 130, y))
            
            image_moins = pygame.image.load("moins.png").convert_alpha()
            image_moins = pygame.transform.scale(image_moins, (20,20))
            
            self.boutonMoins = pygame.Rect(x + 130+ 30 , y, 20, 20)
            self.fenetre.blit(image_moins,(x + 130 + 30, y))
            
           
            boutonOnOffe = pygame.Rect(x + 130 + 60, y, 20, 20)  
            if self.allumer :
                self.boutonOnOff = pygame.draw.rect(self.fenetre, [0, 255, 0], boutonOnOffe)
            else :
                self.boutonOnOff = pygame.draw.rect(self.fenetre, [255, 0, 0], boutonOnOffe)
                
                
        texte = myfont.render("capacite = "+ str(self.puissance), True, (0, 0, 0))
        self.fenetre.blit(texte,(x+10,y+10))