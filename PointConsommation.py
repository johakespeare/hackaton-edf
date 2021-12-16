from Point import Point
import pygame

class PointConsommation(Point):

    def __init__(self, name, lieu,fenetre,x,y):
        self.name = name
        self.lieu = lieu
  
        self.fenetre = fenetre
        image = pygame.image.load("point.jpg").convert_alpha()
        self.image = pygame.transform.scale(image, (30,30))
        self.x = x
        self.y = y

    def dessiner(self):
        self.fenetre.blit(self.image, (self.x,self.y))
        self.boutonClass = pygame.Rect(self.x, self.y, 30, 30)
        
    def setPuissance(self,p):
        self.puissance = p