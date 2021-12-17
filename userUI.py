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
from Ligne import*

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
consoGlobale = 0 
consoGlobalePrec = 0 

pygame.init()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
myfont = pygame.font.SysFont('Times new roman', 16)
fenetre.fill((58,142,179))

"""AFFICHAGE"""

#milieu
corse = pygame.image.load("corse.png").convert()
corse = pygame.transform.scale(corse, (700,700))
fenetre.blit(corse,(LARGEUR/2-350,HAUTEUR/2-350))


#gauche


    
def dessinerLabelGauche():
    labelGauche = pygame.Rect(0, 0, LARGEUR/3 , HAUTEUR)
    listePoints = pygame.Rect(0, 0, LARGEUR/3 , HAUTEUR/2)
    listeReseaux = pygame.Rect(0, HAUTEUR/2, LARGEUR/3 , HAUTEUR/2)
    

    pygame.draw.rect(fenetre, BLANC, listePoints)  
    pygame.draw.rect(fenetre, BLANC, listeReseaux)
    nomListePoints = myfont.render('Liste des points de production', True, (0, 0, 0))
    fenetre.blit(nomListePoints,(5,0))
    nomListeReseaux = myfont.render('Liste des réseaux ', True, (0, 0, 0))
    fenetre.blit(nomListeReseaux,(5,HAUTEUR/2 + 5))
    


dessinerLabelGauche()
consoGlobaleTab = []  
productionTotaleTab = []   
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
     x = 1

     for i in range(0,len(consoGlobaleTab)-1) :
         pygame.draw.line( surface , (255,0,0) , [x,HAUTEUR/5 - consoGlobaleTab[i] + 150], [x+5,HAUTEUR/5 - consoGlobaleTab[i+1] + 150], 2)
         x+=5
     x=1
     for i in range(0,len(productionTotaleTab)-1) :
         pygame.draw.line( surface , (0,255,0) , [x,HAUTEUR/5 - productionTotaleTab[i] + 150], [x+5,HAUTEUR/5 - productionTotaleTab[i+1] + 150], 2)
         x+=5
     fenetre.blit(surface,(LARGEUR+5 - LARGEUR/3 + 10,10))
     texteSave = myfont.render('Courbe de consommation (mW)', True, (0, 0, 0))
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
     texteSave = myfont.render('Courbe ENR (mW)', True, (0, 0, 0))
     fenetre.blit(texteSave,(LARGEUR+5 - LARGEUR/3 +10,(HAUTEUR/3 - 50)*2 + 40))
     
    
    
labelDroit =  pygame.Rect(LARGEUR - LARGEUR/3 ,0, LARGEUR, HAUTEUR) 


vitesse = pygame.Rect(LARGEUR+5 - LARGEUR/3,HAUTEUR-HAUTEUR/3, LARGEUR/3 - 10, HAUTEUR/5)
boutonStart = pygame.Rect(LARGEUR+5 - LARGEUR/3 + 10, HAUTEUR-HAUTEUR/3 + 5, 50, 25)
boutonRestart = pygame.Rect(LARGEUR+5 - LARGEUR/3 + 55 + 10, HAUTEUR-HAUTEUR/3 + 5, 50, 25)
boutonX1  = pygame.Rect(LARGEUR+5 - LARGEUR/3 + 10, HAUTEUR-HAUTEUR/3 + 55, 25, 25)
boutonX10  = pygame.Rect(LARGEUR+5 - LARGEUR/3 + 40, HAUTEUR-HAUTEUR/3 + 55, 25, 25)
boutonX100  = pygame.Rect(LARGEUR+5 - LARGEUR/3 + 70, HAUTEUR-HAUTEUR/3 + 55, 25, 25)
boutonX1000  = pygame.Rect(LARGEUR+5 - LARGEUR/3 + 100, HAUTEUR-HAUTEUR/3 + 55, 25, 25)
texteSave = myfont.render('Facteur de temps :', True, (0, 0, 0))
fenetre.blit(texteSave,(LARGEUR+5 - LARGEUR/3 + 10, HAUTEUR-HAUTEUR/3 + 55))


pygame.draw.rect(fenetre, GRIS, labelDroit)  
 

pygame.draw.rect(fenetre, GRIS, vitesse )  
pygame.draw.rect(fenetre, [210, 210, 210], boutonStart, border_radius=7)  
pygame.draw.rect(fenetre, [210, 210, 210], boutonRestart, border_radius=7) 
boutonX1  = pygame.Rect(LARGEUR+5 - LARGEUR/3 + 10, HAUTEUR-HAUTEUR/3 + 55, 25, 25)
boutonX10  = pygame.Rect(LARGEUR+5 - LARGEUR/3 + 40, HAUTEUR-HAUTEUR/3 + 55, 25, 25)
boutonX100  = pygame.Rect(LARGEUR+5 - LARGEUR/3 + 70, HAUTEUR-HAUTEUR/3 + 55, 25, 25)
boutonX1000  = pygame.Rect(LARGEUR+5 - LARGEUR/3 + 100, HAUTEUR-HAUTEUR/3 + 55, 35, 25)

texte1 = myfont.render(' x1', True, (0, 0, 0))
fenetre.blit(texte1,(LARGEUR+5 - LARGEUR/3 + 20, HAUTEUR-HAUTEUR/3 + 55))
texte10 = myfont.render(' x10', True, (0, 0, 0))
fenetre.blit(texte10,(LARGEUR+5 - LARGEUR/3 + 40 + 20, HAUTEUR-HAUTEUR/3 + 55))
texte100 = myfont.render('x100', True, (0, 0, 0))
fenetre.blit(texte100,(LARGEUR+5 - LARGEUR/3 + 70 + 20 + 30, HAUTEUR-HAUTEUR/3 + 55))
texte1000 = myfont.render('x1000', True, (0, 0, 0))
fenetre.blit(texte1000,(LARGEUR+5 - LARGEUR/3 + 100 + 20 + 50, HAUTEUR-HAUTEUR/3 + 55))

texteSave = myfont.render('Facteur de temps : '+str(facteurTemps), True, (0, 0, 0))
fenetre.blit(texteSave,(LARGEUR+5 - LARGEUR/3 + 10, HAUTEUR-HAUTEUR/3 + 30))  

texteStart = myfont.render('Start', True, (0, 0, 0))
fenetre.blit(texteStart,(LARGEUR+5 - LARGEUR/3 + 10 + 10, HAUTEUR-HAUTEUR/3 + 5 +2))
textePause = myfont.render('Pause', True, (0, 0, 0))
fenetre.blit(textePause,(LARGEUR+5 - LARGEUR/3 + 55 + 10 + 10, HAUTEUR-HAUTEUR/3 + 5 + 2))

afficherCourbeConso() 
afficherCourbeEolienne() 

puissanceTotale= myfont.render('puissanceTotale :'+ str(0), True, (0, 0, 0))
fenetre.blit(puissanceTotale,(LARGEUR+5 - LARGEUR/3 +10,(HAUTEUR/3 - 50)*2 + 40 + 150))
 
consoGlobale= myfont.render('consommation globale :'+str(0), True, (0, 0, 0))
fenetre.blit(consoGlobale,(LARGEUR+5 - LARGEUR/3 +10,(HAUTEUR/3 - 50)*2 + 40 + 150 + 20))
   
    
#droit







def creerPointEol(x,y):
    eolienne = PointProduction("nom","lieu",None,x,y,fenetre,"eolienne.png",True)
    eolienne.dessiner()
    points.append(eolienne)            

def creerPointTherm(x,y):
    thermique = PointProduction("nom","lieu",None,x,y,fenetre,"thermo.png",False)
    thermique.dessiner()
    points.append(thermique)

def creerPointConso(x,y):
    eolienne = PointConsommation("nomlieu",fenetre,x,y)
    eolienne.dessiner()
    points2.append(eolienne)
    
    
creerPointEol(644,561)    
creerPointEol(825,369)  
creerPointConso(721,409)  
creerPointTherm(623,273) 
  

    
def afficherReseaux():
    x = 0
    y = HAUTEUR / 2 + 30
    for lien in reseau :
        pygame.draw.line( fenetre , ORANGE , [lien.pointProd.x, lien.pointProd.y], [lien.pointCons.x,lien.pointCons.y], 5 )
        lien.pointProd.dessiner()
        lien.pointCons.dessiner()                        
        lien.afficher(fenetre,x,y)
        y += 30
        
        
        
def afficherPoints():
    x = 0
    y = 30
    for point in points :         
        point.afficher(x,y)    
        y += 40


def updateEtat():
    for i in range(b-a-1):
        global step,consoGlobale,ProdRenouvelable, productionTotale,score, consoGlobalePrec, productionTotaleTab
        time.sleep((pasTemps/facteurTemps))
        step+=1
        consoGlobalePrec = consoGlobale
        consoGlobale=float(courbeConso[step])
        ProdRenouvelable=float(courbeENR[step]) 
        consoGlobaleTab.append(consoGlobale)
        somme = 0
        for e in points2:
            e.puissance=e.puissance*consoGlobale/100
        for e in points:            
            somme += e.puissance
            
        productionTotale = somme + ProdRenouvelable
        productionTotaleTab.append(productionTotale)
        score =  (productionTotale / consoGlobale)*100
        
        



  
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
        
        
pasTemps=60
facteurTemps=1       
consoGlobale = 0 
consoGlobalePrec = 0 
ProdRenouvelable = 0 
productionTotale = 0   
continuer = 1
isPressed = False
bouton = None
couple = []
step = 0
score = 0
pause = False
while continuer:
     for event in pygame.event.get():
            
            for point in points :
                 if not point.renouvelable :
                     if point.boutonPlus.collidepoint(pygame.mouse.get_pos()) and isPressed==True:
                        point.ajouterPuissance()
                     if point.boutonMoins.collidepoint(pygame.mouse.get_pos()) and isPressed==True:
                        point.baisserPuissance()
                     if point.boutonMoins.collidepoint(pygame.mouse.get_pos()) and isPressed==True:
                        point.baisserPuissance()
                     if point.boutonOnOff.collidepoint(pygame.mouse.get_pos()) and isPressed==True:
                         if point.allumer :
                             point.arreter()
                         else:
                             point.demarrer()
                        
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
           
            if boutonStart.collidepoint(pygame.mouse.get_pos()) and isPressed==True:
                    for p in points2:
                        p.setPuissance(float(courbeConso[step])/len(points2))
                    thread=threading.Thread(target=updateEtat)
                    thread.start()
                   
            
            if boutonRestart.collidepoint(pygame.mouse.get_pos()) and isPressed==True:  
                if not pause :
                    facteurTemps = 0
                    pause = True
                else :
                    facteurTemps = 10
                    pause = False
            if boutonX1.collidepoint(pygame.mouse.get_pos()) and isPressed==True:        
                facteurTemps = 1
            if boutonX10.collidepoint(pygame.mouse.get_pos()) and isPressed==True:        
                facteurTemps = 10
            if boutonX100.collidepoint(pygame.mouse.get_pos()) and isPressed==True:        
                facteurTemps = 100
            if boutonX1000.collidepoint(pygame.mouse.get_pos()) and isPressed==True:        
                facteurTemps = 1000
                    
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
               isPressed = True
        
               
  
            elif event.type == pygame.MOUSEBUTTONUP:
                isPressed = False
              
                
          
               
          
           
        
     pygame.display.flip()  
     dessinerLabelGauche()
     afficherPoints()
     afficherReseaux()
     labelDroit =  pygame.Rect(LARGEUR - LARGEUR/3 ,0, LARGEUR, HAUTEUR) 

    
     vitesse = pygame.Rect(LARGEUR+5 - LARGEUR/3,HAUTEUR-HAUTEUR/3, LARGEUR/3 - 10, HAUTEUR/5)
     boutonStart = pygame.Rect(LARGEUR+5 - LARGEUR/3 + 10, HAUTEUR-HAUTEUR/3 + 5, 50, 25)
     boutonRestart = pygame.Rect(LARGEUR+5 - LARGEUR/3 + 55 + 10, HAUTEUR-HAUTEUR/3 + 5, 50, 25)
     boutonX1  = pygame.Rect(LARGEUR+5 - LARGEUR/3 + 10, HAUTEUR-HAUTEUR/3 + 55, 25, 25)
     boutonX10  = pygame.Rect(LARGEUR+5 - LARGEUR/3 + 40 , HAUTEUR-HAUTEUR/3 + 55, 25+5, 25)
     boutonX100  = pygame.Rect(LARGEUR+5 - LARGEUR/3 + 70 +15, HAUTEUR-HAUTEUR/3 + 55, 25+10, 25)
     boutonX1000  = pygame.Rect(LARGEUR+5 - LARGEUR/3 + 100 + 20 + 15, HAUTEUR-HAUTEUR/3 + 55, 35, 25)
  
    
     pygame.draw.rect(fenetre, GRIS, labelDroit)  
     
    
     pygame.draw.rect(fenetre, GRIS, vitesse )  
     pygame.draw.rect(fenetre, [210, 210, 210], boutonStart, border_radius=7)  
     pygame.draw.rect(fenetre, [210, 210, 210], boutonRestart, border_radius=7) 
     pygame.draw.rect(fenetre,[210, 210, 210] , boutonX1) 
     pygame.draw.rect(fenetre, [210, 210, 210], boutonX10) 
     pygame.draw.rect(fenetre, [210, 210, 210], boutonX100) 
     pygame.draw.rect(fenetre, [210, 210, 210], boutonX1000) 
     
     texte1 = myfont.render(' x1', True, (0, 0, 0))
     fenetre.blit(texte1,(LARGEUR+5 - LARGEUR/3 + 10, HAUTEUR-HAUTEUR/3 + 55))
     texte10 = myfont.render(' x10', True, (0, 0, 0))
     fenetre.blit(texte10,(LARGEUR+5 - LARGEUR/3 + 40 , HAUTEUR-HAUTEUR/3 + 55))
     texte100 = myfont.render('x100', True, (0, 0, 0))
     fenetre.blit(texte100,(LARGEUR+5 - LARGEUR/3 + 70 +10 + 5, HAUTEUR-HAUTEUR/3 + 55))
     texte1000 = myfont.render('x1000', True, (0, 0, 0))
     fenetre.blit(texte1000,(LARGEUR+5 - LARGEUR/3 + 100 +10 + 15 , HAUTEUR-HAUTEUR/3 + 55))
     
     texteSave = myfont.render('Facteur de temps : '+str(facteurTemps) +' timestep', True, (0, 0, 0))
     fenetre.blit(texteSave,(LARGEUR+5 - LARGEUR/3 + 10, HAUTEUR-HAUTEUR/3 + 30))

     texteStart = myfont.render('Start', True, (0, 0, 0))
     fenetre.blit(texteStart,(LARGEUR+5 - LARGEUR/3 + 10 + 10, HAUTEUR-HAUTEUR/3 + 5 +2))
     textePause = myfont.render('Pause', True, (0, 0, 0))
     fenetre.blit(textePause,(LARGEUR+5 - LARGEUR/3 + 55 + 10 + 5, HAUTEUR-HAUTEUR/3 + 5 + 2))
     afficherCourbeConso() 
     afficherCourbeEolienne() 
    
     puissanceTotale= myfont.render('puissanceTotale :'+ str(consoGlobale)+ ' MW', True, (0, 0, 0))
     fenetre.blit(puissanceTotale,(LARGEUR+5 - LARGEUR/3 +10,(HAUTEUR/3 - 50)*2 + 40 + 150))
     carotte = myfont.render('production renouvelable :'+ str(ProdRenouvelable)+ ' MW', True, (0, 0, 0))
     fenetre.blit(carotte,(LARGEUR+5 - LARGEUR/3 +10,(HAUTEUR/3 - 50)*2 + 40 + 150 + 20))
     carotte2 = myfont.render('production totale :'+ str(productionTotale) + ' MW', True, (0, 0, 0))
     fenetre.blit(carotte2,(LARGEUR+5 - LARGEUR/3 +10,(HAUTEUR/3 - 50)*2 + 40 + 150 + 20 + 20))
     carotte3 = myfont.render('Surplus :'+ str(score) + '%', True, (0, 0, 0))
     fenetre.blit(carotte3,(LARGEUR+5 - LARGEUR/3 +10,(HAUTEUR/3 - 50)*2 + 40 + 150 + 20 + 20 + 20))
   

        
            