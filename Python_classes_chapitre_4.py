# -*- coding: utf-8 -*-
class ville:
    def __init__(self,nom):
        self.nom=nom
        self.batiments=[]
    def __del__(self):
        print("destruction ville",self.nom)
    def NbBatiments(self):
        print("le nombre de batiments de la ville {} est {}".format(self.nom, len(self.batiments)))

class batiment:
    def __init__(self,nom):
        self.nom=nom
        self.employes=[]
    def __del__(self):
        print("destruction batiments",self.nom)

class entreprise:
    def __init__(self,nom):
        self.nom=nom
        self.villes=[]
        self.batiments=[]
    def __del__(self):
        print("destruction entreprises",self.nom)
    def NbBatiments(self):
        print("le nombre de batiments de l'entreprise {} est {}".format(self.nom, len(self.batiments)))
        
yoohoo=entreprise("YooHoo")
NewYork=ville("New York")
LosAngeles=ville("Los Angeles")
batimentA=batiment("A")
batimentB=batiment("B")        
batimentC=batiment("C")  
yoohoo.villes=[NewYork,LosAngeles]
NewYork.batiments=[batimentA,batimentB]
LosAngeles.batiments=[batimentC]
batimentA.employes=["martin","Dupond"]
batimentB.employes=["toto"]
batimentC.employes=["Albert","Pierre"]
yoohoo.batiments=NewYork.batiments + LosAngeles.batiments
i=0
for batiment in yoohoo.batiments:
    print(yoohoo.batiments[i].nom)
    i+=1