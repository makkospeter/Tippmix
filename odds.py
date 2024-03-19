from tabella_statisztika import *
from tabella_class import *
from random import randint
import random

from tabella_class import Tabella, Tabella2
tabella_adatai : list[Tabella] = []
fogadhat_mecss : list = []



def main():
    beolvasas('premier_tabella.csv')
    melyik = 0
    while melyik != 1 and melyik != 2:
        melyik = int(input('Keresni szeretne a csapatok között vagy véletlen felajánlást kíván?(Keres - 1, Véletlen - 2):  '))
    if melyik == 1:
        keres_meccs()
    elif melyik == 2:
        rand_meccs()
    else:
        pass

def beolvasas(faljnev):
    file = open(faljnev, 'r', encoding='utf8')
    file.readline()
    for sor in file:
        tabella_adatai.append(Tabella(sor))
    file.close()

def rand_meccs():
        penz = 1000
        folytat = 4
    # for m in range(1,5):
        
        while folytat != 2:
            folytat = 0
            feltett_penz = 0
            eredmeny = 0
            fogad = 0
            Team1 = 0
            Team2 = 0
            while Team2 == Team1:
                Team1 = randint(0,19)
                
                Team2 = randint(0,19)
                
            print(f'{tabella_adatai[Team1].csapat} VS {tabella_adatai[Team2].csapat}')
            
            wr1 = int(tabella_adatai[Team1].gyozelmek)/ int(tabella_adatai[Team1].merkozesek)
            wr2 = int(tabella_adatai[Team2].gyozelmek)/ int(tabella_adatai[Team2].merkozesek)
            draw = (int(tabella_adatai[Team1].dontetlenek) + int(tabella_adatai[Team2].dontetlenek))/(int(tabella_adatai[Team1].merkozesek) + int(tabella_adatai[Team2].merkozesek))
            # print(f'{int(tabella_adatai[Team1].dontetlenek)} + {int(tabella_adatai[Team2].dontetlenek)} / {int(tabella_adatai[Team1].merkozesek)} + {int(tabella_adatai[Team2].merkozesek)}')
            # print(draw)
            esely3 = 1/draw
            if wr1 > wr2:
                esely2 = ((wr1)/(wr2))+ 1
                esely1 = ((wr2)/(wr1))+1
            else: 
                # wr2 > wr1
                esely1 = (wr2)/(wr1)+ 1
                esely2 = (wr1)/(wr2)+1

            print(f'{round(esely1, 2)} | {round(esely3, 2)} | {round(esely2, 2)}')
            while fogad != 1 and fogad != 2 and fogad != 3:
                fogad = int(input('Tipp(1 - Hazai csapat nyer/ 2 - Döntetlen/ 3 - Vendég csapat nyer): '))
            while feltett_penz <= 0:
                feltett_penz = int(input(f'Mennyi tszeretne feltenni?  (jelenlegi összege {penz}): '))
            
            eredmeny = random.choices([1, 2, 3], weights=[round(100/esely1, 2) , 100/esely3 , 100/esely2])[0]
            print(f'Az eredmény: {eredmeny}')
            print(f'A tipped: {fogad}')
            if eredmeny == fogad == 1:
                print('Nyert')
                penz = (feltett_penz * esely1) + penz
                print(f'Frissített egyenlege: {penz}')
            elif eredmeny == fogad == 2:
                print('Nyert')
                penz = (feltett_penz * esely2) + penz
                print(f'Frissített egyenlege: {penz}')
            elif eredmeny == fogad == 3:
                print('Nyert')
                penz = (feltett_penz * esely3) + penz
                print(f'Frissített egyenlege: {penz}')
            else: 
                print('Vesztett')
                penz = penz - feltett_penz
            while folytat != 1 and folytat != 2:
                folytat = int(input('Szeretné folytatni? (Igen - 1, Nem - 2) '))

        
        # print(tabella_adatai[Team2].csapat)
        
        # print(wr1)
        # odds1 = (wr1)/(1-(wr1))
        # print(odds1)
        # odd1 = 100/(wr1 * 100)
        # print(odd1)
        
        # print(wr2)
        # odds2 = (wr2)/(1-(wr2))
        # odd2 = 100/(wr2 * 100)
        # print(odd2)
        
        
        # print(f'{odd1} / {odd2}')

def keres_meccs():
        penz = 1000
        folytat = 4
    # for m in range(1,5):
        
       
                
        
        
        while folytat != 2:
            folytat = 0
            feltett_penz = 0
            eredmeny = 0
            fogad = 0
            Team1 = 0
            Team2 = 0
            bekeres = input('Csapat neve akire fogadna: ')
            for cs in tabella_adatai:
                if bekeres in cs.csapat:
                    # Team1 = int(cs.helyezes)
                    
                    csapat = cs.csapat
                    
            
                
            while Team2 == Team1:
                
                
                Team2 = randint(0,19)
                print(Team2)
                
            print(f'{csapat} VS {tabella_adatai[Team2].csapat}')
            
            wr1 = int(tabella_adatai[Team1].gyozelmek)/ int(tabella_adatai[Team1].merkozesek)
            wr2 = int(tabella_adatai[Team2].gyozelmek)/ int(tabella_adatai[Team2].merkozesek)
            draw = (int(tabella_adatai[Team1].dontetlenek) + int(tabella_adatai[Team2].dontetlenek))/(int(tabella_adatai[Team1].merkozesek) + int(tabella_adatai[Team2].merkozesek))
            # print(f'{int(tabella_adatai[Team1].dontetlenek)} + {int(tabella_adatai[Team2].dontetlenek)} / {int(tabella_adatai[Team1].merkozesek)} + {int(tabella_adatai[Team2].merkozesek)}')
            # print(draw)
            esely3 = 1/draw
            if wr1 > wr2:
                esely2 = ((wr1)/(wr2))+ 1
                esely1 = ((wr2)/(wr1))+1
            else: 
                # wr2 > wr1
                esely1 = (wr2)/(wr1)+ 1
                esely2 = (wr1)/(wr2)+1

            print(f'{round(esely1, 2)} | {round(esely3, 2)} | {round(esely2, 2)}')
            while fogad != 1 and fogad != 2 and fogad != 3:
                fogad = int(input('Tipp(1 - Hazai csapat nyer/ 2 - Döntetlen/ 3 - Vendég csapat nyer): '))
            while feltett_penz <= 0:
                feltett_penz = int(input(f'Mennyi tszeretne feltenni?  (jelenlegi összege {penz}): '))
            
            eredmeny = random.choices([1, 2, 3], weights=[round(100/esely1, 2) , 100/esely3 , 100/esely2])[0]
            print(f'Az eredmény: {eredmeny}')
            print(f'A tipped: {fogad}')
            if eredmeny == fogad == 1:
                print('Nyert')
                penz = (feltett_penz * esely1) + penz
                print(f'Frissített egyenlege: {penz}')
            elif eredmeny == fogad == 2:
                print('Nyert')
                penz = (feltett_penz * esely2) + penz
                print(f'Frissített egyenlege: {penz}')
            elif eredmeny == fogad == 3:
                print('Nyert')
                penz = (feltett_penz * esely3) + penz
                print(f'Frissített egyenlege: {penz}')
            else: 
                print('Vesztett')
                penz = penz - feltett_penz
            while folytat != 1 and folytat != 2:
                folytat = int(input('Szeretné folytatni? (Igen - 1, Nem - 2) '))
    


    
main()