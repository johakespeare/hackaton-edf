# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 12:50:39 2021

@author: johan
"""
import pygame
from pygame.locals import *



class Eolienne:
    
    nb = 0
    
    def __init__(self,x,y,fenetre):
        self.x = x
        self.y = y 
        self.fenetre = fenetre
        
        
     
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
        
    
        
        
        
        
        
        
        
        
        