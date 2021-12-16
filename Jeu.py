# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 09:48:12 2021

@author: notta
"""

import csv
import matplotlib.pyplot as plt
import PointConsommation
import PointProduction
import time
import threading

step=0
pasTemps=5 #en minutes, constante
facteurTemps=10 #pour accelerer/ralentir
courbeConso=[] #veritable, definie par l'admin
courbeRenouvelable=[] #veritable, definie par l'admin
courbeMain=[] #affiche la conso attendu et la production renouvelable
consoGlobale=0 #mise a jour tous les pas
prodGloabale=0 #mise a jour tous les pas

a=49 #debut de la courbe
b=98 #fin de la courbe

pointsConso=[]
pointsProd=[]

etat=[]


def createPointConso():
    return None

def createPointProd():
    return None

def loadCourbe(a,b):
    global courbeMain
    with open('courbeConso.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count=0
        for row in csv_reader:
            if (line_count>a and line_count<=b):
                courbeMain.append(row)
            line_count+=1



def displayCourbe():#pour le joueur seulement, affiche les courbes historiques
    y_points=[]
    y2_points=[]
    for i in range(48):#48=une journee
        y_points.append(float(courbeMain[i][1]))  
        y2_points.append(float(courbeMain[i][2]))
    plt.plot(y_points)
    plt.plot(y2_points)
    plt.xlabel('temps')
    plt.ylabel('MW')
    plt.show()
    
def updateEtat():
    for i in range(b-a-1):
        global step,consoGlobale
        time.sleep((pasTemps/facteurTemps))
        step+=1
        consoGlobale=courbeMain[step][1]
        print(consoGlobale)
    
def count():
    for i in range(5):
        print(i)
        

loadCourbe(a,b)

#met a jour la consommation tous les intervalles
thread=threading.Thread(target=updateEtat)
thread.start()
    


#initialisation depuis admin IHM



nbPointsConso=0
nbPointsProd=0

nom,lieu=None,None
puissance=0

for i in range(nbPointsConso):
    newPc=PointConsommation(nom,lieu,puissance)
    pointsConso.append(newPc)
    etat.append(newPc)
    
for i in range(nbPointsProd):
    newPp=PointProduction(nom,lieu,puissance)
    pointsProd.append(newPp)
    
    

    
    



#Jeu avec user IHM



#displayCourbe()