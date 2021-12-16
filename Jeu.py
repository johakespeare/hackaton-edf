# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 09:48:12 2021

@author: notta
"""

import csv
import matplotlib.pyplot as plt
import numpy as np

pasTemps=30 #en minutes, constante
facteurTemps=1 #pour accelerer/ralentir
courbeConso=[] #veritable, definie par l'admin
courbeRenouvelable=[] #veritable, definie par l'admin
courbeMain=[] #affiche la conso attendu et la production renouvelable
consoGlobale=0 #mise a jour tous les pas
prodGloabale=0 #mise a jour tous les pas
a=49 #debut de la courbe
b=98 #fin de la courbe

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
    print(y_points)
    plt.plot(y_points)
    plt.plot(y2_points)
    plt.xlabel('temps')
    plt.ylabel('MW')
    plt.show()

        

    
    

#initialisation depuis admin IHM



nbPointsConso=0
nbPointsProd=0

for i in range(nbPointsConso):
    createPointConso()
    
for i in range(nbPointsProd):
    createPointProd()
    

    
    



#Jeu avec user IHM

loadCourbe(a,b)

displayCourbe()