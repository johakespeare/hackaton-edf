# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 10:34:33 2021

@author: johan
"""

from Eolienne import Eolienne 
import pygame
from pygame.locals import *
from PointProduction import *
from PointConsommation import*

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
points2 = []

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
    listePoints = pygame.Rect(0, 0, LARGEUR/3 -250, HAUTEUR/2)
    listeReseaux = pygame.Rect(0, HAUTEUR/2, LARGEUR/3 -250, HAUTEUR/2)
    

    pygame.draw.rect(fenetre, BLANC, listePoints)  
    pygame.draw.rect(fenetre, BLANC, listeReseaux)
    nomListePoints = myfont.render('Liste des points de production', True, (0, 0, 0))
    fenetre.blit(nomListePoints,(5,0))
    nomListeReseaux = myfont.render('Liste des réseaux ', True, (0, 0, 0))
    fenetre.blit(nomListeReseaux,(5,HAUTEUR/2 + 5))
    


dessinerLabelGauche()
     
def afficherCourbeConso():
     surface = pygame.Surface((LARGEUR/3 - 10 -200, HAUTEUR/3 - 50))
     surface.fill((255,255,255))
     c =loadCourbe(49,98)
     x = 1
     for i in range(0,len(c)-1) :
       
         y = HAUTEUR/5 - float(c[i]) + 150
         y2 = HAUTEUR/5 - float(c[i+1]) + 150
         pygame.draw.line( surface , (0,0,0) , [x,y], [x+5,y2], 2)
         x+=5
    
     fenetre.blit(surface,(LARGEUR+5 - LARGEUR/3 + 10,10))
     texteSave = myfont.render('indication : Courbe de consommation (mW)', True, (0, 0, 0))
     fenetre.blit(texteSave,(LARGEUR+5 - LARGEUR/3 + 10,HAUTEUR/3 - 50 + 10))
     
    
     
def afficherCourbeEolienne():
     surface = pygame.Surface((LARGEUR/3 - 10 -200, HAUTEUR/3 - 50 ))
     surface.fill((255,255,255))
     c = loadCourbe2(49,98)
     x = 1
     for i in range(0,len(c)-1) :
       
         y = HAUTEUR/5 - float(c[i]) 
         y2 = HAUTEUR/5 - float(c[i+1]) 
         pygame.draw.line( surface , (0,0,0) , [x,y], [x+5,y2], 2)
         x+=5
    
     fenetre.blit(surface,(LARGEUR+5 - LARGEUR/3 +10,HAUTEUR/2 -150))
     texteSave = myfont.render('indication : Courbe ENR (mW)', True, (0, 0, 0))
     fenetre.blit(texteSave,(LARGEUR+5 - LARGEUR/3 +10,(HAUTEUR/3 - 50)*2 + 40))
     
    
    
labelDroit =  pygame.Rect(LARGEUR - LARGEUR/3 ,0, LARGEUR, HAUTEUR) 


vitesse = pygame.Rect(LARGEUR+5 - LARGEUR/3,HAUTEUR-HAUTEUR/3, LARGEUR/3 - 10, HAUTEUR/5)
boutonStart = pygame.Rect(LARGEUR+5 - LARGEUR/3 + 10, HAUTEUR-HAUTEUR/3 + 5, 50, 25)
boutonArret = pygame.Rect(LARGEUR+5 - LARGEUR/3 + 55 + 10, HAUTEUR-HAUTEUR/3 + 5, 50, 25)
sliderTemps = pygame.Rect(LARGEUR+5 - LARGEUR/3 + 10, HAUTEUR-HAUTEUR/3 + 55, 25, 25)


pygame.draw.rect(fenetre, GRIS, labelDroit)  
 

pygame.draw.rect(fenetre, GRIS, vitesse )  
pygame.draw.rect(fenetre, [210, 210, 210], boutonStart, border_radius=7)  
pygame.draw.rect(fenetre, [210, 210, 210], boutonArret, border_radius=7) 
pygame.draw.rect(fenetre, [255, 0, 0], sliderTemps) 

texteStart = myfont.render('Start', True, (0, 0, 0))
fenetre.blit(texteStart,(LARGEUR+5 - LARGEUR/3 + 10 + 10, HAUTEUR-HAUTEUR/3 + 5 +2))
textePause = myfont.render('Pause', True, (0, 0, 0))
fenetre.blit(textePause,(LARGEUR+5 - LARGEUR/3 + 55 + 10 + 10, HAUTEUR-HAUTEUR/3 + 5 + 2))
afficherCourbeConso() 
afficherCourbeEolienne() 

puissanceTotale= myfont.render('puissanceTotale :'+str(0), True, (0, 0, 0))
fenetre.blit(puissanceTotale,(LARGEUR+5 - LARGEUR/3 +10,(HAUTEUR/3 - 50)*2 + 40 + 150))
 

   
    
#droit




#afficherOutils

LARGEUR_OUTILS = 240
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
    

image_consom = pygame.image.load("point.jpg").convert_alpha()
image_consom = pygame.transform.scale(image_consom, (30,30))
boutonConsom = pygame.Rect(OUTILS_X + 210 , 10 , 30,30)

fenetre.blit(image_consom,(OUTILS_X+ 210,10))            
   

boutonSave = pygame.Rect(OUTILS_X+ 210 + 50,10, 50, 25)
pygame.draw.rect(fenetre, [210, 210, 210], boutonSave, border_radius=7) 
texteSave = myfont.render('Save', True, (0, 0, 0))
fenetre.blit(texteSave,(OUTILS_X+ 210+50,10))




  




def dessinerEolienne(fenetre,x,y):
    #image = pygame.image.load("eolienne.png").convert()
    #image = pygame.transform.scale(image, (30,30))
    #fenetre.blit(image, (x,y))
    
    eolienne = PointProduction("nom","lieu",None,x,y,fenetre,"eolienne.png",True)
    eolienne.dessiner()
    points.append(eolienne)
    
    
def dessinerThermique(fenetre,x,y):
    thermique = PointProduction("nom","lieu",None,x,y,fenetre,"thermo.png",False)
    thermique.dessiner()
    points.append(thermique)
    
def dessinerBiogaz(fenetre,x,y):
    biogaz = PointProduction("nom","lieu",None,x,y,fenetre,"biogaz.png",False)
    biogaz.dessiner()
    points.append(biogaz)

def dessinerPhoto(fenetre,x,y):
    eolienne = PointProduction("nom","lieu",None,x,y,fenetre,"solaire.png",True)
    eolienne.dessiner()
    points.append(eolienne)

def dessinerHydro(fenetre,x,y):
    eolienne = PointProduction("nom","lieu",None,x,y,fenetre,"hydro.png",True)
    eolienne.dessiner()
    points.append(eolienne)   




def dessinerConsom(fenetre,x,y):
    eolienne = PointConsommation("nom","lieu",fenetre,x,y)
    eolienne.dessiner()
    points2.append(eolienne)

    
    
def drawCircle( fenetre, x, y ): 
    pygame.draw.circle( fenetre , ORANGE , ( x, y ), 5 )
  
def drawLine( fenetre,x,y,x2,y2):
    pygame.draw.line( fenetre , ORANGE , [x, y], [x2,y2], 5 )
    
def afficherReseaux():
    x = 0
    y = HAUTEUR / 2 + 30
    for lien in reseau :
        texte = str(lien[0].name)+" et "+ str(lien[1].name)
        texte = myfont.render("reseau : "+str(lien[0].name), True, (0, 0, 0))
        fenetre.blit(texte,(x,y))
        texte = myfont.render("            "+str(lien[1].name), True, (0, 0, 0))
        fenetre.blit(texte,(x,y+15))
        y += 30

def afficherPoints():
    x = 0
    y = 30
    for point in points :         
        point.afficher(x,y)       
    
        
        y += 40


def updateEtat():
    for i in range(b-a-1):
        global step,consoGlobale
        time.sleep((pasTemps/facteurTemps))
        step+=1

        consoGlobale=float(courbeENR[step])
        ProdRenouvelable=float(courbeConso[step]) 
        
        for e in points2:
            e.puissance=e.puissance*consoGlobale/100
            

    
#BOUCLE INFINIE
courbeENR=[]
courbeConso =[]
with open('courbeConso.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count=0
    for row in csv_reader:
        if (line_count>48 and line_count<=97):
            courbeENR.append(row[2])
            courbeConso.append(row[1])
        line_count+=1
        
        
        
consoGlobale = 0      
continuer = 1
isPressed = False
bouton = None
couple = []
step = 0

while continuer:
     for event in pygame.event.get():
            
            for point in points :
                 if not point.renouvelable :
                     if point.boutonPlus.collidepoint(pygame.mouse.get_pos()) and isPressed==True:
                        point.ajouterPuissance()
                     if point.boutonMoins.collidepoint(pygame.mouse.get_pos()) and isPressed==True:
                        point.baisserPuissance()
                        
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
            if boutonConsom.collidepoint(pygame.mouse.get_pos()) and isPressed==True:
                    bouton="consom"
            if boutonStart.collidepoint(pygame.mouse.get_pos()) and isPressed==True:
                    for p in points2:
                        p.setPuissance(float(courbeMain[step][1])/len(points2))
                    thread=threading.Thread(target=updateEtat)
                    thread.start()
                    
            
                    
                    
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
                   elif bouton=="consom":    
                        dessinerConsom(fenetre,x,y)
                   elif bouton=="tracer":    
                    
                        
                        for point in points+points2:
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
     labelDroit =  pygame.Rect(LARGEUR - LARGEUR/3 ,0, LARGEUR, HAUTEUR) 

    
     vitesse = pygame.Rect(LARGEUR+5 - LARGEUR/3,HAUTEUR-HAUTEUR/3, LARGEUR/3 - 10, HAUTEUR/5)
     boutonStart = pygame.Rect(LARGEUR+5 - LARGEUR/3 + 10, HAUTEUR-HAUTEUR/3 + 5, 50, 25)
     boutonArret = pygame.Rect(LARGEUR+5 - LARGEUR/3 + 55 + 10, HAUTEUR-HAUTEUR/3 + 5, 50, 25)
     sliderTemps = pygame.Rect(LARGEUR+5 - LARGEUR/3 + 10, HAUTEUR-HAUTEUR/3 + 55, 25, 25)
    
    
     pygame.draw.rect(fenetre, GRIS, labelDroit)  
     
    
     pygame.draw.rect(fenetre, GRIS, vitesse )  
     pygame.draw.rect(fenetre, [210, 210, 210], boutonStart, border_radius=7)  
     pygame.draw.rect(fenetre, [210, 210, 210], boutonArret, border_radius=7) 
     pygame.draw.rect(fenetre, [255, 0, 0], sliderTemps) 
    
     texteStart = myfont.render('Start', True, (0, 0, 0))
     fenetre.blit(texteStart,(LARGEUR+5 - LARGEUR/3 + 10 + 10, HAUTEUR-HAUTEUR/3 + 5 +2))
     textePause = myfont.render('Pause', True, (0, 0, 0))
     fenetre.blit(textePause,(LARGEUR+5 - LARGEUR/3 + 55 + 10 + 10, HAUTEUR-HAUTEUR/3 + 5 + 2))
     afficherCourbeConso() 
     afficherCourbeEolienne() 
    
     puissanceTotale= myfont.render('puissanceTotale :'+str(consoGlobale), True, (0, 0, 0))
     fenetre.blit(puissanceTotale,(LARGEUR+5 - LARGEUR/3 +10,(HAUTEUR/3 - 50)*2 + 40 + 150))
  

        
              