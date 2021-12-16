from Eolienne import Eolienne 
import pygame
from pygame.locals import *

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


    

    
    
def afficherReseaux():
    x = 0
    y = HAUTEUR / 2 + 30
    for lien in reseau :
        texte = str(lien[0].name)+" et "+ str(lien[1].name)
        texte = myfont.render("reseau : "+ str(texte), True, (0, 0, 0))
        fenetre.blit(texte,(x,y))

def afficherPoints():
    x = 0
    y = 30
    for point in points :         
        point.afficher(x,y) 
        

        y += 30



  
    
    
#BOUCLE INFINIE
continuer = 1
isPressed = False
bouton = None


while continuer:
     for event in pygame.event.get():
            print(bouton)
            
            for point in points :
                 if point.boutonPlus.collidepoint(pygame.mouse.get_pos()) and isPressed==True:
                    points.remove(point)   
         
                         
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
            if boutonStart.collidepoint(pygame.mouse.get_pos()) and isPressed==True:
                    print("start")
            if boutonArret.collidepoint(pygame.mouse.get_pos()) and isPressed==True:
                    print("arret")
            
            
            if event.type == pygame.MOUSEBUTTONDOWN:
               isPressed = True               
               
  
            elif event.type == pygame.MOUSEBUTTONUP:
                isPressed = False
              
                
          
               
          
           
                
            pygame.display.flip()  
            dessinerLabelGauche()
            afficherPoints()
            afficherReseaux()
        
            