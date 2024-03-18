from tabella_statisztika import *
from tabella_class import *
from random import randint

from tabella_class import Tabella, Tabella2
tabella_adatai : list[Tabella] = []
fogadhat_mecss : list = []

penz = 1000

def main():
    beolvasas('premier_tabella.csv')
    rand_meccs()
    fogad()


def beolvasas(faljnev):
    file = open(faljnev, 'r', encoding='utf8')
    file.readline()
    for sor in file:
        tabella_adatai.append(Tabella(sor))
    file.close()

def rand_meccs():
    for m in range(1,5):
        Team1 = 0
        Team2 = 0
        while Team2 == Team1:
            Team1 = randint(0,19)
            
            Team2 = randint(0,19)
            
        print(f'{tabella_adatai[Team1].csapat} VS {tabella_adatai[Team2].csapat}')
        
        wr1 = int(tabella_adatai[Team1].gyozelmek)/ int(tabella_adatai[Team1].merkozesek)
        wr2 = int(tabella_adatai[Team2].gyozelmek)/ int(tabella_adatai[Team2].merkozesek)
        if wr1 > wr2:
            esely2 = ((wr1)/(wr2))+ 1
            esely1 = ((wr2)/(wr1))+1
        else: 
            # wr2 > wr1
            esely1 = ((wr2)/(wr1))+ 1
            esely2 = ((wr1)/(wr2))+1
        print(f'{esely1} / {esely2}')
    
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


    


    
main()