# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 08:59:18 2021

@author: notta
"""
import csv
from Jeu import loadCourbe

def saveLog(texte):
    with open("config.csv",'w',newline='') as f:
        writer=csv.writer(f)
        for line in texte:
            writer.writerow(line)
        
        

def loadScenario(idScenario):
    scens=loadCourbe(0,240)
    scen1=scens[0:48]
    scen2=scens[48:96]
    scen3=scens[96:144]
    scen4=scens[144:192]
    scen5=scens[192:240]
    scenTab=[scen1,scen2,scen3,scen4,scen5]
    return scenTab[idScenario]

def readLog():
    listElem=[]
    with open("config.csv","r") as f:
        csv_reader=csv.reader(f,delimiter=',')
        for row in csv_reader:
            listParam=[]
            typePoint=row[0]
            nomPoint=row[1]
            lieuPoint=row[2]
            surface=row[3]
            x=row[4]
            y=row[5]
            listParam.append((typePoint,nomPoint,lieuPoint,surface,x,y))
            listElem.append(listParam)
    return listElem
            
            

print(readLog())    
        

    
    
        