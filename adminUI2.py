# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 10:34:33 2021

@author: johan
"""

from Eolienne import Eolienne 
import pygame
from pygame.locals import *
from PointProduction import *

from Jeu import *

"""CONSTANTES"""

HAUTEUR = 800
LARGEUR = 1400
ORANGE = (255 , 127 , 0)
GRIS = (245,245,245)
BLANC = (245,245,245)
"""VARIABLES """
 
points = []
reseau = []

pygame.init()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
myfont = pygame.font.SysFont('Comic Sans MS', 12)
fenetre.fill((255,255,255))

"""AFFICHAGE"""

#milieu
corse = pygame.image.load("corse.png").convert()
corse = pygame.transform.scale(corse, (700,700))
fenetre.blit(corse,(LARGEUR/2-350,HAUTEUR/2-350))


#gauche


    
def dessinerLabelGauche():
    labelGauche = pygame.Rect(0, 0, LARGEUR/3 -250, HAUTEUR)
    listePoints = pygame.Rect(10, 0, LARGEUR/3 -250, HAUTEUR/2)
    listeReseaux = pygame.Rect(10, HAUTEUR/2, LARGEUR/3 -250, HAUTEUR/2)
    

   
    pygame.draw.rect(fenetre, BLANC, listePoints)  
    pygame.draw.rect(fenetre, BLANC, listeReseaux)
    nomListePoints = myfont.render('Liste des points de production', True, (0, 0, 0))
    fenetre.blit(nomListePoints,(5,0))
    nomListeReseaux = myfont.render('Liste des réseaux ', True, (0, 0, 0))
    fenetre.blit(nomListeReseaux,(5,HAUTEUR/2 + 5))

dessinerLabelGauche()

#droit
labelDroit =  pygame.Rect(LARGEUR - LARGEUR/3 ,0, LARGEUR, HAUTEUR) 
graph1 = pygame.Rect(LARGEUR+5 - LARGEUR/3,0, LARGEUR/3 - 10, HAUTEUR/5) 
graph2 = pygame.Rect(LARGEUR+5 - LARGEUR/3,HAUTEUR/3, LARGEUR/3 - 10, HAUTEUR/5)
vitesse = pygame.Rect(LARGEUR+5 - LARGEUR/3,HAUTEUR-HAUTEUR/3, LARGEUR/3 - 10, HAUTEUR/5)
boutonStart = pygame.Rect(LARGEUR+5 - LARGEUR/3 + 10, HAUTEUR-HAUTEUR/3 + 5, 50, 25)
boutonArret = pygame.Rect(LARGEUR+5 - LARGEUR/3 + 55 + 10, HAUTEUR-HAUTEUR/3 + 5, 50, 25)
sliderTemps = pygame.Rect(LARGEUR+5 - LARGEUR/3 + 10, HAUTEUR-HAUTEUR/3 + 55, 25, 25)


pygame.draw.rect(fenetre, GRIS, labelDroit)  
pygame.draw.rect(fenetre, ORANGE, graph1)  
pygame.draw.rect(fenetre, ORANGE, graph2) 
pygame.draw.rect(fenetre, GRIS, vitesse )  
pygame.draw.rect(fenetre, [210, 210, 210], boutonStart, border_radius=7)  
pygame.draw.rect(fenetre, [210, 210, 210], boutonArret, border_radius=7) 
pygame.draw.rect(fenetre, [255, 0, 0], sliderTemps) 

texteStart = myfont.render('Start', True, (0, 0, 0))
fenetre.blit(texteStart,(LARGEUR+5 - LARGEUR/3 + 10 + 10, HAUTEUR-HAUTEUR/3 + 5 +2))
textePause = myfont.render('Pause', True, (0, 0, 0))
fenetre.blit(textePause,(LARGEUR+5 - LARGEUR/3 + 55 + 10 + 10, HAUTEUR-HAUTEUR/3 + 5 + 2))

#afficherOutils

LARGEUR_OUTILS = 230
OUTILS_X = LARGEUR/3 -250 + 20

outils =  pygame.Rect(OUTILS_X  ,0, LARGEUR_OUTILS, 50) 
pygame.draw.rect(fenetre, GRIS, outils)  


image_eolienne = pygame.image.load("eolienne.png").convert_alpha()
image_eolienne = pygame.transform.scale(image_eolienne, (30,30))
boutonEolienne = pygame.Rect(OUTILS_X + 5 , 10 , 30,30)
 
fenetre.blit(image_eolienne , (OUTILS_X + 5 ,10))


image_thermique = pygame.image.load("thermo.png").convert_alpha()
image_thermique = pygame.transform.scale(image_thermique, (30,30))
boutonThermique = pygame.Rect(OUTILS_X + 40 , 10 , 30,30) 

fenetre.blit(image_thermique, (OUTILS_X+40,10))


image_photo = pygame.image.load("solaire.png").convert_alpha()
image_photo = pygame.transform.scale(image_photo, (30,30))
boutonPhoto = pygame.Rect(OUTILS_X + 75 , 10 , 30,30)

fenetre.blit(image_photo, (OUTILS_X+75,10))


image_hydrau = pygame.image.load("hydro.png").convert_alpha()
image_hydrau = pygame.transform.scale(image_hydrau, (30,30))
boutonHydrau = pygame.Rect(OUTILS_X + 110 , 10 , 30,30)

fenetre.blit(image_hydrau , (OUTILS_X+110,10))

image_biogaz = pygame.image.load("biogaz.png").convert_alpha()
image_biogaz = pygame.transform.scale(image_biogaz, (30,30))
boutonBiogaz = pygame.Rect(OUTILS_X + 145 , 10 , 30,30)

fenetre.blit(image_biogaz,(OUTILS_X+145,10))
    
image_tracer = pygame.image.load("biogaz.png").convert_alpha()
image_tracer = pygame.transform.scale(image_tracer, (30,30))
boutonTracer = pygame.Rect(OUTILS_X + 180 , 10 , 30,30)

fenetre.blit(image_tracer,(OUTILS_X+180,10))
    

            
    

def dessinerEolienne(fenetre,x,y):
    #image = pygame.image.load("eolienne.png").convert()
    #image = pygame.transform.scale(image, (30,30))
    #fenetre.blit(image, (x,y))
    
    eolienne = PointProduction("nom","lieu",None,x,y,fenetre,"eolienne.png")
    eolienne.dessiner()
    points.append(eolienne)
    
    
def dessinerThermique(fenetre,x,y):
    thermique = PointProduction("nom","lieu",None,x,y,fenetre,"thermo.png")
    thermique.dessiner()
    points.append(thermique)
    
def dessinerBiogaz(fenetre,x,y):
    biogaz = PointProduction("nom","lieu",None,x,y,fenetre,"biogaz.png")
    biogaz.dessiner()
    points.append(biogaz)

def dessinerPhoto(fenetre,x,y):
    eolienne = PointProduction("nom","lieu",None,x,y,fenetre,"solaire.png")
    eolienne.dessiner()
    points.append(eolienne)

def dessinerHydro(fenetre,x,y):
    eolienne = PointProduction("nom","lieu",None,x,y,fenetre,"hydro.png")
    eolienne.dessiner()
    points.append(eolienne)   



def drawCircle( fenetre, x, y ): 
  pygame.draw.circle( fenetre , ORANGE , ( x, y ), 5 )
  
def drawLine( fenetre,x,y,x2,y2):
    pygame.draw.line( fenetre , ORANGE , [x, y], [x2,y2], 5 )
    
def afficherReseaux():
    x = 0
    y = HAUTEUR / 2 + 30
    for lien in reseau :
        texte = str(lien[0].name)+" et "+ str(lien[1].name)
        texte = myfont.render("reseau : "+ str(texte), True, (0, 0, 0))
        fenetre.blit(texte,(x,y))
        y += 30

def afficherPoints():
    x = 0
    y = 30
    for point in points :         
        point.afficher(x,y)       
    
        
        y += 30



def afficherGraphes():
    pass

  
    
    
#BOUCLE INFINIE
continuer = 1
isPressed = False
bouton = None
couple = []

while continuer:
     for event in pygame.event.get():
            print(bouton)
            
            for point in points :
                 if point.boutonPlus.collidepoint(pygame.mouse.get_pos()) and isPressed==True:
                    points.remove(point)   
         
                         
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if boutonEolienne.collidepoint(pygame.mouse.get_pos()) and isPressed==True:
                    bouton="eolienne"
            if boutonThermique.collidepoint(pygame.mouse.get_pos()) and isPressed==True:
                    bouton="thermique"
            if boutonPhoto.collidepoint(pygame.mouse.get_pos()) and isPressed==True:
                    bouton="photo"
            if boutonHydrau.collidepoint(pygame.mouse.get_pos()) and isPressed==True:
                    bouton="hydrau"
            if boutonBiogaz.collidepoint(pygame.mouse.get_pos()) and isPressed==True:
                    bouton="biogaz"
            if boutonTracer.collidepoint(pygame.mouse.get_pos()) and isPressed==True:
                    bouton="tracer"
                    
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
               isPressed = True
               ( x, y ) = pygame.mouse.get_pos()  
               
               if(x<LARGEUR-LARGEUR/3) and(x>LARGEUR/3 - 250) and(y> 50) and (y<HAUTEUR-50):
                   if bouton=="eolienne":    
                        dessinerEolienne(fenetre,x,y)                    
                   elif bouton=="thermique":    
                        dessinerThermique(fenetre,x,y)
                   elif bouton=="photo":    
                        dessinerPhoto(fenetre,x,y)
                   elif bouton=="hydrau":    
                        dessinerHydro(fenetre,x,y)
                   elif bouton=="biogaz":    
                        dessinerBiogaz(fenetre,x,y)
                   elif bouton=="tracer":    
                        
                        for point in points:
                            if point.boutonClass.collidepoint(pygame.mouse.get_pos()) and isPressed==True :
                                couple.append(point)
                                if(len(couple)==2):
                                     pygame.draw.line( fenetre , ORANGE , [couple[0].x, couple[0].y], [couple[1].x,couple[1].y], 5 )
                                     reseau.append((couple[0],couple[1]))
                                     couple.clear()
                                     
               
  
            elif event.type == pygame.MOUSEBUTTONUP:
                isPressed = False
              
                
          
               
          
           
                
            pygame.display.flip()  
            dessinerLabelGauche()
            afficherPoints()
            afficherReseaux()
        
            
              