import csv

#### fonction ####
def ouvrir(nom_fichier,sep):                                #cette fonction nous permet d'ouvrir les fichier csv 2008,2016,2021.
    L=[]
    with open(nom_fichier,newline='') as csvfile:
        reader=csv.reader(csvfile,delimiter=sep)
        for row in reader:
            L.append(row)
        del L[0]
    return L



def sommes_pop_années(L):
    som=0
    for b in L:
        som+=int(b[-1])
    return som

def code_commune():
    L=[]
    L2=[]
    L3=[]
    for c in L2008_2:
        L.append([int(c[2])*1000+int(c[5]),c[6]])
    L2=["Appoigny", "Augy", "Auxerre", "Bleigny-le-Carreau", "Branches", "Champs-sur-Yonne", "Charbuy","Chevannes", "Chitry", "Coulanges-la-Vineuse", "Escamps", "Escolives Sainte-Camille", "Gurgy","Gy-l’Eveque", "Irancy", "Jussy", "Lindry", "Mon´eteau", "Montigny-la-Resle", "Perrigny", "Quenne","Saint-Bris-le-Vineux", "Saint-Georges-sur-Baulche", "Vallan", "Venoy", "Villefargeau", "Villeneuve-Saint-Salves", "Vincelles, Vincelottes"]
    for truc in L2:
        for machin in L:
            if truc==machin[1]:
                L3.append(machin)
    return(L3)
                 


#### code principal ####
#ceci est un rappel si vous l'aviez pas compris
L2=["Appoigny", "Augy", "Auxerre", "Bleigny-le-Carreau", "Branches", "Champs-sur-Yonne", "Charbuy","Chevannes", "Chitry", "Coulanges-la-Vineuse", "Escamps", "Escolives Sainte-Camille", "Gurgy","Gy-l’Eveque", "Irancy", "Jussy", "Lindry", "Mon´eteau", "Montigny-la-Resle", "Perrigny", "Quenne","Saint-Bris-le-Vineux", "Saint-Georges-sur-Baulche", "Vallan", "Venoy", "Villefargeau", "Villeneuve-Saint-Salves", "Vincelles, Vincelottes"]

L2008=ouvrir("donnees_2008.csv",",")
L2008_2=[]
for a in L2008:
    if a[2]=="89":
        L2008_2.append(a)

Liste_nom_code=code_commune()           #nous permet de trier pour obtenir l'aglomération totale.


L2008_3=[]
for a in Liste_nom_code:
    for b in L2008_2:
        if a[0]==(int(b[2])*1000+int(b[5])):
            L2008_3.append(b)



L2016=ouvrir("donnees_2016.csv",",")
L2016_2=[]
for a in L2016:
    if a[2]=="89":
        L2016_2.append(a)

L2016_3=[]
for a in Liste_nom_code:
    for b in L2016_2:
        if a[0]==(int(b[2])*1000+int(b[5])):
            L2016_3.append(b)

print(L2016_3)

L2021=ouvrir("donnees_2021.csv",";")
L2021_2=[]
for a in Liste_nom_code:
    for b in L2021:
        if str(a[0])==b[2]:
            L2021_2.append(b)



pop2008=sommes_pop_années(L2008_3)
pop2016=sommes_pop_années(L2016_3)
pop2021=sommes_pop_années(L2021_2)

print(pop2008)
print(pop2016)
print(pop2021)

####affichage courbe agglomération totale####

dates=[2008,2016,2021]
popu2008 = []
popu2016 = []
popu2021 = []

popu2008.append(pop2008)
popu2016.append(pop2016)
popu2021.append(pop2021)

from matplotlib import pyplot as plt

plt.plot(dates,popu2008,color='b')
plt.plot(dates,popu2016,color='r')
plt.plot(dates,popu2021,color='g')
plt.scatter(dates,popu2008,color='b')
plt.scatter(dates,popu2016,color='r')
plt.scatter(dates,popu2021,color='g')
plt.title("Population à Auxerre agglomération générale")
plt.ylabel('Population')
plt.xlabel('Années')
plt.show()

## DOnc la population décroit bien.