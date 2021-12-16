# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 09:48:12 2021

@author: notta
"""

import csv
import matplotlib.pyplot as plt
from PointConsommation import PointConsommation
from PointProduction import PointProduction
from Groupe import Groupe
import time
import threading

step=0
pasTemps=5 #en minutes, constante
facteurTemps=10 #pour accelerer/ralentir
courbeConso=[] #veritable, definie par l'admin
courbeRenouvelable=[] #veritable, definie par l'admin
courbeMain=[] #affiche la conso attendu et la production renouvelable


a=49 #debut de la courbe
b=98 #fin de la courbe

pointsConso=[]
pointsProd=[]

etat=[]


def loadCourbe(a,b):
    global courbeMain
    with open('courbeConso.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count=0
        for row in csv_reader:
            if (line_count>a and line_count<=b):
                courbeMain.append(row)
            line_count+=1
            
loadCourbe(a, b)

consoGlobale=float(courbeMain[0][1]) #mise a jour tous les pas
prodGlobale=0 #mise a jour tous les pas
ProdRenouvelable=float(courbeMain[0][2]) #mise a jour tous les pas
'''
def createPointConso(nbPointsConso):
    for i in range(nbPointsConso):
        nom=input("point conso: nom ")
        lieu=input("lieu ")
        puissance=float(input("puissance en % ")) #puissance: pourcentage du total
        newPc=PointConsommation(nom,lieu,puissance*consoGlobale/100)
        pointsConso.append(newPc)
etat.append(pointsConso)

def createPointProd(nbPointsProd):
    for i in range(nbPointsProd):
        nom=input("point prod: nom ")
        lieu=input("lieu ")
        nbGroupes=int(input("nb de groupes: "))
        lstGrp=[]
        for j in range(nbGroupes):
            nom=input("Groupe: nom: ")
            puissance=float(input("puissance "))
            groupe=Groupe(nom,puissance)
            lstGrp.append(groupe)
        newPp=PointProduction(nom,lieu,lstGrp)
        pointsProd.append(newPp)
etat.append(pointsProd)
'''
def createPointProd(nom,lieu):
    newPp=PointProduction(nom,lieu,None)
    pointsProd.append(newPp)
    etat.append(pointsProd)
    
def createPointConso(nom,lieu, puissance):
    newPc=PointConsommation(nom,lieu,puissance*consoGlobale/100)
    pointsConso.append(newPc)
    etat.append(pointsConso)


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
        consoGlobale=float(courbeMain[step][1])
        ProdRenouvelable=float(courbeMain[step][2])   
        for e in etat:
            if isinstance(e,PointConsommation):
                e.puissance=e.puissance*consoGlobale/100
        print(etat)
    
def activerGroupe(pointProd, idGroup):
    pointProd.getGroup(idGroup).activate()
    
def desactiverGroupe(pointProd, idGroup):
    pointProd.getGroup(idGroup).deactivate()






#initialisation depuis admin IHM



nbPointsConso=2
nbPointsProd=1

#createPointConso()

#createPointProd()

    

    

    
    



#Jeu avec user IHM




#met a jour la consommation tous les intervalles
thread=threading.Thread(target=updateEtat)
thread.start()
#print(pointsConso)




#displayCourbe()